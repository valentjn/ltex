#!/usr/bin/python3

# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import functools
import os
import pathlib
import re
import sys
from typing import Any, Callable, Dict, Sequence

sys.path.append(str(pathlib.Path(__file__).parent))
import common



def getAnchorsInPage(pageFilePath: pathlib.Path) -> Sequence[str]:
  markdown = common.readFile(pageFilePath)
  if markdown.startswith("---"): markdown = markdown[markdown.index("---", 3)+3:]
  anchors = [common.getSlug(x) for x in re.findall(r"^#+\s+(.*)$", markdown, flags=re.MULTILINE)]
  return anchors



def checkLinksInPage(anchors: Dict[str, Sequence[str]],
      pagesDirPath: pathlib.Path, pageFilePath: pathlib.Path) -> int:
  markdown = common.readFile(pageFilePath)
  urls = re.findall(r"\[.*?\]\((.*?)\)", markdown)
  numberOfProblems = 0

  for url in urls:
    if re.search("^https?://(?!valentjn.github.io/ltex/)", url) is not None: continue

    regexMatch = re.search(r"^(.*?)(?:#(.*))?$", url)

    if regexMatch is None:
      print(f"Invalid URL '{url}' found in '{pageFilePath}'.")
      numberOfProblems += 1
      continue

    urlPathRelative = regexMatch.group(1)
    assert urlPathRelative is not None
    if urlPathRelative == "": urlPathRelative = f"{pageFilePath.stem}.html"
    urlAnchor = regexMatch.group(2)

    if re.search("^https://valentjn.github.io/ltex", url) is not None:
      urlPathRelativeToPages = re.sub("^https://valentjn.github.io/ltex/", "", urlPathRelative)
    else:
      urlPath = pageFilePath.parent.joinpath(urlPathRelative).resolve()
      urlPathRelativeToPages = os.path.relpath(urlPath, start=pagesDirPath).replace("\\", "/")

    if not urlPathRelativeToPages.endswith(".html"):
      print(f"Path '{urlPathRelativeToPages}' in URL '{url}' found in '{pageFilePath}' "
          "does not end with '.html'.")
      numberOfProblems += 1
      continue

    urlPathRelativeToPages = urlPathRelativeToPages[:-5]

    if urlPathRelativeToPages not in anchors:
      print(f"Path '{urlPathRelativeToPages}' in URL '{url}' found in '{pageFilePath}' not found.")
      numberOfProblems += 1
      continue

    if (urlAnchor is not None) and (urlAnchor not in anchors[urlPathRelativeToPages]):
      print(f"Anchor '{urlAnchor}' in URL '{url}' found in '{pageFilePath}' not found.")
      numberOfProblems += 1
      continue

  return numberOfProblems



def runRecursively(function: Callable[[pathlib.Path], Any],
      pagesDirPath: pathlib.Path,) -> Dict[str, Any]:
  result = {}

  for root, dirNames, fileNames in os.walk(pagesDirPath):
    dirNames.sort()

    for fileName in fileNames:
      if fileName.endswith(".md"):
        pageFilePath = pathlib.Path(root).joinpath(fileName)
        result[os.path.relpath(pageFilePath, start=pagesDirPath).replace("\\", "/")[:-3]] = (
            function(pageFilePath))

  return result



def main() -> None:
  pagesDirPath = pathlib.Path(__file__).parent.parent.joinpath("pages")

  anchors = runRecursively(getAnchorsInPage, pagesDirPath)
  numbersOfProblems = runRecursively(functools.partial(checkLinksInPage, anchors, pagesDirPath),
      pagesDirPath)

  numberOfProblems = sum(int(x) for x in numbersOfProblems.values())
  assert numberOfProblems == 0, \
      f"Found {numberOfProblems} problem{'' if numberOfProblems == 1 else 's'}."

  print("Check successful.")



if __name__ == "__main__":
  main()
