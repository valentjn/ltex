---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Installation and Usage (vscode-ltex)"
permalink: "/vscode-ltex/installation-usage-vscode-ltex.html"
sidebar: "sidebar"
---

## Download Providers

- Download from within VS Code: Open the *Extensions* panel and type `ltex`
- [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) (VS Code uses this for downloading)
- [Open VSX](https://open-vsx.org/extension/valentjn/vscode-ltex)
- [Releases on GitHub](https://github.com/valentjn/vscode-ltex/releases) (+ packages for offline installation)
- [Source on GitHub](https://github.com/valentjn/vscode-ltex)

## Requirements

- 64-bit Linux, Mac, or Windows operating system
- [VS Code 1.52.0 or later](https://code.visualstudio.com/) (new versions of LTeX released on or after January 14, 2022, will require VS Code 1.61.0 or later)
- Optional:
  - If you want to check LaTeX documents: [LaTeX Workshop Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
  - If you want to check Org documents: [Org Mode Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=tootone.org-mode)
  - If you want to check reStructuredText documents: [reStructuredText Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext)

## How to Install and Use

1. Install the requirements listed above
2. Install this extension
3. Reload the VS Code window if necessary
4. Open a LaTeX or a Markdown document, or open a new file and change the language mode to `LaTeX` or `Markdown` (open the Command Palette and select `Change Language Mode`)
5. Wait until [ltex-ls](../faq.html#whats-the-difference-between-vscode-ltex-ltex-ls-and-languagetool) has been found; if necessary, LTeX downloads it for you. Alternatively, you can choose [offline installation](#offline-installation).
6. Grammar/spelling errors will be displayed! (if there are any)

## Offline Installation

The key component of LTeX, the LTeX Language Server (ltex-ls), which also includes Java and LanguageTool, cannot be included in the LTeX version distributed on the Visual Studio Marketplace due to file size restrictions.

When activated for the first time, LTeX will automatically download and use a hard-coded ltex-ls release from GitHub. It will be stored in the extension folder. Note that after this initial installation, no connection to the Internet is necessary. Checking your documents is completely offline.

If you don't have an Internet connection, or if you simply don't want this, there are two alternatives.

In case there are any problems, you will find additional debug info in `View` → `Output` → `LTeX Language Server` and `LTeX Language Client`.

### First Alternative: Download the Offline Version of LTeX

Download the offline version of LTeX at the [Releases page on GitHub](https://github.com/valentjn/vscode-ltex/releases) and install it via `Extensions: Install from VSIX...` on the Command Palette. The offline version already includes ltex-ls (and the portable Java distribution). Reload the Visual Studio Code window after installing the offline version.

### Second Alternative: Download ltex-ls/Java Manually

Download [ltex-ls](https://github.com/valentjn/ltex-ls/releases) and/or a Java distribution (e.g., [Eclipse Adoptium](https://adoptium.net/)) individually and set [`ltex.ltex-ls.path`](../settings.html#ltexltex-lspath) and/or [`ltex.java.path`](../settings.html#ltexjavapath) to the respective locations. If you download a binary release of ltex-ls (those include a platform in the archive file name), then that release already includes Java and you don't need to set [`ltex.java.path`](../settings.html#ltexjavapath).

Note that the versions of ltex-ls and/or Java have to satisfy the following requirements:

- Each version of LTeX has been tested with exactly one version of ltex-ls, which is the version that LTeX automatically downloads. If you download ltex-ls manually, be sure to use this version of ltex-ls. An older or a newer version of ltex-ls might work, or it might not.

  For this reason, this approach is not recommended as automatically updated versions of LTeX (by Visual Studio Code) might not be compatible anymore with your manually downloaded version of ltex-ls. If you choose this approach, remember to update ltex-ls if LTeX doesn't work anymore.

  To find out which version a particular version of LTeX uses, check the [changelog](changelog.html) for `Update LTeX LS to X.Y.Z`. If there is no entry of this form in the changelog for the version of LTeX you want to use, use the entry of the first previous version of LTeX that has such an entry.
- The version of Java must be at least 11. Some Java distributions offer a JRE (Java Runtime Environment) and a JDK (Java Development Kit); in this case, the JRE is sufficient.

If you download Java, you can also decide to install it system-wide. In this case, LTeX should be able to automatically detect its location. If not, you can still set [`ltex.java.path`](../settings.html#ltexjavapath) to the location of your system-wide installation.

Reload the Visual Studio Code window after installing ltex-ls and/or Java.
