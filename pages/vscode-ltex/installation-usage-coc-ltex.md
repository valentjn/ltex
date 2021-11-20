---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Installation and Usage (coc-ltex)"
permalink: "/vscode-ltex/installation-usage-coc-ltex.html"
sidebar: "sidebar"
---

## Download Providers

- Download from within coc.nvim: Run `:CocInstall coc-ltex`
- [npm](https://www.npmjs.com/package/coc-ltex) (coc.nvim uses this for downloading)
- [Source on GitHub](https://github.com/valentjn/vscode-ltex)

## Requirements

- 64-bit Linux, Mac, or Windows operating system
- [Node.js 14.16.0 or later](https://nodejs.org/)
- [Vim](https://www.vim.org/) or [Neovim](https://neovim.io/) with [coc.nvim 0.0.80 or later](https://github.com/neoclide/coc.nvim)

## How to Install and Use

1. Install the requirements listed above
2. Install coc-ltex by running `:CocInstall coc-ltex`
3. If you want to check LaTeX documents: Add `let g:coc_filetype_map = {'tex': 'latex'}` to `~/.vimrc` (Vim) or `~/.config/nvim/init.vim` (workaround for [#425](https://github.com/valentjn/vscode-ltex/issues/425), until [neoclide/coc.nvim#3433](https://github.com/neoclide/coc.nvim/pull/3433) is released)
4. Open a LaTeX or a Markdown document
5. Wait until [ltex-ls](../faq.html#whats-the-difference-between-vscode-ltex-ltex-ls-and-languagetool) has been downloaded and started
6. Grammar/spelling errors will be displayed! (if there are any)
