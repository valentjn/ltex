#!/usr/bin/python3

# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import functools
import json
import os
import pathlib
import re
from typing import Dict, Sequence



def replaceSettingsCommandsMatch(markdownPath: pathlib.Path, pagesDirPath: pathlib.Path,
      markdown: str, settingNames: Sequence[str], commandNames: Dict[str, str],
      match: re.Match[str]) -> str:
  markdownName = markdownPath.name
  pageNameMatch = re.match(r"^.*-([a-z]{2})\.md$", markdownName)
  pageNameSuffix = (f"-{pageNameMatch.group(1)}" if pageNameMatch is not None else "")

  i = markdown.rfind("\n", 0, match.start())
  contextBefore = markdown[i+1:match.start()]
  if re.search(r"^#+\s*", contextBefore): return match.group(0)
  text = (match.group(1) if match.group(1) is not None else match.group(2))

  if text in commandNames.values():
    key = next(x for x, y in commandNames.items() if y == text)
  else:
    key = text

  if key in settingNames:
    url = "{}#{}".format(pagesDirPath.joinpath(
        "docs", f"settings{pageNameSuffix}.html").relative_to(markdownPath.parent), getSlug(key))
    return f"[`{text}`]({url})"
  elif key in commandNames:
    url = "{}#{}".format(pagesDirPath.joinpath(
        "docs", f"commands{pageNameSuffix}.html").relative_to(markdownPath.parent), getSlug(key))
    return f"[`{text}`]({url})"
  else:
    return f"`{text}`"

def getSlug(markdown: str) -> str:
  return re.sub(r"[^a-z0-9\-]", "", re.sub(r"[ ]", "-", markdown.lower()))

def replaceNlsKey(packageNlsJson: Dict[str, str], match: re.Match[str]) -> str:
  key = match.group(1)
  if key not in packageNlsJson: raise RuntimeError("unknown NLS key '{}'".format(key))
  return packageNlsJson[key]

def formatTitle(description: str, packageNlsJson: Dict[str, str]) -> str:
  return re.sub(r"%([A-Za-z0-9\-_\.]+)%", functools.partial(replaceNlsKey, packageNlsJson),
      description)

def linkSettingsAndCommands(markdownPath: pathlib.Path, pagesDirPath: pathlib.Path,
      ltexRepoDirPath: pathlib.Path) -> None:
  markdownName = markdownPath.name
  pageNameMatch = re.match(r"^.*-([a-z]{2})\.md$", markdownName)
  packageNlsJsonSuffix = (f".{pageNameMatch.group(1)}" if pageNameMatch is not None else "")

  packageJsonPath = ltexRepoDirPath.joinpath("package.json")
  with open(packageJsonPath, "r") as f: packageJson = json.load(f)

  packageNlsJsonPath = ltexRepoDirPath.joinpath(f"package.nls{packageNlsJsonSuffix}.json")
  with open(packageNlsJsonPath, "r") as f: packageNlsJson = json.load(f)

  settingsJson = packageJson["contributes"]["configuration"]["properties"]
  settingNames = [x for x in settingsJson.keys() if "markdownDescription" in settingsJson[x]]

  commandsJson = packageJson["contributes"]["commands"]
  commandNames = {"{}: {}".format(x["category"], formatTitle(x["title"], packageNlsJson)) :
      x["command"] for x in commandsJson}

  with open(markdownPath, "r") as f: markdown = f.read()
  markdown = re.sub(r"`(ltex\.[^`]+|LTeX: [^`]+)`|\[`(ltex\.[^`]+|LTeX: [^`]+)`\]\([^\)]*?\)",
      functools.partial(replaceSettingsCommandsMatch, markdownPath, pagesDirPath, markdown,
        settingNames, commandNames), markdown)
  with open(markdownPath, "w") as f: f.write(markdown)



def main() -> None:
  parser = argparse.ArgumentParser(description="link settings in all pages")
  parser.add_argument("--ltex-repo",
      default=pathlib.Path(__file__).parent.parent.parent.joinpath("vscode-ltex"),
      help="path to main repo")
  args = parser.parse_args()

  pagesDirPath = pathlib.Path(__file__).parent.parent.joinpath("pages")
  ltexRepoDirPath = args.ltex_repo

  for root, dirNames, fileNames in os.walk(pagesDirPath):
    dirNames.sort()

    for fileName in fileNames:
      if fileName.endswith(".md"):
        linkSettingsAndCommands(
            pathlib.Path(root).joinpath(fileName), pagesDirPath, ltexRepoDirPath)

if __name__ == "__main__":
  main()
