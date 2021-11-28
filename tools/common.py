#!/usr/bin/python3

# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pathlib
import re
import subprocess
from typing import Tuple



def isRemotePath(path: pathlib.Path) -> bool:
  return (":" in path.parts[0]) and (len(path.parts[0]) >= 4)

def getRemotePathParts(filePath: pathlib.Path) -> Tuple[str, pathlib.PurePosixPath]:
  assert isRemotePath(filePath)
  remoteFilePath = str(pathlib.PurePosixPath(filePath))
  remoteHostName, remoteFilePath = remoteFilePath.split(":")
  return remoteHostName, pathlib.PurePosixPath(remoteFilePath)

def readFile(filePath: pathlib.Path) -> str:
  if isRemotePath(filePath):
    remoteHostName, remoteFilePath = getRemotePathParts(filePath)
    process = subprocess.run(["ssh", remoteHostName, "cat", str(remoteFilePath)],
        stdout=subprocess.PIPE)
    text = process.stdout.decode()
  else:
    with open(filePath, "r", encoding="utf-8", newline="\n") as file:
      text = file.read()

  return text.replace("\r\n", "\n")

def writeFile(filePath: pathlib.Path, text: str) -> None:
  assert not isRemotePath(filePath)

  with open(filePath, "w", encoding="utf-8", newline="\n") as file:
    file.write(text.replace("\r\n", "\n"))



def getSlug(markdown: str) -> str:
  return re.sub(r"[^a-z\xe4\xf6\xfc\xdf0-9\-_]", "",
      re.sub(r"&#x?[0-9A-Za-z]+?;", "", re.sub(r"[ ]", "-", markdown.lower())))
