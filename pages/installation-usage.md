---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Installation and Usage"
permalink: "/installation-usage.html"
sidebar: "sidebar"
---

The installation of LTeX depends on the scenario in which you want to use LTeX. LTeX can be used
- [as an extension for your editor](#via-editor-extensions),
- [as a language client using the Language Server Protocol (LSP)](#via-language-clients), or
- [standalone on the command line](#via-command-line).

Choose the topmost scenario that applies to you.

## Via Editor Extensions

LTeX publishes official extensions for Visual Studio Code (VS Code) and Vim/Neovim via coc.nvim. For some other popular editors, third-party extensions exist that add support for LTeX. If no extension exists yet for your editor, but your editor supports the Language Server Protocol (LSP), then you should be able to [use LTeX as a language client](#via-language-clients).

### Official Extensions

| Editor | Extension | Link to instructions |
| ------ | --------- | -------------------- |
| [VS Code](https://code.visualstudio.com/) | vscode-ltex | [Instructions](vscode-ltex/installation-usage-vscode-ltex.html) |
| [Vim](https://www.vim.org/)/[Neovim](https://neovim.io/) + [coc.nvim](https://github.com/neoclide/coc.nvim) | coc-ltex | [Instructions](vscode-ltex/installation-usage-coc-ltex.html) |

### Third-Party Extensions

LTeX is not responsible for the quality of third-party extensions. The list and corresponding links are provided for your information only.

| Editor | Extension | Link to instructions |
| ------ | --------- | -------------------- |
| [Emacs](https://www.gnu.org/software/emacs/) + [eglot](https://github.com/joaotavora/eglot) | eglot-ltex | [Instructions](https://github.com/emacs-languagetool/eglot-ltex) |
| [Emacs](https://www.gnu.org/software/emacs/) + [lsp-mode](https://github.com/emacs-lsp/lsp-mode) | lsp-ltex | [Instructions](https://github.com/emacs-languagetool/lsp-ltex) |
| [Neovim](https://neovim.io/) | Grammar Guard | [Instructions](https://github.com/brymer-meneses/grammar-guard.nvim) |
| [Neovim](https://neovim.io/) | nvim-lsp-installer | [Instructions](https://github.com/williamboman/nvim-lsp-installer) |
| [Neovim](https://neovim.io/) + [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) | lbiaggi/ltex.lua | [Instructions](https://gist.github.com/lbiaggi/a3eb761ac2fdbff774b29c88844355b8) |
| [Neovim](https://neovim.io/) + [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) | LTeX_extra.nvim | [Instructions](https://github.com/barreiroleo/ltex_extra.nvim) |
| [Sublime Text](https://www.sublimetext.com/) | LSP-ltex-ls | [Instructions](https://github.com/LDAP/LSP-ltex-ls) |

## Via Language Clients

If your editor is not yet supported by an extension, but it supports the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/), then you can use the language server [LTeX LS (read here for instructions)](ltex-ls/installation.html).

Typically, the editor starts LTeX LS during startup (either locally or remotely), it sends LTeX LS your L<sup>A</sup>T<sub>E</sub>X or Markdown document, and LTeX LS will respond with a list of the grammar and spelling errors in it. The communication between server and editor is done using the LSP, with a language client as a communication endpoint that runs in the editor.

If your editor already supports the LSP (either natively or via an extension), then writing a language client for LTeX should be possible with almost no overhead. If your editor doesn't support the LSP, then you can write a language client yourself that communicates with LTeX LS according to the [LSP specification](https://microsoft.github.io/language-server-protocol/).

## Via Command Line

LTeX can be run on the command line. In this mode, you supply LT<sub>E</sub>X paths to files and directories to be checked as command-line arguments. The results will be printed to the standard output, and no language client or knowledge of the Language Server Protocol (LSP) is necessary.

The command-line interface (CLI) of LTeX is included in LTeX LS. [Read here for instructions.](ltex-ls/cli-usage.html)
