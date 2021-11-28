---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Changelog"
permalink: "/vscode-ltex/changelog.html"
sidebar: "sidebar"
toc: false
---

## Upcoming Fundamental Changes

- New versions of LTeX released on or after January 14, 2022, will require VS Code 1.61.0 or later

## 13.1.0 &#x2014; &#x201c;The ConTeXt Paradigm&#x201d; (November 28, 2021)

- &#x2728; *New:* Add support for ConTeXt &#x2014; [ltex-ls#120](https://github.com/valentjn/ltex-ls/issues/120)
- &#x2728; *New:* Add support for strikethrough as in [GitHub Flavored Markdown](https://github.github.com/gfm/#strikethrough-extension-) &#x2014; [ltex-ls#123](https://github.com/valentjn/ltex-ls/issues/123)
- &#x2728; *New:* Always check selected text when running [`LTeX: Check Selection`](commands.html#ltex-check-selection), even non-comment parts of programs &#x2014; [#457](https://github.com/valentjn/vscode-ltex/issues/457)
- &#x2728; *New:* Add support for the `minted` package (LaTeX) &#x2014; [#463](https://github.com/valentjn/vscode-ltex/issues/463)
- &#x2728; *New:* Add support for the Pandoc language variable `lang` in YAML front matter (Markdown) &#x2014; [#465](https://github.com/valentjn/vscode-ltex/issues/465)
- &#x1f527; *Change:* Update LTeX LS to 15.2.0

## 13.0.0 &#x2014; &#x201c;The Completion Setting Excitation&#x201d; (October 30, 2021)

- &#x1f527; *Change:* Add [`ltex.completionEnabled`](../settings.html#ltexcompletionenabled) to disable completion by default &#x2014; [#443](https://github.com/valentjn/vscode-ltex/issues/443)
- &#x1f41b; *Bug fix:* Fix `StringIndexOutOfBoundsException` in `AnnotatedTextFragment.getSubstringOfPlainText` &#x2014; [#442](https://github.com/valentjn/vscode-ltex/issues/442)
- &#x1f41b; *Bug fix:* Fix handling of multiple subsequent whitespace characters in XHTML (e.g., CRLF)
- &#x1f527; *Change:* Update LTeX LS to 15.0.0

## 12.2.0 &#x2014; &#x201c;The Completion Hypothesis&#x201d; (October 19, 2021)

- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolHttpServerUri` &#x2192; [`ltex.languageToolHttpServerUri`](../settings.html#ltexlanguagetoolhttpserveruri); the previous name is deprecated
- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolOrgUsername` &#x2192; [`ltex.languageToolOrg.username`](../settings.html#ltexlanguagetoolorgusername); the previous name is deprecated
- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolOrgApiKey` &#x2192; [`ltex.languageToolOrg.apiKey`](../settings.html#ltexlanguagetoolorgapikey); the previous name is deprecated
- &#x2728; *New:* Add completion support for English and German (begin typing a word and press `Ctrl+Space`) &#x2014; [#409](https://github.com/valentjn/vscode-ltex/issues/409)
- &#x1f41b; *Bug fix:* Fix `Add '...' to dictionary` quick fix missing for Austrian and Swiss German &#x2014; [#431](https://github.com/valentjn/vscode-ltex/issues/431)
- &#x1f527; *Change:* Move documentation to <https://valentjn.github.io/ltex>
- &#x1f527; *Change:* Update LTeX LS to 14.1.0

## 12.1.0 &#x2014; &#x201c;The coc.nvim Diffusion&#x201d; (October 16, 2021)

- &#x2728; *New:* Publish coc.nvim version as coc-ltex to npm

## 12.0.0 &#x2014; &#x201c;The Premium Emanation&#x201d; (October 14, 2021)

- &#x1f527; *Change:* Bundle Java with LTeX LS; Java is not downloaded separately anymore and bundled Java is used if [`ltex.java.path`](../settings.html#ltexjavapath) is not set
- &#x1f5d1; *Removal:* Remove setting `ltex.java.forceTrySystemWide`
- &#x1f527; *Change:* Update LanguageTool to 5.5 (see [LT 5.5 release notes](https://github.com/languagetool-org/languagetool/blob/v5.5/languagetool-standalone/CHANGES.md#55-2021-10-02))
- &#x2728; *New:* Add support for automatic language detection via language short code `auto`; language variants like `en-US` are not detected, only generic languages like `en`; this will result in spelling errors not being reported &#x2014; [ltex-ls#103](https://github.com/valentjn/ltex-ls/issues/103)
- &#x2728; *New:* Provide ID of LanguageTool rule via diagnostics code, not as part of diagnostics message
- &#x2728; *New:* Link diagnostics to LanguageTool website with more information
- &#x2728; *New:* Add support for the `main` option of the babel package (LaTeX) &#x2014; [#391](https://github.com/valentjn/vscode-ltex/issues/391)
- &#x2728; *New:* Add setting `ltex.ltex-ls.languageToolOrgUsername` to set username on languagetool.org for Premium API access &#x2014; [#398](https://github.com/valentjn/vscode-ltex/issues/398)
- &#x2728; *New:* Add setting `ltex.ltex-ls.languageToolOrgApiKey` to set API key on languagetool.org for Premium API access &#x2014; [#398](https://github.com/valentjn/vscode-ltex/issues/398)
- &#x2728; *New:* Add support for [`ltex.dictionary`](../settings.html#ltexdictionary) when using a LanguageTool HTTP server
- &#x1f527; *Change:* Handle disabled rules ourselves to prevent reinitialization of LanguageTool when running the `Disable rule` quick fix &#x2014; [#390](https://github.com/valentjn/vscode-ltex/issues/390)
- &#x1f41b; *Bug fix:* Fix LanguageTool reinitialized when running the `Add '...' to dictionary` quick fix &#x2014; [#390](https://github.com/valentjn/vscode-ltex/issues/390)
- &#x1f41b; *Bug fix:* Fix wrong parsing of inline math formulas in Markdown when using dollar signs as delimiters and containing only one character (e.g., `$a$`)
- &#x1f41b; *Bug fix:* Fix used i18n keys removed in LTeX LS
- &#x1f41b; *Bug fix:* Fix fallback from German to English i18n in LTeX LS
- &#x2728; *New:* Add support for coc.nvim (Vim/Neovim) &#x2014; [ltex-ls#103](https://github.com/valentjn/ltex-ls/issues/103)
- &#x1f527; *Change:* Update bundled Java runtime to 11.0.12+7 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8269291?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.12))
- &#x1f5d1; *Removal:* Remove transition code for upgrading from LTeX 4.x
- &#x1f527; *Change:* Update LTeX LS to 14.0.0

## 11.0.0 &#x2014; &#x201c;The Kotlin Conundrum&#x201d; (August 11, 2021)

- &#x1f527; *Change:* Migrate LTeX LS from Java to Kotlin
- &#x2728; *New:* Add support for checking comments in many popular programming languages &#x2014; [#350](https://github.com/valentjn/vscode-ltex/issues/350)
- &#x2728; *New:* Add support for rule-dependent diagnostic severities in [`ltex.diagnosticSeverity`](../settings.html#ltexdiagnosticseverity) &#x2014; [ltex-ls#95](https://github.com/valentjn/ltex-ls/issues/95)
- &#x2728; *New:* Add support for vowel dummies in LaTeX (`"vowelDummy"` in [`ltex.latex.commands`](../settings.html#ltexlatexcommands)) and Markdown (`"vowelDummy"` in [`ltex.markdown.nodes`](../settings.html#ltexmarkdownnodes)) &#x2014; [#366](https://github.com/valentjn/vscode-ltex/issues/366)
- &#x2728; *New:* Add support for more LaTeX commands (`\mathop`, `\overline`, `\tilde`, `\alpha`, etc.) for automatic vowel detection in formulas in LaTeX &#x2014; [ltex-ls#92](https://github.com/valentjn/ltex-ls/issues/92), [Shuhao Cao (@scaomath)](https://github.com/scaomath)
- &#x2728; *New:* Add support for `\counterwithin`, `\counterwithout`, and `\numberwithin` in LaTeX &#x2014; [ltex-ls#87](https://github.com/valentjn/ltex-ls/issues/87), [Alexander Zeilmann (@AlexanderZeilmann)](https://github.com/AlexanderZeilmann)
- &#x2728; *New:* Add missing support for Argentine Spanish (`es-AR`)
- &#x1f41b; *Bug fix:* Don't ignore second argument of `\setkomavar` in LaTeX &#x2014; [#373](https://github.com/valentjn/vscode-ltex/issues/373)
- &#x1f5d1; *Removal:* Remove support for magic comments in XHTML
- &#x1f41b; *Bug fix:* Validate keys of [`ltex.dictionary`](../settings.html#ltexdictionary), [`ltex.disabledRules`](../settings.html#ltexdisabledrules), [`ltex.enabledRules`](../settings.html#ltexenabledrules), and [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives) &#x2014; [#381](https://github.com/valentjn/vscode-ltex/issues/381)
- &#x2728; *New:* Improve interaction with VS Code's UI-based settings editor
- &#x1f527; *Change:* Change format of changelog
- &#x1f527; *Change:* Update LTeX LS to 13.0.0

## 10.5.0 &#x2014; &#x201c;The XHTML Calculation&#x201d; (July 12, 2021)

- &#x1f527; *Change:* Update LanguageTool to 5.4 (see [LT 5.4 release notes](https://github.com/languagetool-org/languagetool/blob/v5.4/languagetool-standalone/CHANGES.md#54-2021-06-25))
- &#x2728; *New:* Add support for XHTML &#x2014; [#342](https://github.com/valentjn/vscode-ltex/issues/342)
- &#x1f41b; *Bug fix:* Fix markup before actual grammar/spelling errors included in errors &#x2014; [#349](https://github.com/valentjn/vscode-ltex/issues/349)
- &#x1f41b; *Bug fix:* Fix error when checking LaTeX documents ending with specific commands &#x2014; [#341](https://github.com/valentjn/vscode-ltex/issues/341)
- &#x2728; *New:* Fix name of Portuguese babel language names, add support for Brazilian Portuguese babel language names &#x2014; [ltex-ls#72](https://github.com/valentjn/ltex-ls/issues/72)
- &#x1f5d1; *Removal:* Remove unnecessary files from packaged extension (reduces size from 570 KB to 160 KB)
- &#x1f527; *Change:* Update LTeX LS to 12.3.0

## 10.4.0 &#x2014; &#x201c;The Walkthrough Implementation&#x201d; (June 12, 2021)

- &#x1f527; *Change:* Enable LTeX in untrusted workspaces (introduced in VS Code 1.57.0)
- &#x2728; *New:* Add walkthrough for VS Code's *Getting Started* page (introduced in VS Code 1.57.0)

## 10.3.0 &#x2014; &#x201c;The Orphan Disintegration&#x201d; (June 5, 2021)

- &#x1f527; *Change:* Enable LTeX in Jupyter notebooks in VS Code Insiders (as soon as the native notebooks are released by VS Code, this will automatically work in regular VS Code)
- &#x2728; *New:* Add support for `\setplength` (LaTeX)
- &#x1f41b; *Bug fix:* Fix LTeX LS not closed when VS Code or workspace is closed &#x2014; [#325](https://github.com/valentjn/vscode-ltex/issues/325)
- &#x1f527; *Change:* Update LTeX LS to 12.2.0

## 10.2.0 &#x2014; &#x201c;The Long Document Reverberation&#x201d; (May 1, 2021)

- &#x1f527; *Change:* Show `Use ...` quick fixes before other quick fixes &#x2014; [#297](https://github.com/valentjn/vscode-ltex/issues/297)
- &#x1f527; *Change:* Limit number of `Use ...` quick fixes to 5 &#x2014; [#297](https://github.com/valentjn/vscode-ltex/issues/297)
- &#x2728; *New:* Add checking status to output of [`LTeX: Show Status Information`](commands.html#ltex-show-status-information)
- &#x2728; *New:* Add support for `\phantom`, `\hphantom`, and `\vphantom` (LaTeX)
- &#x1f41b; *Bug fix:* Fix almost infinite loops when checking very long documents &#x2014; [#253](https://github.com/valentjn/vscode-ltex/issues/253)
- &#x1f41b; *Bug fix:* Fix wrong underlining of words starting with markup &#x2014; [ltex-ls#69](https://github.com/valentjn/ltex-ls/issues/69)
- &#x1f527; *Change:* Update bundled AdoptOpenJDK JRE to 11.0.11+9 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8264310?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.11%20ORDER%20BY%20created%20DESC))
- &#x1f527; *Change:* Update LTeX LS to 12.1.0

## 10.1.0 &#x2014; &#x201c;The Org Summation&#x201d; (April 18, 2021)

- &#x2728; *New:* Add support for Org &#x2014; [#277](https://github.com/valentjn/vscode-ltex/issues/277)
- &#x2728; *New:* Add basic support for reStructuredText &#x2014; [#32](https://github.com/valentjn/vscode-ltex/issues/32)
- &#x2728; *New:* Add [`LTeX: Reset and Restart`](commands.html#ltex-reset-and-restart) command to reset the extension and restart LTeX LS (equivalent to reloading the VS Code window)
- &#x1f41b; *Bug fix:* Fix `.Rnw` not recognized for R Sweave documents when running [`LTeX: Check All Documents in Workspace`](commands.html#ltex-check-all-documents-in-workspace)
- &#x1f41b; *Bug fix:* Fix inconsistent titles of German commands
- &#x1f41b; *Bug fix:* Hide internal commands in table of keyboard shortcuts to prevent confusion &#x2014; [#282](https://github.com/valentjn/vscode-ltex/issues/282)
- &#x1f527; *Change:* Engineering: A running instance of LTeX LS, if it has been started with `--server-type=tcpSocket`, will be chosen over starting a new instance; this enables simultaneous debugging of vscode-ltex and ltex-ls
- &#x1f527; *Change:* Update LTeX LS to 12.0.0

## 10.0.0 &#x2014; &#x201c;The Unicode Simulation&#x201d; (April 5, 2021)

- &#x1f527; *Change:* Update required version of VS Code (now 1.52.0 or newer)
- &#x1f527; *Change:* Update LanguageTool to 5.3 (see [LT 5.3 release notes](https://github.com/languagetool-org/languagetool/blob/v5.3/languagetool-standalone/CHANGES.md#53-2021-03-29))
- &#x2728; *New:* Add [`LTeX: Activate Extension`](commands.html#ltex-activate-extension) to activate the extension in case it has not been activated before
- &#x1f527; *Change:* Automatically activate extension if one of the [LTeX commands](https://valentjn.github.io/ltex/vscode-ltex/commands.html) is executed
- &#x2728; *New:* Enhance support of accents in LaTeX by using Unicode combining diacritical marks, normalized via [Unicode Normalization Form C](https://www.unicode.org/reports/tr15/tr15-50.html#Normalization_Forms_Table) &#x2014; [#269](https://github.com/valentjn/vscode-ltex/issues/269)
- &#x2728; *New:* Add support for many accents in LaTeX: double acute (e.g., `\H{O}`, &#x0150;), line below (e.g., `\b{h}`, &#x1e96;), dot below (e.g., `\d{A}`, &#x1ea0;), ogonek (e.g., `\k{A}`, &#x0104;), breve (e.g., `\u{A}`, &#x0102;), and caron (e.g., `\v{C}`, &#x010c;) &#x2014; [ltex-ls#56](https://github.com/valentjn/ltex-ls/issues/56), [ltex-ls#57](https://github.com/valentjn/ltex-ls/issues/57), [@ed359](https://github.com/ed359)
- &#x2728; *New:* Add support for special characters in LaTeX: `\L` (&#x0141;), `\SS` (&#x1e9e;), `\i` (&#x0131;), `\j` (&#x0237;), and `\l` (&#x0142;) &#x2014; [ltex-ls#56](https://github.com/valentjn/ltex-ls/issues/56), [ltex-ls#57](https://github.com/valentjn/ltex-ls/issues/57), [@ed359](https://github.com/ed359)
- &#x2728; *New:* Add `FR_SPELLING_RULE` as a rule for unknown words &#x2014; [ltex-ls#47](https://github.com/valentjn/ltex-ls/issues/47), [Nicolas Sicard (@biozic)](https://github.com/biozic)
- &#x1f527; *Change:* Use LaTeX parser for documents with code language ID `tex` &#x2014; [ltex-ls#53](https://github.com/valentjn/ltex-ls/issues/53), [ltex-ls#54](https://github.com/valentjn/ltex-ls/issues/54), [Lucas Alber (@LDAP)](https://github.com/LDAP)
- &#x1f527; *Change:* Change type of [`ltex.additionalRules.motherTongue`](../settings.html#ltexadditionalrulesmothertongue) to `enum` to clarify possible values &#x2014; [#260](https://github.com/valentjn/vscode-ltex/issues/260)
- &#x1f527; *Change:* Update LSP4J to 0.12.0
- &#x1f527; *Change:* Update LTeX LS to 11.0.0

## 9.0.0 &#x2014; &#x201c;The HTML Evaporation&#x201d; (February 12, 2021)

- &#x1f5d1; *Removal:* Remove support for settings that are deprecated since 8.0.0: `ltex.workspaceDictionary`, `ltex.workspaceFolderDictionary`, `ltex.workspaceDisabledRules`, `ltex.workspaceFolderDisabledRules`, `ltex.workspaceEnabledRules`, `ltex.workspaceFolderEnabledRules`, `ltex.ignoreInRuleSentence`, `ltex.commands.ignore`, `ltex.commands.dummy`, `ltex.environments.ignore`, `ltex.markdown.ignore`, and `ltex.markdown.dummy`
- &#x1f5d1; *Removal:* Remove support for values for [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) that are deprecated since 7.0.0 or 8.0.0: `"global"` (deprecated since 7.0.0), `"addToDictionary"`, `"disableRule"`, and `"ignoreRuleInSentence"`
- &#x2728; *New:* Add support for magic comments inside HTML comments in Markdown (`<!-- ltex: SETTINGS -->`)
- &#x1f527; *Change:* Check frame title in argument of LaTeX Beamer frames &#x2014; [#239](https://github.com/valentjn/vscode-ltex/issues/239)
- &#x2728; *New:* Add [`LTeX: Check Selection`](commands.html#ltex-check-selection) to check text in documents with unsupported code languages
- &#x1f41b; *Bug fix:* Fix comment sign before babel commands not recognized &#x2014; [#245](https://github.com/valentjn/vscode-ltex/issues/245)
- &#x1f41b; *Bug fix:* Fix removing items in settings with a hyphen prefix sometimes not working
- &#x1f41b; *Bug fix:* Fix space not added between two arguments of LaTeX commands
- &#x1f41b; *Bug fix:* Fix manually checking BibTeX documents not working
- &#x1f41b; *Bug fix:* Fix words in dictionary containing markup not recognized
- &#x1f527; *Change:* Update bundled AdoptOpenJDK JRE to 11.0.10+9 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8258701?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.10%20ORDER%20BY%20created%20DESC))
- &#x1f527; *Change:* Update LTeX LS to 10.0.0

## 8.4.0 &#x2014; &#x201c;The Math Optimization&#x201d; (January 29, 2021)

- &#x2728; *New:* Add support for Pandoc-style inline math (`$...$`) and display math (`$$...$$` with `$$` being at the beginning/end of a Markdown block) to Markdown parser &#x2014; [#210](https://github.com/valentjn/vscode-ltex/issues/210)
- &#x1f41b; *Bug fix:* Fix false positives for words added by `Add to dictionary` for Slovak rule IDs `MUZSKY_ROD_NEZIV_A`, `ZENSKY_ROD_A`, and `STREDNY_ROD_A` &#x2014; [#221](https://github.com/valentjn/vscode-ltex/issues/221)
- &#x1f41b; *Bug fix:* Fix BibTeX field `seealso` not ignored, ignore `category` and `parent` &#x2014; [#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x1f527; *Change:* Disable `UPPERCASE_SENTENCE_START` in BibTeX files &#x2014; [#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x1f527; *Change:* Move rule ID to the end of diagnostic messages as VS Code truncates the messages if the Problems panel is narrow &#x2014; [#233](https://github.com/valentjn/vscode-ltex/issues/233)
- &#x1f41b; *Bug fix:* Fix regression that messages of possible spelling mistakes are not prepended with the respective unknown words &#x2014; [#161](https://github.com/valentjn/vscode-ltex/issues/161)
- &#x1f41b; *Bug fix:* Fix crash when using `\begin` or `\end` without an argument &#x2014; [#236](https://github.com/valentjn/vscode-ltex/issues/236)
- &#x1f527; *Change:* Use Title Case for titles of commands
- &#x1f527; *Change:* Update LTeX LS to 9.2.0

## 8.3.0 &#x2014; &#x201c;The BibTeX Experimentation&#x201d; (January 24, 2021)

- &#x2728; *New:* Add support for BibTeX files (language code `bibtex`) &#x2014; [#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x2728; *New:* Add setting [`ltex.bibtex.fields`](../settings.html#ltexbibtexfields) to control which BibTeX fields should be checked
- &#x2728; *New:* Add support for [GitLab Flavored Markdown](https://gitlab.com/gitlab-org/gitlab/blob/master/doc/user/markdown.md), especially inline math (e.g., ``$`E = mc^2`$``) &#x2014; [#210](https://github.com/valentjn/vscode-ltex/issues/210)
- &#x2728; *New:* Add support for Markdown tables as in [GitHub Flavored Markdown](https://github.github.com/gfm/#tables-extension-) &#x2014; [#218](https://github.com/valentjn/vscode-ltex/issues/218)
- &#x2728; *New:* Add support for more commands of the `glossaries` LaTeX package
- &#x1f527; *Change:* Enable `Add to dictionary` quick fix for Slovak rule IDs `MUZSKY_ROD_NEZIV_A`, `ZENSKY_ROD_A`, and `STREDNY_ROD_A` &#x2014; [#221](https://github.com/valentjn/vscode-ltex/issues/221)
- &#x1f5d1; *Removal:* Remove superfluous spaces in messages of diagnostics
- &#x1f41b; *Bug fix:* Fix LTeX LS not starting if Java version string does not contain a minor version (e.g., `"16"`) &#x2014; [#224](https://github.com/valentjn/vscode-ltex/issues/224)
- &#x1f41b; *Bug fix:* Fix handling of `\r\n` (Windows) line terminators in Markdown
- &#x1f527; *Change:* Use Flexmark's YAML Front Matter extension to ignore YAML front matter in Markdown instead of own handling
- &#x1f41b; *Bug fix:* Fix documentation on the number of backslashes for [`ltex.latex.commands`](../settings.html#ltexlatexcommands) &#x2014; [#232](https://github.com/valentjn/vscode-ltex/issues/232)
- &#x1f527; *Change:* Print Flexmark AST of Markdown documents to log when [`ltex.ltex-ls.logLevel`](../settings.html#ltexltex-lsloglevel) is `"finest"`
- &#x1f527; *Change:* Update LTeX LS to 9.1.0

## 8.2.1 &#x2014; &#x201c;The Accent Ramification&#x201d; (January 13, 2021)

- &#x1f527; *Change:* Ignore `\pgfmathsetmacro`, `\setmainfont`, and `\theoremstyle`
- &#x1f41b; *Bug fix:* Fix accent commands such as `\O` in math mode resulting in diagnostics &#x2014; [#216](https://github.com/valentjn/vscode-ltex/issues/216)
- &#x1f527; *Change:* Update issue labels when reporting bugs or requesting features
- &#x1f527; *Change:* Update LTeX LS to 9.0.1

## 8.2.0 &#x2014; &#x201c;The Separation Displacement&#x201d; (January 3, 2021)

- &#x1f527; *Change:* Make versioning of LTeX LS independent of vscode-ltex; see the changelog of vscode-ltex to find out which version of LTeX LS a particular version of vscode-ltex uses
- &#x1f527; *Change:* Update LanguageTool to 5.2 (see [LT 5.2 release notes](https://github.com/languagetool-org/languagetool/blob/v5.2/languagetool-standalone/CHANGES.md#52-released-2020-12-29))
- &#x2728; *New:* Add [`ltex.additionalRules.enablePickyRules`](../settings.html#ltexadditionalrulesenablepickyrules) to still be able to detect false friends after the update of LanguageTool (default: `false`)
- &#x1f527; *Change:* Only check file types for which LTeX has been enabled when running [`LTeX: Check All Documents in Workspace`](commands.html#ltex-check-all-documents-in-workspace) &#x2014; [#183](https://github.com/valentjn/vscode-ltex/issues/183)
- &#x1f41b; *Bug fix:* Fix scope of [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives) (was application-scoped, is now resource-scoped)
- &#x1f527; *Change:* Replace `\dots` with Unicode ellipsis `&#x2026;` instead of three dots `...` to fix some false positives
- &#x1f527; *Change:* Update LTeX LS to 9.0.0

## 8.1.1 &#x2014; &#x201c;The Action Postulate&#x201d; (November 24, 2020)

- &#x1f527; *Change:* Migrate from Travis CI to GitHub Actions
- &#x1f527; *Change:* Update LTeX LS to 8.1.1

## 8.1.0 &#x2014; &#x201c;The Prepending Annihilation&#x201d; (November 15, 2020)

- &#x1f527; *Change:* Prepend messages of possible spelling mistakes with the respective unknown words &#x2014; [#161](https://github.com/valentjn/vscode-ltex/issues/161)
- &#x2728; *New:* Add support for optional arguments of `\newtheorem`
- &#x1f41b; *Bug fix:* Fix wrong position of diagnostics when using a recognized LaTeX command with a non-recognized set of arguments due to an infinite loop &#x2014; [#167](https://github.com/valentjn/vscode-ltex/issues/167)
- &#x1f527; *Change:* Avoid misleading popup prompting to install Java on Mac, use `ltex.java.forceTrySystemWide` to force trying a system-wide Java installation &#x2014; [#162](https://github.com/valentjn/vscode-ltex/issues/162)
- &#x1f527; *Change:* Update bundled AdoptOpenJDK JRE to 11.0.9+11 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8253813?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.9%20ORDER%20BY%20created%20DESC))
- &#x1f527; *Change:* Update LSP4J to 0.10.0
- &#x1f527; *Change:* Update LTeX LS to 8.1.0

## 8.0.0 &#x2014; &#x201c;The Setting Transformation&#x201d; (November 1, 2020)

- &#x1f527; *Change:* Upgrade from Java 8 to Java 11 (see [announcement](https://valentjn.github.io/ltex/old/deprecation-of-java-8.html)) &#x2014; [#39](https://github.com/valentjn/vscode-ltex/issues/39)
- &#x2728; *New:* Add workaround to eliminate the need for workspace-specific setting names; [`ltex.dictionary`](../settings.html#ltexdictionary), [`ltex.disabledRules`](../settings.html#ltexdisabledrules), and [`ltex.enabledRules`](../settings.html#ltexenabledrules) can now be used in multiple setting scopes (user settings, workspace settings, and workspace folder settings) at the same time without overriding each other; instead, the settings of the different scopes will be properly merged (see [documentation](https://valentjn.github.io/ltex/vscode-ltex/setting-scopes-files.html#multi-scope-settings))
- &#x1f527; *Change:* Rename `ltex.workspaceDictionary`, `ltex.workspaceFolderDictionary` &#x2192; [`ltex.dictionary`](../settings.html#ltexdictionary)
- &#x1f527; *Change:* Rename `ltex.workspaceDisabledRules`, `ltex.workspaceFolderDisabledRules` &#x2192; [`ltex.disabledRules`](../settings.html#ltexdisabledrules)
- &#x1f527; *Change:* Rename `ltex.workspaceEnabledRules`, `ltex.workspaceFolderEnabledRules` &#x2192; [`ltex.enabledRules`](../settings.html#ltexenabledrules)
- &#x1f527; *Change:* Rename `ltex.ignoreInRuleSentence` &#x2192; [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives)
- &#x1f527; *Change:* Rename `ltex.commands.ignore`, `ltex.commands.dummy` &#x2192; [`ltex.latex.commands`](../settings.html#ltexlatexcommands)
- &#x1f527; *Change:* Rename `ltex.environments.ignore` &#x2192; [`ltex.latex.environments`](../settings.html#ltexlatexenvironments)
- &#x1f527; *Change:* Rename `ltex.markdown.ignore`, `ltex.markdown.dummy` &#x2192; [`ltex.markdown.nodes`](../settings.html#ltexmarkdownnodes)
- &#x1f527; *Change:* Change format of [`ltex.latex.commands`](../settings.html#ltexlatexcommands), [`ltex.latex.environments`](../settings.html#ltexlatexenvironments), [`ltex.markdown.nodes`](../settings.html#ltexmarkdownnodes) to be objects (with key = command and value = action, e.g., `"ignore"`, `"dummy"`, etc.) instead of arrays
- &#x1f527; *Change:* Rename `addToDictionary` &#x2192; `dictionary` in [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget)
- &#x1f527; *Change:* Rename `disableRule` &#x2192; `disabledRules` in [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget)
- &#x1f527; *Change:* Rename `ignoreRuleInSentence` &#x2192; `hiddenFalsePositives` in [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget)
- &#x2728; *New:* Add `userExternalFile`, `workspaceExternalFile`, and `workspaceFolderExternalFile` enumeration values to [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget), which enables saving settings to external files (see [documentation](https://valentjn.github.io/ltex/vscode-ltex/setting-scopes-files.html#external-setting-files)) &#x2014; [#144](https://github.com/valentjn/vscode-ltex/issues/144), [#145](https://github.com/valentjn/vscode-ltex/issues/145)
- &#x1f527; *Change:* Change default of [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) for `dictionary`, `disabledRules`, and `hiddenFalsePositives` to `workspaceFolderExternalFile`
- &#x2728; *New:* Add [`ltex.statusBarItem`](../settings.html#ltexstatusbaritem) to permanently display LTeX's status in the status bar &#x2014; [#141](https://github.com/valentjn/vscode-ltex/issues/141)
- &#x2728; *New:* Add [`ltex.checkFrequency`](../settings.html#ltexcheckfrequency) to control when LTeX checks documents &#x2014; [#142](https://github.com/valentjn/vscode-ltex/issues/142)
- &#x2728; *New:* Add [`LTeX: Show Status Information`](commands.html#ltex-show-status-information) command to show information about the status of LTeX
- &#x2728; *New:* Add support for `\usepackage[LANGUAGE]{babel}` if in the same file as the text to be checked &#x2014; [#140](https://github.com/valentjn/vscode-ltex/issues/140)
- &#x2728; *New:* Add support for more BibLaTeX commands such as `\autocite`, `\citeauthor`, etc. &#x2014; [#143](https://github.com/valentjn/vscode-ltex/issues/143)
- &#x2728; *New:* Add support for overriding hard-coded command signatures &#x2014; [ltex-ls#27](https://github.com/valentjn/ltex-ls/issues/27)
- &#x2728; *New:* Add verification for downloaded files (LTeX LS and Java)
- &#x1f527; *Change:* Move handling of external setting files from ltex-ls to vscode-ltex
- &#x1f527; *Change:* Better resolve relative paths to external setting files, either with respect to the `.vscode` directory of the workspace folder if any, the `.vscode` directory of the workspace if any, or the global storage directory of the extension (see [documentation](https://valentjn.github.io/ltex/vscode-ltex/setting-scopes-files.html#external-setting-files)) &#x2014; [#146](https://github.com/valentjn/vscode-ltex/issues/146)
- &#x1f527; *Change:* Slightly change logo
- &#x1f527; *Change:* Improve logging in case of problems with the initialization of ltex-ls
- &#x1f527; *Change:* Increase duration before sentences expire in the result cache to 60 minutes
- &#x1f41b; *Bug fix:* Fix many settings changes cleared sentence cache, which led to performance issues, e.g., changing the [`ltex.enabled`](../settings.html#ltexenabled) setting via magic comments &#x2014; [#134](https://github.com/valentjn/vscode-ltex/issues/134)
- &#x1f5d1; *Removal:* Remove dependency on `org.apache.httpcomponents:httpclient` by using the HTTP client that comes with Java 11 when connecting to an HTTP LanguageTool server
- &#x1f527; *Change:* Update LTeX LS to 8.0.0

## 7.3.1 &#x2014; &#x201c;The Delay Correlation&#x201d; (October 12, 2020)

- &#x1f41b; *Bug fix:* Fix delayed publication of diagnostics by adding workaround to guess the caret position
- &#x1f41b; *Bug fix:* Fix recheck being triggered when generating list of quick fixes; this should improve speed
- &#x1f41b; *Bug fix:* Fix comment in readme
- &#x1f527; *Change:* Update LTeX LS to 7.3.1

## 7.3.0 &#x2014; &#x201c;The Debugging Formulation&#x201d; (October 10, 2020)

- &#x2728; *New:* Add support for `\ell` as well as `\mathcal`, `\mathfrak`, etc. to vowel detection &#x2014; [#131](https://github.com/valentjn/vscode-ltex/issues/131)
- &#x2728; *New:* Add setting [`ltex.ltex-ls.logLevel`](../settings.html#ltexltex-lsloglevel) to control the verbosity of the server log of LTeX LS
- &#x2728; *New:* Add command [`ltex.requestFeature`](commands.html#ltex-request-feature-for-ltex) to quickly request a new feature in LTeX via VS Code
- &#x2728; *New:* Add button to set [`ltex.trace.server`](../settings.html#ltextraceserver) to `"verbose"` when reporting a bug
- &#x1f41b; *Bug fix:* Fix diagnostics sometimes not lined up with the text with switching back from incremental to full document updates; unfortunately, this disables the delayed publication of diagnostics at the caret position
- &#x1f527; *Change:* Restructure and simplify internal quick fix and command structure, removing the need for pseudo-telemetry notifications
- &#x1f527; *Change:* Update LTeX LS to 7.3.0

## 7.2.0 &#x2014; &#x201c;The LanguageTool Acquisition&#x201d; (September 27, 2020)

- &#x1f527; *Change:* Update LanguageTool to 5.1 (see [LT 5.1 release notes](https://github.com/languagetool-org/languagetool/blob/v5.1/languagetool-standalone/CHANGES.md#51-released-2020-09-25))
- &#x2728; *New:* Add support for HTML entities such as `&auml;` and `&copy;` in Markdown
- &#x1f41b; *Bug fix:* Fix missing tilde expansion for external dictionary files
- &#x1f527; *Change:* Improve logging of LTeX LS
- &#x1f527; *Change:* Update LTeX LS to 7.2.0

## 7.1.2 &#x2014; &#x201c;The Magic Configuration&#x201d; (September 22, 2020)

- &#x1f41b; *Bug fix:* Fix performance issue with multiple languages in one document via magic comments due to LanguageTool being reinitialized on each keystroke &#x2014; [#124](https://github.com/valentjn/vscode-ltex/issues/124)
- &#x1f527; *Change:* Update LTeX LS to 7.1.2

## 7.1.1 &#x2014; &#x201c;The Relative Malfunction&#x201d; (September 20, 2020)

- &#x1f41b; *Bug fix:* Fix `NullPointerException` when supplying relative paths to external dictionary files
- &#x1f41b; *Bug fix:* Fix German log messages
- &#x1f527; *Change:* Update LTeX LS to 7.1.1

## 7.1.0 &#x2014; &#x201c;The External Accumulation&#x201d; (September 20, 2020)

- &#x2728; *New:* Add support for external dictionary files &#x2014; [#118](https://github.com/valentjn/vscode-ltex/issues/118)
- &#x2728; *New:* Add support for enabling/disabling LTeX only for specific file types via [`ltex.enabled`](../settings.html#ltexenabled) &#x2014; [#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `acro` commands such as `\DeclareAcronym` and `\ac` &#x2014; [#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `\addcontentsline` &#x2014; [#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `\printbibliography` and `\printglossary` without argument
- &#x1f527; *Change:* Ignore parenthesis arguments of `textblock`s &#x2014; [#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x1f41b; *Bug fix:* Fix optional argument of heading commands such as `\section` parsed incorrectly &#x2014; [#123](https://github.com/valentjn/vscode-ltex/issues/123)
- &#x1f527; *Change:* Include stack traces when logging exceptions
- &#x1f41b; *Bug fix:* Fix some links (bug reporter, offline installation, readme)
- &#x1f527; *Change:* Update LTeX LS to 7.1.0

## 7.0.0 &#x2014; &#x201c;The Workspace Solution&#x201d; (September 13, 2020)

- &#x1f527; *Change:* Change scope of [`ltex.dictionary`](../settings.html#ltexdictionary), [`ltex.disabledRules`](../settings.html#ltexdisabledrules), and [`ltex.enabledRules`](../settings.html#ltexenabledrules) to `application`; these are now user-specific settings that can only be configured in user settings
- &#x2728; *New:* Add settings `ltex.workspaceDictionary`, `ltex.workspaceDisabledRules`, and `ltex.workspaceEnabledRules` with `window` scope to amend the corresponding user-specific settings; these are workspace-specific settings that should be configured in workspace settings
- &#x2728; *New:* Add settings `ltex.workspaceFolderDictionary`, `ltex.workspaceFolderDisabledRules`, and `ltex.workspaceFolderEnabledRules` with `resource` scope to amend the corresponding user-specific and workspace-specific settings; these are workspace-folder-specific settings that should be configured in workspace folder settings
- &#x1f527; *Change:* Change default of [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) for `addToDictionary` to `workspaceFolder`, i.e., by default, words will now be added to the workspace-folder-specific settings instead of the user-specific settings
- &#x2728; *New:* Rename `"global"` value for [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) to `"user"` (`"global"` is still supported, but deprecated)
- &#x1f5d1; *Removal:* Remove deprecated settings `ltex.javaHome`, `ltex.performance.initialJavaHeapSize`, `ltex.performance.maximumJavaHeapSize`, `ltex.performance.sentenceCacheSize`, `ltex.*.dictionary`, `ltex.*.enabledRules`, and `ltex.*.disabledRules` (deprecation since 5.0.0)
- &#x1f527; *Change:* Update LanguageTool to 5.0.2 (see [LT 5.0.2 release notes](https://github.com/languagetool-org/languagetool/blob/v5.0.2/languagetool-standalone/CHANGES.md#502-2020-08-28))
- &#x1f41b; *Bug fix:* Fix skipping of YAML front matter &#x2014; [#104](https://github.com/valentjn/vscode-ltex/issues/104)
- &#x1f527; *Change:* Update LTeX LS to 7.0.0

## 6.3.0 &#x2014; &#x201c;The Vowel Extraction&#x201d; (August 22, 2020)

- &#x2728; *New:* Add support for `an` article when before a formula starting with a vowel (e.g., `an $n$-dimensional problem`) &#x2014; [#92](https://github.com/valentjn/vscode-ltex/issues/92)
- &#x2728; *New:* Add support for `~/` and `~\` in settings &#x2014; [#99](https://github.com/valentjn/vscode-ltex/issues/99)
- &#x1f41b; *Bug fix:* Fix links to documentation in various places (readme, changelog, error messages, etc.)
- &#x1f527; *Change:* Update LTeX LS to 6.3.0

## 6.2.0 &#x2014; &#x201c;The Command Isotope&#x201d; (August 7, 2020)

- &#x2728; *New:* Add commands [`LTeX: Check Current Document`](commands.html#ltex-check-current-document) and [`LTeX: Check All Documents in Workspace`](commands.html#ltex-check-all-documents-in-workspace) &#x2014; [#84](https://github.com/valentjn/vscode-ltex/issues/84)
- &#x2728; *New:* Add commands [`LTeX: Clear Diagnostics in Current Document`](commands.html#ltex-clear-diagnostics-in-current-document) and [`LTeX: Clear All Diagnostics`](commands.html#ltex-clear-all-diagnostics)
- &#x2728; *New:* Add setting [`ltex.clearDiagnosticsWhenClosingFile`](../settings.html#ltexcleardiagnosticswhenclosingfile)
- &#x1f527; *Change:* Skip front matter in Markdown
- &#x1f527; *Change:* Ignore more LaTeX preamble commands (e.g., `\automark`, `\color`, `\DeclareSIUnit`, `\directlua`, `\setuptoc`)
- &#x2728; *New:* Add support for German babel hyphenation commands `"-`, `""`, `"|`, `"=`, `"~`
- &#x1f527; *Change:* Use non-breaking space for `~`
- &#x1f527; *Change:* Update LTeX LS to 6.2.0

## 6.1.1 &#x2014; &#x201c;The Space Saturation&#x201d; (July 26, 2020)

- &#x1f41b; *Bug fix:* Fix another problem with spaces in paths when using LTeX LS on Windows &#x2014; [#80](https://github.com/valentjn/vscode-ltex/issues/80)
- &#x1f527; *Change:* Update LTeX LS to 6.1.1

## 6.1.0 &#x2014; &#x201c;The babel Momentum&#x201d; (July 26, 2020)

- &#x2728; *New:* Download Java 11 if only Java 8 is installed; LTeX support for Java 8 will end on November 1, 2020 (see [documentation](https://valentjn.github.io/ltex/old/deprecation-of-java-8.html)) &#x2014; [#39](https://github.com/valentjn/vscode-ltex/issues/39)
- &#x2728; *New:* Add support for babel commands (see [documentation](https://valentjn.github.io/ltex/advanced-usage.html#multilingual-latex-documents-with-the-babel-package)) &#x2014; [#81](https://github.com/valentjn/vscode-ltex/issues/81)
- &#x1f41b; *Bug fix:* Fix problems with spaces in paths when using LTeX LS on Windows &#x2014; [#80](https://github.com/valentjn/vscode-ltex/issues/80)
- &#x1f527; *Change:* Update bundled AdoptOpenJDK JRE to 11.0.8+10 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8253009?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.8%20ORDER%20BY%20created%20DESC))
- &#x1f527; *Change:* Update some NPM dependencies
- &#x1f527; *Change:* Update LTeX LS to 6.1.0

## 6.0.2 &#x2014; &#x201c;The Startup Congruence&#x201d; (July 11, 2020)

- &#x1f527; *Change:* Make Windows startup script of LTeX LS (`ltex-ls.bat`) honor `JAVA_HOME` &#x2014; [#75](https://github.com/valentjn/vscode-ltex/issues/75)
- &#x1f527; *Change:* Relicense vscode-ltex under the Mozilla Public License Version 2.0
- &#x1f527; *Change:* Update some NPM dependencies
- &#x1f527; *Change:* Update LTeX LS to 6.0.2

## 6.0.1 &#x2014; &#x201c;The Freeze Paradox&#x201d; (July 2, 2020)

- &#x1f41b; *Bug fix:* Fix freezes when checking German text by working around [languagetool-org/languagetool#3181](https://github.com/languagetool-org/languagetool/issues/3181) introduced by LanguageTool 5.0 &#x2014; [#68](https://github.com/valentjn/vscode-ltex/issues/68)
- &#x1f527; *Change:* Update LTeX LS to 6.0.1

## 6.0.0 &#x2014; &#x201c;The Internationalization Proposition&#x201d; (June 28, 2020)

- &#x1f527; *Change:* Update LanguageTool to 5.0 (see [LT 5.0 release notes](https://github.com/languagetool-org/languagetool/blob/v5.0/languagetool-standalone/CHANGES.md#50-2020-06-27))
- &#x2728; *New:* Add support for internationalized user interface of LTeX
- &#x2728; *New:* Add German translations for user interface of LTeX
- &#x1f527; *Change:* Delay diagnostics at the current caret position (e.g., incomplete word or sentence) until the user has finished typing &#x2014; [#46](https://github.com/valentjn/vscode-ltex/issues/46)
- &#x2728; *New:* Add `enabled` to magic comments &#x2014; [#67](https://github.com/valentjn/vscode-ltex/issues/67)
- &#x2728; *New:* Add command [`LTeX: Report Bug in LTeX`](commands.html#ltex-report-bug-in-ltex) for reporting LTeX bugs from within VS Code
- &#x1f41b; *Bug fix:* Fix `\todo` couldn't be ignored &#x2014; [#63](https://github.com/valentjn/vscode-ltex/issues/63)
- &#x1f41b; *Bug fix:* Fix wrong language-dependent settings used for magic comments
- &#x1f41b; *Bug fix:* Fix add to dictionary and disable rule quick fixes using wrong language when used with magic comments
- &#x1f41b; *Bug fix:* Fix deprecation message for `ltex.performance.maximumJavaHeapSize` not shown
- &#x1f41b; *Bug fix:* Improve code quality of LTeX LS by fixing hundreds of Checkstyle, SpotBugs, and Checker Framework warnings
- &#x1f527; *Change:* Migrate LTeX LS from Gradle to Maven
- &#x1f527; *Change:* Update NPM dependencies
- &#x1f527; *Change:* Update Maven dependencies
- &#x1f527; *Change:* Update LTeX LS to 6.0.0

## 5.0.2 &#x2014; &#x201c;The Disabling Submergence&#x201d; (June 18, 2020)

- &#x1f41b; *Bug fix:* Fix `Disable rule` quick fix using wrong setting structure &#x2014; [#61](https://github.com/valentjn/vscode-ltex/issues/61)

## 5.0.1 &#x2014; &#x201c;The Acceptance Incursion&#x201d; (June 7, 2020)

- &#x1f41b; *Bug fix:* Fix `Value is not accepted` warning when using [`ltex.disabledRules`](../settings.html#ltexdisabledrules) or [`ltex.enabledRules`](../settings.html#ltexenabledrules) &#x2014; [#44](https://github.com/valentjn/vscode-ltex/issues/44)
- &#x1f527; *Change:* Change badges in readme

## 5.0.0 &#x2014; &#x201c;The Rewrite Materialization&#x201d; (June 1, 2020)

- &#x2728; *New:* Download LTeX LS on demand with all languages already included; this removes the need for language support extensions &#x2014; [#6](https://github.com/valentjn/vscode-ltex/issues/6)
- &#x1f527; *Change:* Download Java distribution on demand if no suitable Java installation has been found &#x2014; [#5](https://github.com/valentjn/vscode-ltex/issues/5)
- &#x1f527; *Change:* Adhere to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). This means that the version of LTeX is not tied to the version of LanguageTool anymore, as the version of LanguageTool is not a semantic version. LTeX 5.0.0 uses LanguageTool 4.9.
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.dictionary` &#x2192; [`ltex.dictionary`](../settings.html#ltexdictionary) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.disabledRules` &#x2192; [`ltex.disabledRules`](../settings.html#ltexdisabledrules) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.enabledRules` &#x2192; [`ltex.enabledRules`](../settings.html#ltexenabledrules) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.javaHome` &#x2192; [`ltex.java.path`](../settings.html#ltexjavapath)
- &#x1f527; *Change:* Rename `ltex.performance.initialJavaHeapSize` &#x2192; [`ltex.java.initialHeapSize`](../settings.html#ltexjavainitialheapsize)
- &#x1f527; *Change:* Rename `ltex.performance.maximumJavaHeapSize` &#x2192; [`ltex.java.maximumHeapSize`](../settings.html#ltexjavamaximumheapsize)
- &#x1f527; *Change:* Rename `ltex.performance.sentenceCacheSize` &#x2192; [`ltex.sentenceCacheSize`](../settings.html#ltexsentencecachesize)
- &#x2728; *New:* Add support for external LanguageTool HTTP servers &#x2014; [#36](https://github.com/valentjn/vscode-ltex/issues/36)
- &#x2728; *New:* Add support for magic comments, enables changing the language in the middle of documents &#x2014; [#21](https://github.com/valentjn/vscode-ltex/issues/21)
- &#x1f41b; *Bug fix:* Check `\footnote` and `\todo` contents separately, preventing &#x201c;double period&#x201d; warnings &#x2014; [#42](https://github.com/valentjn/vscode-ltex/issues/42)
- &#x2728; *New:* Add support for more BibLaTeX citation commands, add support for plural dummies, add support for `\eg`, `\egc`, `\ie`, `\iec` &#x2014; [#43](https://github.com/valentjn/vscode-ltex/issues/43)
- &#x2728; *New:* Add visual feedback in status bar during startup and checks that take a long time
- &#x1f5d1; *Removal:* Remove `null` types and default values from settings, use empty string/array/object instead &#x2014; [#41](https://github.com/valentjn/vscode-ltex/issues/41)
- &#x1f527; *Change:* Use proper server/client model for language server/client
- &#x1f527; *Change:* Make documentation more extensive, put it on own [website](https://valentjn.github.io/ltex)
- &#x1f527; *Change:* Update LTeX LS to 5.0.0

## 4.9.3 &#x2014; &#x201c;The Java Collapse&#x201d; (May 7, 2020)

- &#x1f527; *Change:* Revert to Java 8
- &#x1f5d1; *Removal:* Remove support for external LanguageTool HTTP servers
- &#x1f527; *Change:* Update LTeX LS to 4.9.3

## 4.9.2 &#x2014; &#x201c;The Server Renormalization&#x201d; (May 6, 2020)

- &#x1f527; *Change:* Update required version of Java (now 11 or newer)
- &#x2728; *New:* Add support for external LanguageTool HTTP servers &#x2014; [#36](https://github.com/valentjn/vscode-ltex/issues/36)
- &#x2728; *New:* Add support for `\autoref`, `\pageref`, `\autopageref` &#x2014; [#37](https://github.com/valentjn/vscode-ltex/issues/37)
- &#x1f527; *Change:* Update LTeX LS to 4.9.2

## 4.9.1 &#x2014; &#x201c;The Sentence Cache Acceleration&#x201d; (May 1, 2020)

- &#x1f41b; *Bug fix:* Fix sentence cache was invalidated when a single ignore sentence rule was present &#x2014; [#29](https://github.com/valentjn/vscode-ltex/issues/29)
- &#x1f527; *Change:* Use thin non-breaking space for `\,` &#x2014; [#35](https://github.com/valentjn/vscode-ltex/issues/35)
- &#x1f527; *Change:* Update LTeX LS to 4.9.1

## 4.9.0 &#x2014; &#x201c;The Update Alternative&#x201d; (March 28, 2020)

- &#x1f527; *Change:* Update LanguageTool to 4.9 (see [LT 4.9 release notes](https://github.com/languagetool-org/languagetool/blob/v4.9/languagetool-standalone/CHANGES.md#49-2020-03-24))
- &#x1f527; *Change:* Update other Java dependencies
- &#x1f527; *Change:* Update NPM dependencies
- &#x1f527; *Change:* Update required version of VS Code (now 1.39.0 or newer)
- &#x1f527; *Change:* Reduce file size of extension (omitting unneeded dependencies)
- &#x2728; *New:* Add usage instructions to readme
- &#x1f527; *Change:* Update LTeX LS to 4.9.0

## 4.7.10 &#x2014; &#x201c;The French Capacitance&#x201d; (March 12, 2020)

- &#x1f41b; *Bug fix:* Fix spelling errors for French dummies &#x2014; [#27](https://github.com/valentjn/vscode-ltex/issues/27)
- &#x1f41b; *Bug fix:* Fix `\dots` in math mode being interpreted as `...`
- &#x1f527; *Change:* Minor changes in readme, changelog, and `package.json`
- &#x1f527; *Change:* Update LTeX LS to 4.7.10

## 4.7.9 &#x2014; &#x201c;The Markdown Resonance&#x201d; (February 29, 2020)

- &#x1f527; *Change:* Update Markdown parser Flexmark to 0.60.2; this increases the speed of parsing Markdown
- &#x2728; *New:* Add possibility to ignore Markdown elements or replace them by dummy words via `ltex.markdown.ignore` and `ltex.markdown.dummy` &#x2014; [#26](https://github.com/valentjn/vscode-ltex/issues/26)
- &#x1f527; *Change:* Ignore Markdown code blocks by default
- &#x1f527; *Change:* Replace auto-links and inline Markdown code with dummy words by default
- &#x1f41b; *Bug fix:* Fix match positions were sometimes off by one, especially in Markdown documents
- &#x1f527; *Change:* Rewrite `MarkdownAnnotatedTextBuilder`
- &#x1f527; *Change:* Update LTeX LS to 4.7.9

## 4.7.8 &#x2014; &#x201c;The Multi-Diagnostic Equivalency&#x201d; (February 16, 2020)

- &#x2728; *New:* Add support for R Sweave `.rnw` files &#x2014; [#22](https://github.com/valentjn/vscode-ltex/issues/22)
- &#x1f527; *Change:* Enable fixing multiple diagnostics at once &#x2014; [#23](https://github.com/valentjn/vscode-ltex/issues/23)
- &#x2728; *New:* Add `ltex.javaHome` setting to control the `JAVA_HOME` environment variable &#x2014; [#24](https://github.com/valentjn/vscode-ltex/issues/24), [@mpolitze](https://github.com/mpolitze)
- &#x2728; *New:* Add support for `\euro` &#x2014; [#25](https://github.com/valentjn/vscode-ltex/issues/25)
- &#x1f527; *Change:* Minor changes in readme
- &#x1f527; *Change:* Update LTeX LS to 4.7.8

## 4.7.7 &#x2014; &#x201c;The Preview Perturbation&#x201d; (November 23, 2019)

- &#x1f5d1; *Removal:* Remove preview status from extension
- &#x1f527; *Change:* Update LTeX LS to 4.7.7

## 4.7.6 &#x2014; &#x201c;The Java Thermalization&#x201d; (November 10, 2019)

- &#x2728; *New:* Add `ltex.performance` settings to give users more control over Java's RAM usage
- &#x1f527; *Change:* Change default initial Java heap size to 64 MB
- &#x1f527; *Change:* Change default maximum Java heap size to 512 MB
- &#x1f527; *Change:* Change default sentence cache size from 10000 to 2000 sentences
- &#x1f527; *Change:* Rename logs, enable logging of client messages even if no folder is open
- &#x2728; *New:* Add more examples to readme
- &#x1f527; *Change:* Update LTeX LS to 4.7.6

## 4.7.5 &#x2014; &#x201c;The Listing Collapse&#x201d; (October 22, 2019)

- &#x1f527; *Change:* Enable ignoring environments such as `lstlisting` and `verbatim`
- &#x2728; *New:* Add `ltex.environments.ignore` setting for defining own environments to ignore
- &#x1f527; *Change:* Update LTeX LS to 4.7.5

## 4.7.4 &#x2014; &#x201c;The Disabling Allocation&#x201d; (October 15, 2019)

- &#x2728; *New:* Add `disabledRules` and `enabledRules` settings (requires update of language extensions)
- &#x2728; *New:* Add `disable rule` quick fix
- &#x1f41b; *Bug fix:* Fix a bug where the `codeAction` request gets stuck in infinite loop
- &#x1f41b; *Bug fix:* Fix another `NullPointerException` for word2vec
- &#x1f527; *Change:* Update LTeX LS to 4.7.4

## 4.7.3 &#x2014; &#x201c;The word2vec Erosion&#x201d; (October 7, 2019)

- &#x1f41b; *Bug fix:* Fix null pointer error for word2vec quick fixes &#x2014; [#12](https://github.com/valentjn/vscode-ltex/issues/12)
- &#x1f527; *Change:* Update LTeX LS to 4.7.3

## 4.7.2 &#x2014; &#x201c;The Message Dissection&#x201d; (October 2, 2019)

- &#x2728; *New:* Add missing error message if legacy false friends could not be loaded
- &#x1f527; *Change:* Update LTeX LS to 4.7.2

## 4.7.1 &#x2014; &#x201c;The Mother Tongue Factor&#x201d; (October 2, 2019)

- &#x2728; *New:* Add [`ltex.additionalRules.motherTongue`](../settings.html#ltexadditionalrulesmothertongue) setting to enable detection of false friends &#x2014; [#11](https://github.com/valentjn/vscode-ltex/issues/11)
- &#x1f527; *Change:* Change defaults for `ltex.additionalRules` settings from `""` to `null`
- &#x1f527; *Change:* Update LTeX LS to 4.7.1

## 4.7.0 &#x2014; &#x201c;The Multi-Root Observation&#x201d; (October 1, 2019)

- &#x1f527; *Change:* Update LanguageTool to 4.7 (see [LT 4.7 release notes](https://github.com/languagetool-org/languagetool/blob/v4.7/languagetool-standalone/CHANGES.md#47-2019-09-28))
- &#x2728; *New:* Support multi-root workspaces, all configuration settings except [`ltex.enabled`](../settings.html#ltexenabled) are now resource-specific &#x2014; [#7](https://github.com/valentjn/vscode-ltex/issues/7)
- &#x1f527; *Change:* Save dictionary settings under full language short code (e.g., `en-US` instead of `en`). If you already have a dictionary under `ltex.en.dictionary` and use `en-US` as language (not `en`), you have to rename the settings name to `ltex.en-US.dictionary` (similarly for other languages).
- &#x1f5d1; *Removal:* Remove diagnostics when a file is closed
- &#x1f41b; *Bug fix:* Prevent insertion of text in Ti*k*Z mode
- &#x2728; *New:* Add support for more commands such as `\newenvironment`, `\newgeometry`, and `\pagenumbering`
- &#x1f527; *Change:* Update LTeX LS to 4.7.0

## 4.6.13 &#x2014; &#x201c;The Remote Permeability&#x201d; (September 26, 2019)

- &#x1f41b; *Bug fix:* Fix language extensions not installable on remote machines &#x2014; [#8](https://github.com/valentjn/vscode-ltex/issues/8)
- &#x1f41b; *Bug fix:* Fix LTeX LS not reinitialized after a language extension has been installed (which was missing during initialization)
- &#x1f527; *Change:* Update LTeX LS to 4.6.13

## 4.6.12 &#x2014; &#x201c;The Interpolation Entanglement&#x201d; (September 25, 2019)

- &#x1f41b; *Bug fix:* Patch LanguageTool's `AnnotatedText` with linear interpolation to hopefully fix the `fromPos must be less than toPos` LT errors for good
- &#x1f41b; *Bug fix:* Fix `\footnote` in math mode messed up text mode and math mode
- &#x1f527; *Change:* Increase robustness in case locale or settings are not provided
- &#x1f527; *Change:* Ignore all brace and bracket arguments after `\begin{environment}` (`tabular`, `array`, etc.)
- &#x2728; *New:* Add support for some more commands and environments such as `\pagestyle` and `eqnarray`
- &#x1f527; *Change:* Update LTeX LS to 4.6.12

## 4.6.11 &#x2014; &#x201c;The Infinite Loop Contraction&#x201d; (September 23, 2019)

- &#x1f41b; *Bug fix:* Detect and prevent infinite loops in `LatexAnnotatedTextBuilder`
- &#x1f41b; *Bug fix:* Fix infinite loop with other line endings than `\n`
- &#x1f41b; *Bug fix:* Fix some more `fromPos must be less than toPos` LT errors
- &#x1f527; *Change:* Check for interrupts to avoid 100% CPU usage on timeout (this doesn't fix any bugs though)
- &#x2728; *New:* Add support for `\email`, `\href`, and `\verb|...|`
- &#x2728; *New:* Add support for more citation commands (`\citep`, `\citet`, etc.)
- &#x2728; *New:* Add support for float/theorem definition commands and starred sectioning commands
- &#x1f527; *Change:* Update LTeX LS to 4.6.11

## 4.6.10 &#x2014; &#x201c;The Plaintext Decay&#x201d; (September 18, 2019)

- &#x1f527; *Change:* Don't check plaintext files &#x2014; [#4](https://github.com/valentjn/vscode-ltex/issues/4)
- &#x1f41b; *Bug fix:* Fix `NullPointerException` if LanguageTool has not been initialized &#x2014; [ltex-ls#1](https://github.com/valentjn/ltex-ls/issues/1)
- &#x1f527; *Change:* Update LTeX LS to 4.6.10

## 4.6.9 &#x2014; &#x201c;The Bundle Valuation&#x201d; (September 8, 2019)

- &#x1f527; *Change:* Bundle Node.js modules to decrease number of files in the extension (this means a slight performance gain)
- &#x1f527; *Change:* Update LTeX LS to 4.6.9

## 4.6.8 &#x2014; &#x201c;The Severity Manifestation&#x201d; (September 7, 2019)

- &#x2728; *New:* Add setting [`ltex.diagnosticSeverity`](../settings.html#ltexdiagnosticseverity) to control where and how the diagnostics appear
- &#x1f41b; *Bug fix:* Change default severity from `warning` to `info`
- &#x2728; *New:* Add possibility to ignore a LanguageTool rule in a sentence via quick fix
- &#x2728; *New:* Add setting [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) to control which `settings.json` to update when using one of the quick fixes
- &#x1f41b; *Bug fix:* More commands like `\PackageWarning` and `\addbibresource` are ignored
- &#x2728; *New:* Add support for `\url` and `\nolinkurl`
- &#x2728; *New:* Add support for more accents (`` \` ``, `\'`, `\^`, `\~`, `\"`, `\=`, `\.`, ...)
- &#x1f527; *Change:* Command names can now include `@` (this assumes that users don't write something like `\example@gmail.com` with a command `\example`, otherwise replace with `\example{}@gmail.com`)
- &#x1f527; *Change:* Ignore alignment argument of tabular environment
- &#x1f527; *Change:* Update LTeX LS to 4.6.8

## 4.6.7 &#x2014; &#x201c;The Model Combustion&#x201d; (September 2, 2019)

- &#x2728; *New:* Add possibility to use language model *n*-gram data, neural network model data, or word2vec model data
- &#x1f527; *Change:* `Add to dictionary` now always modifies global settings

## 4.6.6 &#x2014; &#x201c;The Timeout Theorem&#x201d; (September 2, 2019)

- &#x1f41b; *Bug fix:* Fix `fromPos must be less than toPos` LT errors
- &#x2728; *New:* Localization of diagnostics, initially support of English and German
- &#x2728; *New:* Add timeout for `latex.AnnotatedTextBuilder`; unfortunately this only displays an error, but does not kill the process
- &#x2728; *New:* Add support for `\(`, `\)`, `\[`, `\]`
- &#x1f527; *Change:* Don't insert spaces before `\text` in display math

## 4.6.5 &#x2014; &#x201c;The Consistency Integration&#x201d; (September 2, 2019)

- &#x1f527; *Change:* Make readme and `package.json` consistent
- &#x1f41b; *Bug fix:* Fix second arguments of `\(re)newcommand` not ignored

## 4.6.4 &#x2014; &#x201c;The Umlaut Expansion&#x201d; (September 1, 2019)

- &#x1f527; *Change:* Ignore some commands often found in LaTeX preambles
- &#x2728; *New:* Support umlauts and eszett

## 4.6.3 &#x2014; &#x201c;The Version Interruption&#x201d; (September 1, 2019)

- &#x1f41b; *Bug fix:* Fix deployed `*.vsix` needed Java 11, not 8

## 4.6.2 &#x2014; &#x201c;The vsce Minimization&#x201d; (September 1, 2019)

- &#x1f527; *Change:* Don't include vsce in extension

## 4.6.1 &#x2014; &#x201c;The Badges Vortex&#x201d; (September 1, 2019)

- &#x1f527; *Change:* Link badges in readme

## 4.6.0 &#x2014; &#x201c;The LTeX Resurgence&#x201d; (September 1, 2019)

- &#x1f527; *Change:* Forked abandoned repository, rename to vscode-ltex
- &#x1f527; *Change:* Update LanguageTool to 4.6 (see [LT 4.6 release notes](https://github.com/languagetool-org/languagetool/blob/v4.6/languagetool-standalone/CHANGES.md#46-2019-06-26))
- &#x1f527; *Change:* Update other dependencies (vscode, vscode-languageclient, LSP, JUnit, Gradle)
- &#x1f527; *Change:* Implement simple LaTeX parser

## 3.8.0 (July 8, 2017)

- &#x1f527; *Change:* Update LanguageTool to 3.8 (see [LT 3.8 release notes](https://github.com/languagetool-org/languagetool/blob/v3.8/languagetool-standalone/CHANGES.md#38-2017-06-27))
- &#x1f527; *Change:* Update versioning to reflect LanguageTool versioning
- &#x1f5d1; *Removal:* Remove preview flag since no blocker issues have been reported

## 0.0.4 (June 22, 2017)

- &#x2728; *New:* Add configuration to make extension opt-in by workspace &#x2014; [adamvoss/vscode-languagetool#5](https://github.com/adamvoss/vscode-languagetool/issues/5), [Faustino Aguilar (@faustinoaq)](https://github.com/faustinoaq)
- &#x2728; *New:* Language-support extensions are now detected through the Visual Studio Code API rather than file-path assumptions

## 0.0.3 (June 14, 2017)

- &#x1f41b; *Bug fix:* Fix checking of files when no folder was open
- &#x1f41b; *Bug fix:* Prevent virtual files (including those from Git) from being checked &#x2014; [adamvoss/vscode-languagetool#2](https://github.com/adamvoss/vscode-languagetool/issues/2)

## 0.0.2 (June 12, 2017)

- &#x2728; *New:* Allow any LanguageTool supported language to be used through the use of supplemental extensions
- &#x1f5d1; *Removal:* Remove built-in English support

## 0.0.1 (June 3, 2017)

- &#x2728; *New:* Initial release
