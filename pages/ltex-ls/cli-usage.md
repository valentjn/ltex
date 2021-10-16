---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "CLI Usage"
permalink: "/ltex-ls/cli-usage.html"
sidebar: "sidebar"
---

LTeX CLI is contained in LTeX LS. To use LTeX CLI, [download and install LTeX LS](installation.html) first.

## Startup

It is recommended to use the startup scripts `bin/ltex-cli` (Linux, Mac) and `bin\ltex-cli.bat` (Windows) to start LTeX CLI. These scripts are only part of the released versions (they are not contained in the source repository).

The startup scripts can be controlled by the following environment variables:

- `JAVA_HOME`: Path to the directory of the Java distribution to use (contains `bin`, `lib`, and other subdirectories). If set, this overrides the included Java distribution when using a platform-dependent LTeX LS archive.
- `JAVA_OPTS`: Java arguments to be fed to `java` (e.g., `-Xmx1024m`)

It is also possible to start LTeX CLI directly without the startup scripts (not recommended).

### Command-Line Arguments

Any command-line arguments supplied to the startup scripts are processed by LTeX CLI itself. The possible arguments are as follows:

- `--client-configuration=<file>`: Use the client configuration stored in the JSON file `<file>`. The format is nested JSON objects (e.g., `{"latex": {"commands": ...}}`). A flattened JSON object (`{"latex.commands": ...}`) is also allowed, and setting names may be prefixed by a top level named `ltex` (e.g., `{"ltex.latex.commands": ...}` is accepted as well).
- `-h`, `--help`: Show help message and exit.
- `-V`, `--version`: Print version information as JSON to the standard output and exit. The format is a JSON object with `"java"` and `"ltex-ls"` keys and string values. A key may be missing if no information about the corresponding version could be retrieved.
- `<path> <path> ...`: Required. Paths of files or directories to check. Directories are traversed recursively for supported file types. If `-` is given, standard input will be checked as plain text.

Instead of using the equals sign `=` to separate option names and values, it is also possible to use one or more spaces.

### Exit Codes

- 0: LTeX CLI exited successfully and no grammar/spelling errors were found.
- 1: An exception was thrown during the execution of LTeX CLI.
- 2: An invalid command-line argument was supplied to LTeX CLI.
- 3: At least one grammar/spelling error was found.
