---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Changelog"
permalink: "/ltex-ls/changelog.html"
sidebar: "sidebar"
toc: false
---

## 15.2.0 (November 28, 2021)

- &#x2728; *New:* Add support for ConTeXt &#x2014; [#120](https://github.com/valentjn/ltex/issues/120)
- &#x2728; *New:* Add support for strikethrough as in [GitHub Flavored Markdown](https://github.github.com/gfm/#strikethrough-extension-) &#x2014; [#123](https://github.com/valentjn/ltex/issues/123)
- &#x2728; *New:* Always check selected text when running [`_ltex.checkDocument`](https://valentjn.github.io/ltex/ltex-ls/server-usage.html#_ltexcheckdocument-server), even non-comment parts of programs &#x2014; [vscode-ltex#457](https://github.com/valentjn/vscode-ltex/issues/457)
- &#x2728; *New:* Add support for the `minted` package (LaTeX) &#x2014; [vscode-ltex#463](https://github.com/valentjn/vscode-ltex/issues/463)
- &#x2728; *New:* Add support for the Pandoc language variable `lang` in YAML front matter (Markdown) &#x2014; [vscode-ltex#465](https://github.com/valentjn/vscode-ltex/issues/465)

## 15.1.0 (November 5, 2021)

- &#x2728; *New:* Add support for some aliases of LSP language IDs: `bib` for `bibtex`, `plaintex` for `latex`, `xhtml` for `html`
- &#x1f41b; *Bug fix:* Fix LTeX LS sometimes not properly terminated when using LTeX CLI &#x2014; [#117](https://github.com/valentjn/ltex/issues/117)
- &#x1f41b; *Bug fix:* Fix error when running `ltex-cli` from a different directory than `bin/`

## 15.0.0 (October 30, 2021)

- &#x1f527; *Change:* Add [`ltex.completionEnabled`](../settings.html#ltexcompletionenabled) to disable completion by default &#x2014; [vscode-ltex#443](https://github.com/valentjn/vscode-ltex/issues/443)
- &#x1f41b; *Bug fix:* Fix `StringIndexOutOfBoundsException` in `AnnotatedTextFragment.getSubstringOfPlainText` &#x2014; [vscode-ltex#442](https://github.com/valentjn/vscode-ltex/issues/442)
- &#x1f41b; *Bug fix:* Fix handling of multiple subsequent whitespace characters in XHTML (e.g., CRLF)

## 14.1.0 (October 19, 2021)

- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolHttpServerUri` &#x2192; [`ltex.languageToolHttpServerUri`](../settings.html#ltexlanguagetoolhttpserveruri); the previous name is deprecated
- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolOrgUsername` &#x2192; [`ltex.languageToolOrg.username`](../settings.html#ltexlanguagetoolorgusername); the previous name is deprecated
- &#x1f527; *Change:* Rename `ltex.ltex-ls.languageToolOrgApiKey` &#x2192; [`ltex.languageToolOrg.apiKey`](../settings.html#ltexlanguagetoolorgapikey); the previous name is deprecated
- &#x2728; *New:* Add support for completion requests for English and German &#x2014; [vscode-ltex#409](https://github.com/valentjn/vscode-ltex/issues/409)
- &#x1f41b; *Bug fix:* Fix `Add '...' to dictionary` quick fix missing for Austrian and Swiss German &#x2014; [vscode-ltex#431](https://github.com/valentjn/vscode-ltex/issues/431)
- &#x1f527; *Change:* Move documentation to <https://valentjn.github.io/ltex>

## 14.0.0 (October 14, 2021)

- &#x1f527; *Change:* Update LanguageTool to 5.5 (see [LT 5.5 release notes](https://github.com/languagetool-org/languagetool/blob/v5.5/languagetool-standalone/CHANGES.md#55-2021-10-02))
- &#x1f527; *Change:* Refactor CLI into `ltex-cli`; `--input-documents` and `--setings-file` are deprecated and will be removed in a future release
- &#x2728; *New:* Add support for automatic language detection via language short code `auto`; language variants like `en-US` are not detected, only generic languages like `en`; this will result in spelling errors not being reported &#x2014; [#103](https://github.com/valentjn/ltex/issues/103)
- &#x2728; *New:* Provide ID of LanguageTool rule via diagnostics code, not as part of diagnostics message
- &#x2728; *New:* Link diagnostics to LanguageTool website with more information
- &#x2728; *New:* Add support for the `main` option of the babel package (LaTeX) &#x2014; [vscode-ltex#391](https://github.com/valentjn/vscode-ltex/issues/391)
- &#x2728; *New:* Add setting `ltex.ltex-ls.languageToolOrgUsername` to set username on languagetool.org for Premium API access &#x2014; [vscode-ltex#398](https://github.com/valentjn/vscode-ltex/issues/398)
- &#x2728; *New:* Add setting `ltex.ltex-ls.languageToolOrgApiKey` to set API key on languagetool.org for Premium API access &#x2014; [vscode-ltex#398](https://github.com/valentjn/vscode-ltex/issues/398)
- &#x2728; *New:* Add support for [`ltex.dictionary`](../settings.html#ltexdictionary) when using a LanguageTool HTTP server
- &#x1f527; *Change:* Handle disabled rules ourselves to prevent reinitialization of LanguageTool when running the `Disable rule` quick fix &#x2014; [vscode-ltex#390](https://github.com/valentjn/vscode-ltex/issues/390)
- &#x1f41b; *Bug fix:* Fix LanguageTool reinitialized when running the `Add '...' to dictionary` quick fix &#x2014; [vscode-ltex#390](https://github.com/valentjn/vscode-ltex/issues/390)
- &#x1f41b; *Bug fix:* Fix wrong parsing of inline math formulas in Markdown when using dollar signs as delimiters and containing only one character (e.g., `$a$`)
- &#x1f41b; *Bug fix:* Fix used i18n keys removed
- &#x1f41b; *Bug fix:* Fix fallback from German to English i18n
- &#x1f527; *Change:* For binary archives, migrate from AdoptOpenJDK JREs to own Java runtime generated from Eclipse Adoptium JDKs
- &#x1f527; *Change:* Update bundled Java runtime to 11.0.12+7 (see [list of OpenJDK fixes](https://bugs.openjdk.java.net/browse/JDK-8269291?jql=project%20%3D%20JDK%20AND%20fixVersion%20%3D%2011.0.12))

## 13.0.0 (August 11, 2021)

- &#x1f527; *Change:* Migrate from Java to Kotlin
- &#x2728; *New:* Add support for checking comments in many popular programming languages &#x2014; [vscode-ltex#350](https://github.com/valentjn/vscode-ltex/issues/350)
- &#x2728; *New:* Add non-server batch mode via `--input-documents` &#x2014; [#71](https://github.com/valentjn/ltex/issues/71)
- &#x2728; *New:* Add support for rule-dependent diagnostic severities in [`ltex.diagnosticSeverity`](../settings.html#ltexdiagnosticseverity) &#x2014; [#95](https://github.com/valentjn/ltex/issues/95)
- &#x2728; *New:* Add support for vowel dummies in LaTeX (`"vowelDummy"` in [`ltex.latex.commands`](../settings.html#ltexlatexcommands)) and Markdown (`"vowelDummy"` in [`ltex.markdown.nodes`](../settings.html#ltexmarkdownnodes)) &#x2014; [vscode-ltex#366](https://github.com/valentjn/vscode-ltex/issues/366)
- &#x2728; *New:* Add support for more LaTeX commands (`\mathop`, `\overline`, `\tilde`, `\alpha`, etc.) for automatic vowel detection in formulas in LaTeX &#x2014; [#92](https://github.com/valentjn/ltex/issues/92), [Shuhao Cao (@scaomath)](https://github.com/scaomath)
- &#x2728; *New:* Add support for `\counterwithin`, `\counterwithout`, and `\numberwithin` in LaTeX &#x2014; [#87](https://github.com/valentjn/ltex/issues/87), [Alexander Zeilmann (@AlexanderZeilmann)](https://github.com/AlexanderZeilmann)
- &#x1f41b; *Bug fix:* Don't ignore second argument of `\setkomavar` in LaTeX &#x2014; [vscode-ltex#373](https://github.com/valentjn/vscode-ltex/issues/373)
- &#x2728; *New:* Add support for [`InitializeParams.locale`](https://microsoft.github.io/language-server-protocol/specifications/specification-3-17/#initializeParams) when using LSP 3.16 or later, deprecate `CustomInitializationOptions.locale`
- &#x1f5d1; *Removal:* Remove support for magic comments in XHTML
- &#x1f527; *Change:* Change format of changelog

## 12.3.0 (July 12, 2021)

- &#x1f527; *Change:* Update LanguageTool to 5.4 (see [LT 5.4 release notes](https://github.com/languagetool-org/languagetool/blob/v5.4/languagetool-standalone/CHANGES.md#54-2021-06-25))
- &#x2728; *New:* Add support for XHTML &#x2014; [vscode-ltex#342](https://github.com/valentjn/vscode-ltex/issues/342)
- &#x1f41b; *Bug fix:* Fix diagnostics contain markup before actual error &#x2014; [vscode-ltex#349](https://github.com/valentjn/vscode-ltex/issues/349)
- &#x1f41b; *Bug fix:* Fix error when checking LaTeX documents ending with specific commands &#x2014; [vscode-ltex#341](https://github.com/valentjn/vscode-ltex/issues/341)
- &#x2728; *New:* Fix name of Portuguese babel language names, add support for Brazilian Portuguese babel language names &#x2014; [#72](https://github.com/valentjn/ltex/issues/72)

## 12.2.0 (June 5, 2021)

- &#x2728; *New:* Add support for `\setplength` (LaTeX)
- &#x2728; *New:* Add `--log-file` option to tee server/client communication and server log to a file
- &#x1f41b; *Bug fix:* Fix LTeX LS not terminating if input stream is end-of-file &#x2014; [vscode-ltex#325](https://github.com/valentjn/vscode-ltex/issues/325)
- &#x1f527; *Change:* Bundle Java for platform-dependent, standalone archives &#x2014; [#70](https://github.com/valentjn/ltex/issues/70)

## 12.1.0 (May 1, 2021)

- &#x2728; *New:* Add support for cancellation of checking requests &#x2014; [vscode-ltex#253](https://github.com/valentjn/vscode-ltex/issues/253)
- &#x1f527; *Change:* Show `Use ...` quick fixes before other quick fixes &#x2014; [vscode-ltex#297](https://github.com/valentjn/vscode-ltex/issues/297)
- &#x1f527; *Change:* Limit number of `Use ...` quick fixes to 5 &#x2014; [vscode-ltex#297](https://github.com/valentjn/vscode-ltex/issues/297)
- &#x2728; *New:* Add `isChecking` and `documentUriBeingChecked` fields to result of `_ltex.getServerStatus`
- &#x2728; *New:* Add support for `\phantom`, `\hphantom`, and `\vphantom` (LaTeX)
- &#x1f41b; *Bug fix:* Fix wrong underlining of words starting with markup &#x2014; [#69](https://github.com/valentjn/ltex/issues/69)

## 12.0.0 (April 18, 2021)

- &#x1f527; *Change:* Prefix all command names with an underscore to mark them as internal (for hiding them from the user in some clients)
- &#x1f527; *Change:* Rename `ltex.addToDictionary` &#x2192; `_ltex.addToDictionary`
- &#x1f527; *Change:* Rename `ltex.disableRules` &#x2192; `_ltex.disableRules`
- &#x1f527; *Change:* Rename `ltex.hideFalsePositives` &#x2192; `_ltex.hideFalsePositives`
- &#x1f527; *Change:* Rename `ltex.checkDocument` &#x2192; `_ltex.checkDocument`
- &#x1f527; *Change:* Rename `ltex.getServerStatus` &#x2192; `_ltex.getServerStatus`
- &#x2728; *New:* Add support for Org; use the code language ID `org` &#x2014; [vscode-ltex#277](https://github.com/valentjn/vscode-ltex/issues/277)
- &#x2728; *New:* Add basic support for reStructuredText; use the code language ID `restructuredtext` &#x2014; [vscode-ltex#32](https://github.com/valentjn/vscode-ltex/issues/32)
- &#x2728; *New:* Add `--server-type=tcpSocket` option to communicate over a TCP socket
- &#x2728; *New:* Add `--host` and `--port` options to control host and port of the TCP socket
- &#x2728; *New:* Add `--[no-]endless` option to keep the server alive when the client terminates the connection
- &#x2728; *New:* Add `-h` and `--help` options to show help message
- &#x2728; *New:* Add `-V` option as alias for `--version`
- &#x1f5d1; *Removal:* Remove support of single CR characters as line endings
- &#x1f41b; *Bug fix:* Fix `.Rnw` not recognized for R Sweave documents when running `_ltex.checkDocument`
- &#x1f41b; *Bug fix:* Fix newlines accepted as whitespace in magic comments
- &#x1f527; *Change:* Use picocli for parsing of command-line arguments

## 11.0.0 (April 5, 2021)

- &#x1f527; *Change:* Update LanguageTool to 5.3 (see [LT 5.3 release notes](https://github.com/languagetool-org/languagetool/blob/v5.3/languagetool-standalone/CHANGES.md#53-2021-03-29))
- &#x1f527; *Change:* Update LSP4J to 0.12.0
- &#x2728; *New:* Enhance support of accents in LaTeX by using Unicode combining diacritical marks, normalized via [Unicode Normalization Form C](https://www.unicode.org/reports/tr15/tr15-50.html#Normalization_Forms_Table) &#x2014; [vscode-ltex#269](https://github.com/valentjn/vscode-ltex/issues/269)
- &#x2728; *New:* Add support for many accents in LaTeX: double acute (e.g., `\H{O}`, &#x0150;), line below (e.g., `\b{h}`, &#x1e96;), dot below (e.g., `\d{A}`, &#x1ea0;), ogonek (e.g., `\k{A}`, &#x0104;), breve (e.g., `\u{A}`, &#x0102;), and caron (e.g., `\v{C}`, &#x010c;) &#x2014; [#56](https://github.com/valentjn/ltex/issues/56), [#57](https://github.com/valentjn/ltex/issues/57), [@ed359](https://github.com/ed359)
- &#x2728; *New:* Add support for special characters in LaTeX: `\L` (&#x0141;), `\SS` (&#x1e9e;), `\i` (&#x0131;), `\j` (&#x0237;), and `\l` (&#x0142;) &#x2014; [#56](https://github.com/valentjn/ltex/issues/56), [#57](https://github.com/valentjn/ltex/issues/57), [@ed359](https://github.com/ed359)
- &#x2728; *New:* Add `FR_SPELLING_RULE` as a rule for unknown words &#x2014; [#47](https://github.com/valentjn/ltex/issues/47), [Nicolas Sicard (@biozic)](https://github.com/biozic)
- &#x1f527; *Change:* Use LaTeX parser for documents with code language ID `tex` &#x2014; [#53](https://github.com/valentjn/ltex/issues/53), [#54](https://github.com/valentjn/ltex/issues/54), [Lucas Alber (@LDAP)](https://github.com/LDAP)
- &#x2728; *New:* Add support for [Markdown Extra definition lists](https://michelf.ca/projects/php-markdown/extra/#def-list) &#x2014; [vscode-ltex#268](https://github.com/valentjn/vscode-ltex/issues/268)
- &#x1f527; *Change:* Ignore non-object values for `InitializeParams.initializationOptions` &#x2014; [#65](https://github.com/valentjn/ltex/issues/65)

## 10.0.0 (February 12, 2021)

- &#x1f5d1; *Removal:* Remove support for settings that are deprecated since 8.0.0: `ltex.ignoreInRuleSentence`, `ltex.commands.ignore`, `ltex.commands.dummy`, `ltex.environments.ignore`, `ltex.markdown.ignore`, and `ltex.markdown.dummy`
- &#x1f527; *Change:* Replace `ltex/serverStatus` request with `ltex.getServerStatus` command
- &#x2728; *New:* Add support for magic comments inside HTML comments in Markdown (`<!-- ltex: SETTINGS -->`)
- &#x1f527; *Change:* Check frame title in argument of LaTeX Beamer frames &#x2014; [vscode-ltex#239](https://github.com/valentjn/vscode-ltex/issues/239)
- &#x2728; *New:* Add `range` argument to `ltex.checkDocument`
- &#x2728; *New:* Check documents even if their code language is not supported
- &#x1f41b; *Bug fix:* Fix comment sign before babel commands not recognized &#x2014; [vscode-ltex#245](https://github.com/valentjn/vscode-ltex/issues/245)
- &#x1f41b; *Bug fix:* Fix removing items in settings with a hyphen prefix sometimes not working
- &#x1f41b; *Bug fix:* Fix space not added between two arguments of LaTeX commands
- &#x1f41b; *Bug fix:* Fix manually checking BibTeX documents not working
- &#x1f41b; *Bug fix:* Fix words in dictionary containing markup not recognized

## 9.2.0 (January 29, 2021)

- &#x2728; *New:* Add support for Pandoc-style inline math (`$...$`) and display math (`$$...$$` with `$$` being at the beginning/end of a Markdown block) to Markdown parser &#x2014; [vscode-ltex#210](https://github.com/valentjn/vscode-ltex/issues/210)
- &#x1f41b; *Bug fix:* Fix false positives for words added by `Add to dictionary` for Slovak rule IDs `MUZSKY_ROD_NEZIV_A`, `ZENSKY_ROD_A`, and `STREDNY_ROD_A` &#x2014; [vscode-ltex#221](https://github.com/valentjn/vscode-ltex/issues/221)
- &#x1f41b; *Bug fix:* Fix BibTeX field `seealso` not ignored, ignore `category` and `parent` &#x2014; [vscode-ltex#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x1f527; *Change:* Disable `UPPERCASE_SENTENCE_START` in BibTeX files &#x2014; [vscode-ltex#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x1f527; *Change:* Move rule ID to the end of diagnostic messages as VS Code truncates the messages if the Problems panel is narrow &#x2014; [vscode-ltex#233](https://github.com/valentjn/vscode-ltex/issues/233)
- &#x1f41b; *Bug fix:* Fix regression that messages of possible spelling mistakes are not prepended with the respective unknown words &#x2014; [vscode-ltex#161](https://github.com/valentjn/vscode-ltex/issues/161)
- &#x1f41b; *Bug fix:* Fix crash when using `\begin` or `\end` without an argument &#x2014; [vscode-ltex#236](https://github.com/valentjn/vscode-ltex/issues/236)
- &#x1f527; *Change:* Change `$/progress` tokens to include a UUID instead of a counter

## 9.1.0 (January 24, 2021)

- &#x2728; *New:* Add support for BibTeX files (language code `bibtex`) &#x2014; [vscode-ltex#211](https://github.com/valentjn/vscode-ltex/issues/211)
- &#x2728; *New:* Add setting [`ltex.bibtex.fields`](../settings.html#ltexbibtexfields) to control which BibTeX fields should be checked
- &#x2728; *New:* Add support for [GitLab Flavored Markdown](https://gitlab.com/gitlab-org/gitlab/blob/master/doc/user/markdown.md), especially inline math (e.g., ``$`E = mc^2`$``) &#x2014; [vscode-ltex#210](https://github.com/valentjn/vscode-ltex/issues/210)
- &#x2728; *New:* Add support for Markdown tables as in [GitHub Flavored Markdown](https://github.github.com/gfm/#tables-extension-) &#x2014; [vscode-ltex#218](https://github.com/valentjn/vscode-ltex/issues/218)
- &#x2728; *New:* Add support for more commands of the `glossaries` LaTeX package
- &#x1f527; *Change:* Enable `Add to dictionary` quick fix for Slovak rule IDs `MUZSKY_ROD_NEZIV_A`, `ZENSKY_ROD_A`, and `STREDNY_ROD_A` &#x2014; [vscode-ltex#221](https://github.com/valentjn/vscode-ltex/issues/221)
- &#x1f5d1; *Removal:* Remove superfluous spaces in messages of diagnostics
- &#x1f41b; *Bug fix:* Fix handling of `\r\n` (Windows) line terminators in Markdown
- &#x1f527; *Change:* Use Flexmark's YAML Front Matter extension to ignore YAML front matter in Markdown instead of own handling
- &#x1f527; *Change:* Print Flexmark AST of Markdown documents to log when [`ltex.ltex-ls.logLevel`](../settings.html#ltexltex-lsloglevel) is `"finest"`

## 9.0.1 (January 13, 2021)

- &#x1f527; *Change:* Ignore `\pgfmathsetmacro`, `\setmainfont`, and `\theoremstyle`
- &#x1f41b; *Bug fix:* Fix accent commands such as `\O` in math mode resulting in diagnostics &#x2014; [vscode-ltex#216](https://github.com/valentjn/vscode-ltex/issues/216)

## 9.0.0 (January 3, 2021)

- &#x1f527; *Change:* Make versioning independent of vscode-ltex; LTeX LS now adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- &#x2728; *New:* Require support of LSP 3.15
- &#x1f527; *Change:* Update LanguageTool to 5.2 (see [LT 5.2 release notes](https://github.com/languagetool-org/languagetool/blob/v5.2/languagetool-standalone/CHANGES.md#52-released-2020-12-29))
- &#x2728; *New:* Add [`ltex.additionalRules.enablePickyRules`](../settings.html#ltexadditionalrulesenablepickyrules) to still be able to detect false friends after the update of LanguageTool (default: `false`)
- &#x1f527; *Change:* Replace `ltex/progress` with `$/progress` &#x2014; [#34](https://github.com/valentjn/ltex/issues/34)
- &#x2728; *New:* Add `customCapabilities` in `InitializeParams.initializationOptions`
- &#x1f5d1; *Removal:* Remove unneeded command arguments `type` and `command`
- &#x1f527; *Change:* Replace `\dots` with Unicode ellipsis `&#x2026;` instead of three dots `...` to fix some false positives
- &#x2728; *New:* Add documentation

## 8.1.1 (November 24, 2020)

- &#x1f527; *Change:* Migrate from Travis CI to GitHub Actions

## 8.1.0 (November 15, 2020)

- &#x1f527; *Change:* Prepend messages of possible spelling mistakes with the respective unknown words &#x2014; [vscode-ltex#161](https://github.com/valentjn/vscode-ltex/issues/161)
- &#x2728; *New:* Add support for optional arguments of `\newtheorem`
- &#x1f41b; *Bug fix:* Fix wrong position of diagnostics when using a recognized LaTeX command with a non-recognized set of arguments due to an infinite loop &#x2014; [vscode-ltex#167](https://github.com/valentjn/vscode-ltex/issues/167)
- &#x1f527; *Change:* Update LSP4J to 0.10.0

## 8.0.0 (November 1, 2020)

- &#x1f527; *Change:* Upgrade from Java 8 to Java 11 (see [announcement](https://valentjn.github.io/ltex/old/deprecation-of-java-8.html)) &#x2014; [vscode-ltex#39](https://github.com/valentjn/vscode-ltex/issues/39)
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
- &#x2728; *New:* Add `userExternalFile`, `workspaceExternalFile`, and `workspaceFolderExternalFile` enumeration values to [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget), which enables saving settings to external files (see [documentation](https://valentjn.github.io/ltex/vscode-ltex/setting-scopes-files.html#external-setting-files)) &#x2014; [vscode-ltex#144](https://github.com/valentjn/vscode-ltex/issues/144), [vscode-ltex#145](https://github.com/valentjn/vscode-ltex/issues/145)
- &#x1f527; *Change:* Change default of [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) for `dictionary`, `disabledRules`, and `hiddenFalsePositives` to `workspaceFolderExternalFile`
- &#x2728; *New:* Add [`ltex.checkFrequency`](../settings.html#ltexcheckfrequency) to control when LTeX checks documents &#x2014; [vscode-ltex#142](https://github.com/valentjn/vscode-ltex/issues/142)
- &#x2728; *New:* Add [`LTeX: Show Status Information`](../vscode-ltex/commands.html#ltex-show-status-information) command to show information about the status of LTeX
- &#x2728; *New:* Add support for `\usepackage[LANGUAGE]{babel}` if in the same file as the text to be checked &#x2014; [vscode-ltex#140](https://github.com/valentjn/vscode-ltex/issues/140)
- &#x2728; *New:* Add support for more BibLaTeX commands such as `\autocite`, `\citeauthor`, etc. &#x2014; [vscode-ltex#143](https://github.com/valentjn/vscode-ltex/issues/143)
- &#x2728; *New:* Add support for overriding hard-coded command signatures &#x2014; [#27](https://github.com/valentjn/ltex/issues/27)
- &#x1f527; *Change:* Move handling of external setting files from ltex-ls to vscode-ltex
- &#x1f527; *Change:* Increase duration before sentences expire in the result cache to 60 minutes
- &#x1f41b; *Bug fix:* Fix many settings changes cleared sentence cache, which led to performance issues, e.g., changing the [`ltex.enabled`](../settings.html#ltexenabled) setting via magic comments &#x2014; [vscode-ltex#134](https://github.com/valentjn/vscode-ltex/issues/134)
- &#x1f5d1; *Removal:* Remove dependency on `org.apache.httpcomponents:httpclient` by using the HTTP client that comes with Java 11 when connecting to an HTTP LanguageTool server

## 7.3.1 (October 12, 2020)

- &#x1f41b; *Bug fix:* Fix delayed publication of diagnostics by adding workaround to guess the caret position
- &#x1f41b; *Bug fix:* Fix recheck being triggered when generating list of quick fixes; this should improve speed

## 7.3.0 (October 10, 2020)

- &#x2728; *New:* Add support for `\ell` as well as `\mathcal`, `\mathfrak`, etc. to vowel detection &#x2014; [vscode-ltex#131](https://github.com/valentjn/vscode-ltex/issues/131)
- &#x2728; *New:* Add setting [`ltex.ltex-ls.logLevel`](../settings.html#ltexltex-lsloglevel) to control the verbosity of the server log
- &#x1f41b; *Bug fix:* Fix diagnostics sometimes not lined up with the text with switching back from incremental to full document updates; unfortunately, this disables the delayed publication of diagnostics at the caret position
- &#x1f527; *Change:* Restructure and simplify internal quick fix and command structure, removing the need for pseudo-telemetry notifications

## 7.2.0 (September 27, 2020)

- &#x1f527; *Change:* Update LanguageTool to 5.1 (see [LT 5.1 release notes](https://github.com/languagetool-org/languagetool/blob/v5.1/languagetool-standalone/CHANGES.md#51-released-2020-09-25))
- &#x2728; *New:* Add support for HTML entities such as `&auml;` and `&copy;` in Markdown
- &#x1f41b; *Bug fix:* Fix missing tilde expansion for external dictionary files
- &#x1f527; *Change:* Improve logging

## 7.1.2 (September 22, 2020)

- &#x1f41b; *Bug fix:* Fix performance issue with multiple languages in one document via magic comments due to LanguageTool being reinitialized on each keystroke &#x2014; [vscode-ltex#124](https://github.com/valentjn/vscode-ltex/issues/124)

## 7.1.1 (September 20, 2020)

- &#x1f41b; *Bug fix:* Fix `NullPointerException` when supplying relative paths to external dictionary files
- &#x1f41b; *Bug fix:* Fix German log messages

## 7.1.0 (September 20, 2020)

- &#x2728; *New:* Add support for external dictionary files &#x2014; [vscode-ltex#118](https://github.com/valentjn/vscode-ltex/issues/118)
- &#x2728; *New:* Add support for enabling/disabling LTeX only for specific file types via [`ltex.enabled`](../settings.html#ltexenabled) &#x2014; [vscode-ltex#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `acro` commands such as `\DeclareAcronym` and `\ac` &#x2014; [vscode-ltex#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `\addcontentsline` &#x2014; [vscode-ltex#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x2728; *New:* Add support for `\printbibliography` and `\printglossary` without argument
- &#x1f527; *Change:* Ignore parenthesis arguments of `textblock`s &#x2014; [vscode-ltex#19](https://github.com/valentjn/vscode-ltex/issues/19)
- &#x1f41b; *Bug fix:* Fix optional argument of heading commands such as `\section` parsed incorrectly &#x2014; [vscode-ltex#123](https://github.com/valentjn/vscode-ltex/issues/123)
- &#x1f527; *Change:* Include stack traces when logging exceptions

## 7.0.0 (September 13, 2020)

- &#x1f527; *Change:* Change scope of [`ltex.dictionary`](../settings.html#ltexdictionary), [`ltex.disabledRules`](../settings.html#ltexdisabledrules), and [`ltex.enabledRules`](../settings.html#ltexenabledrules) to `application`; these are now user-specific settings that can only be configured in user settings
- &#x2728; *New:* Add settings `ltex.workspaceDictionary`, `ltex.workspaceDisabledRules`, and `ltex.workspaceEnabledRules` with `window` scope to amend the corresponding user-specific settings; these are workspace-specific settings that should be configured in workspace settings
- &#x2728; *New:* Add settings `ltex.workspaceFolderDictionary`, `ltex.workspaceFolderDisabledRules`, and `ltex.workspaceFolderEnabledRules` with `resource` scope to amend the corresponding user-specific and workspace-specific settings; these are workspace-folder-specific settings that should be configured in workspace folder settings
- &#x1f527; *Change:* Rename `global` &#x2192; `user` in [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget)
- &#x1f5d1; *Removal:* Remove deprecated settings `ltex.javaHome`, `ltex.performance.initialJavaHeapSize`, `ltex.performance.maximumJavaHeapSize`, `ltex.performance.sentenceCacheSize`, `ltex.*.dictionary`, `ltex.*.enabledRules`, and `ltex.*.disabledRules` (deprecation since 5.0.0)
- &#x1f527; *Change:* Update LanguageTool to 5.0.2 (see [LT 5.0.2 release notes](https://github.com/languagetool-org/languagetool/blob/v5.0.2/languagetool-standalone/CHANGES.md#502-2020-08-28))
- &#x1f41b; *Bug fix:* Fix skipping of YAML front matter &#x2014; [vscode-ltex#104](https://github.com/valentjn/vscode-ltex/issues/104)

## 6.3.0 (August 22, 2020)

- &#x2728; *New:* Add support for `an` article when before a formula starting with a vowel (e.g., `an $n$-dimensional problem`) &#x2014; [vscode-ltex#92](https://github.com/valentjn/vscode-ltex/issues/92)
- &#x2728; *New:* Add support for `~/` and `~\` in settings &#x2014; [vscode-ltex#99](https://github.com/valentjn/vscode-ltex/issues/99)

## 6.2.0 (August 7, 2020)

- &#x2728; *New:* Add commands [`LTeX: Check Current Document`](../vscode-ltex/commands.html#ltex-check-current-document) and [`LTeX: Check All Documents in Workspace`](../vscode-ltex/commands.html#ltex-check-all-documents-in-workspace) &#x2014; [vscode-ltex#84](https://github.com/valentjn/vscode-ltex/issues/84)
- &#x2728; *New:* Add setting [`ltex.clearDiagnosticsWhenClosingFile`](../settings.html#ltexcleardiagnosticswhenclosingfile)
- &#x1f527; *Change:* Skip front matter in Markdown
- &#x1f527; *Change:* Ignore more LaTeX preamble commands (e.g., `\automark`, `\color`, `\DeclareSIUnit`, `\directlua`, `\setuptoc`)
- &#x2728; *New:* Add support for German babel hyphenation commands `"-`, `""`, `"|`, `"=`, `"~`
- &#x1f527; *Change:* Use non-breaking space for `~`

## 6.1.1 (July 26, 2020)

- &#x1f41b; *Bug fix:* Fix another problem with spaces in paths on Windows &#x2014; [vscode-ltex#80](https://github.com/valentjn/vscode-ltex/issues/80)

## 6.1.0 (July 26, 2020)

- &#x2728; *New:* LTeX LS support for Java 8 will end on November 1, 2020 (see [documentation](https://valentjn.github.io/ltex/old/deprecation-of-java-8.html)) &#x2014; [vscode-ltex#39](https://github.com/valentjn/vscode-ltex/issues/39)
- &#x2728; *New:* Add support for babel commands (see [documentation](https://valentjn.github.io/ltex/advanced-usage.html#multilingual-latex-documents-with-the-babel-package)) &#x2014; [vscode-ltex#81](https://github.com/valentjn/vscode-ltex/issues/81)
- &#x1f41b; *Bug fix:* Fix problems with spaces in paths on Windows &#x2014; [vscode-ltex#80](https://github.com/valentjn/vscode-ltex/issues/80)

## 6.0.2 (July 11, 2020)

- &#x1f527; *Change:* Make Windows startup script (`ltex-ls.bat`) honor `JAVA_HOME` &#x2014; [vscode-ltex#75](https://github.com/valentjn/vscode-ltex/issues/75)

## 6.0.1 (July 2, 2020)

- &#x1f41b; *Bug fix:* Fix freezes when checking German text by working around [languagetool-org/languagetool#3181](https://github.com/languagetool-org/languagetool/issues/3181) introduced by LanguageTool 5.0 &#x2014; [vscode-ltex#68](https://github.com/valentjn/vscode-ltex/issues/68)

## 6.0.0 (June 28, 2020)

- &#x1f527; *Change:* Update LanguageTool to 5.0 (see [LT 5.0 release notes](https://github.com/languagetool-org/languagetool/blob/v5.0/languagetool-standalone/CHANGES.md#50-2020-06-27))
- &#x1f527; *Change:* Delay diagnostics at the current caret position (e.g., incomplete word or sentence) until the user has finished typing &#x2014; [vscode-ltex#46](https://github.com/valentjn/vscode-ltex/issues/46)
- &#x2728; *New:* Add `enabled` to magic comments &#x2014; [vscode-ltex#67](https://github.com/valentjn/vscode-ltex/issues/67)
- &#x1f41b; *Bug fix:* Fix `\todo` couldn't be ignored &#x2014; [vscode-ltex#63](https://github.com/valentjn/vscode-ltex/issues/63)
- &#x1f41b; *Bug fix:* Fix wrong language-dependent settings used for magic comments
- &#x1f41b; *Bug fix:* Fix add to dictionary and disable rule quick fixes using wrong language when used with magic comments
- &#x1f41b; *Bug fix:* Improve code quality by fixing hundreds of Checkstyle, SpotBugs, and Checker Framework warnings
- &#x1f527; *Change:* Migrate from Gradle to Maven
- &#x1f527; *Change:* Update Maven dependencies

## 5.0.0 (June 1, 2020)

- &#x2728; *New:* Include all languages in LTeX LS; this removes the need for language support extensions &#x2014; [vscode-ltex#6](https://github.com/valentjn/vscode-ltex/issues/6)
- &#x1f527; *Change:* Adhere to [semantic versioning](https://semver.org/). This means that the version of LTeX LS is not tied to the version of LanguageTool anymore, as the version of LanguageTool is not a semantic version. LTeX LS 5.0.0 uses LanguageTool 4.9.
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.dictionary` &#x2192; [`ltex.dictionary`](../settings.html#ltexdictionary) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.disabledRules` &#x2192; [`ltex.disabledRules`](../settings.html#ltexdisabledrules) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.<LANGUAGE>.enabledRules` &#x2192; [`ltex.enabledRules`](../settings.html#ltexenabledrules) (object with `<LANGUAGE>` keys)
- &#x1f527; *Change:* Rename `ltex.javaHome` &#x2192; [`ltex.java.path`](../settings.html#ltexjavapath)
- &#x1f527; *Change:* Rename `ltex.performance.initialJavaHeapSize` &#x2192; [`ltex.java.initialHeapSize`](../settings.html#ltexjavainitialheapsize)
- &#x1f527; *Change:* Rename `ltex.performance.maximumJavaHeapSize` &#x2192; [`ltex.java.maximumHeapSize`](../settings.html#ltexjavamaximumheapsize)
- &#x1f527; *Change:* Rename `ltex.performance.sentenceCacheSize` &#x2192; [`ltex.sentenceCacheSize`](../settings.html#ltexsentencecachesize)
- &#x2728; *New:* Add support for external LanguageTool HTTP servers &#x2014; [vscode-ltex#36](https://github.com/valentjn/vscode-ltex/issues/36)
- &#x2728; *New:* Add support for magic comments, enables changing the language in the middle of documents &#x2014; [vscode-ltex#21](https://github.com/valentjn/vscode-ltex/issues/21)
- &#x1f41b; *Bug fix:* Check `\footnote` and `\todo` contents separately, preventing &#x201c;double period&#x201d; warnings &#x2014; [vscode-ltex#42](https://github.com/valentjn/vscode-ltex/issues/42)
- &#x2728; *New:* Add support for more BibLaTeX citation commands, add support for plural dummies, add support for `\eg`, `\egc`, `\ie`, `\iec` &#x2014; [vscode-ltex#43](https://github.com/valentjn/vscode-ltex/issues/43)
- &#x2728; *New:* Add visual feedback in status bar during startup and checks that take a long time
- &#x1f5d1; *Removal:* Remove `null` types and default values from settings, use empty string/array/object instead &#x2014; [vscode-ltex#41](https://github.com/valentjn/vscode-ltex/issues/41)
- &#x1f527; *Change:* Use proper server/client model for language server/client
- &#x1f527; *Change:* Make documentation of vscode-ltex more extensive, put it on own [website](https://valentjn.github.io/ltex)

## 4.9.3 (May 7, 2020)

- &#x1f527; *Change:* Revert to Java 8
- &#x1f5d1; *Removal:* Remove support for external LanguageTool HTTP servers

## 4.9.2 (May 6, 2020)

- &#x1f527; *Change:* Update required version of Java (now 11 or newer)
- &#x2728; *New:* Add support for external LanguageTool HTTP servers &#x2014; [vscode-ltex#36](https://github.com/valentjn/vscode-ltex/issues/36)
- &#x2728; *New:* Add support for `\autoref`, `\pageref`, `\autopageref` &#x2014; [vscode-ltex#37](https://github.com/valentjn/vscode-ltex/issues/37)

## 4.9.1 (May 1, 2020)

- &#x1f41b; *Bug fix:* Fix sentence cache was invalidated when a single ignore sentence rule was present &#x2014; [vscode-ltex#29](https://github.com/valentjn/vscode-ltex/issues/29)
- &#x1f527; *Change:* Use thin non-breaking space for `\,` &#x2014; [vscode-ltex#35](https://github.com/valentjn/vscode-ltex/issues/35)

## 4.9.0 (March 28, 2020)

- &#x1f527; *Change:* Update LanguageTool to 4.9 (see [LT 4.9 release notes](https://github.com/languagetool-org/languagetool/blob/v4.9/languagetool-standalone/CHANGES.md#49-2020-03-24))
- &#x1f527; *Change:* Update other Java dependencies
- &#x1f527; *Change:* Reduce file size (omitting unneeded dependencies)

## 4.7.10 (March 12, 2020)

- &#x1f41b; *Bug fix:* Fix spelling errors for French dummies &#x2014; [vscode-ltex#27](https://github.com/valentjn/vscode-ltex/issues/27)
- &#x1f41b; *Bug fix:* Fix `\dots` in math mode being interpreted as `...`

## 4.7.9 (February 29, 2020)

- &#x1f527; *Change:* Update Markdown parser Flexmark to 0.60.2; this increases the speed of parsing Markdown
- &#x2728; *New:* Add possibility to ignore Markdown elements or replace them by dummy words via `ltex.markdown.ignore` and `ltex.markdown.dummy` &#x2014; [vscode-ltex#26](https://github.com/valentjn/vscode-ltex/issues/26)
- &#x1f527; *Change:* Ignore Markdown code blocks by default
- &#x1f527; *Change:* Replace auto-links and inline Markdown code with dummy words by default
- &#x1f41b; *Bug fix:* Fix match positions were sometimes off by one, especially in Markdown documents
- &#x1f527; *Change:* Rewrite `MarkdownAnnotatedTextBuilder`

## 4.7.8 (February 16, 2020)

- &#x2728; *New:* Add support for R Sweave `.rnw` files &#x2014; [vscode-ltex#22](https://github.com/valentjn/vscode-ltex/issues/22)
- &#x1f527; *Change:* Enable fixing multiple diagnostics at once &#x2014; [vscode-ltex#23](https://github.com/valentjn/vscode-ltex/issues/23)
- &#x2728; *New:* Add support for `\euro` &#x2014; [vscode-ltex#25](https://github.com/valentjn/vscode-ltex/issues/25)

## 4.7.7 (November 23, 2019)

- &#x1f527; *Change:* No changes, dummy release

## 4.7.6 (November 10, 2019)

- &#x2728; *New:* Add `ltex.performance` settings to give users more control over Java's RAM usage
- &#x1f527; *Change:* Change default initial Java heap size to 64 MB
- &#x1f527; *Change:* Change default maximum Java heap size to 512 MB
- &#x1f527; *Change:* Change default sentence cache size from 10000 to 2000 sentences

## 4.7.5 (October 22, 2019)

- &#x1f527; *Change:* Enable ignoring environments such as `lstlisting` and `verbatim`
- &#x2728; *New:* Add `ltex.environments.ignore` setting for defining own environments to ignore

## 4.7.4 (October 15, 2019)

- &#x2728; *New:* Add `disabledRules` and `enabledRules` settings (requires update of language extensions)
- &#x2728; *New:* Add `disable rule` quick fix
- &#x1f41b; *Bug fix:* Fix a bug where the `codeAction` request gets stuck in infinite loop
- &#x1f41b; *Bug fix:* Fix another `NullPointerException` for word2vec

## 4.7.3 (October 7, 2019)

- &#x1f41b; *Bug fix:* Fix null pointer error for word2vec quick fixes &#x2014; [vscode-ltex#12](https://github.com/valentjn/vscode-ltex/issues/12)

## 4.7.2 (October 2, 2019)

- &#x2728; *New:* Add missing error message if legacy false friends could not be loaded

## 4.7.1 (October 2, 2019)

- &#x2728; *New:* Add [`ltex.additionalRules.motherTongue`](../settings.html#ltexadditionalrulesmothertongue) setting to enable detection of false friends &#x2014; [vscode-ltex#11](https://github.com/valentjn/vscode-ltex/issues/11)
- &#x1f527; *Change:* Change defaults for `ltex.additionalRules` settings from `""` to `null`

## 4.7.0 (October 1, 2019)

- &#x1f527; *Change:* Update LanguageTool to 4.7 (see [LT 4.7 release notes](https://github.com/languagetool-org/languagetool/blob/v4.7/languagetool-standalone/CHANGES.md#47-2019-09-28))
- &#x2728; *New:* Support multi-root workspaces, all configuration settings except [`ltex.enabled`](../settings.html#ltexenabled) are now resource-specific &#x2014; [vscode-ltex#7](https://github.com/valentjn/vscode-ltex/issues/7)
- &#x1f527; *Change:* Save dictionary settings under full language short code (e.g., `en-US` instead of `en`). If you already have a dictionary under `ltex.en.dictionary` and use `en-US` as language (not `en`), you have to rename the settings name to `ltex.en-US.dictionary` (similarly for other languages).
- &#x1f5d1; *Removal:* Remove diagnostics when a file is closed
- &#x1f41b; *Bug fix:* Prevent insertion of text in TikZ mode
- &#x2728; *New:* Add support for more commands such as `\newenvironment`, `\newgeometry`, and `\pagenumbering`

## 4.6.13 (September 26, 2019)

- &#x1f41b; *Bug fix:* Fix LTeX LS not reinitialized after a language extension has been installed (which was missing during initialization)

## 4.6.12 (September 25, 2019)

- &#x1f41b; *Bug fix:* Patch LanguageTool's `AnnotatedText` with linear interpolation to hopefully fix the `fromPos must be less than toPos` LT errors for good
- &#x1f41b; *Bug fix:* Fix `\footnote` in math mode messed up text mode and math mode
- &#x1f527; *Change:* Increase robustness in case locale or settings are not provided
- &#x1f527; *Change:* Ignore all brace and bracket arguments after `\begin{environment}` (`tabular`, `array`, etc.)
- &#x2728; *New:* Add support for some more commands and environments such as `\pagestyle` and `eqnarray`

## 4.6.11 (September 23, 2019)

- &#x1f41b; *Bug fix:* Detect and prevent infinite loops in `LatexAnnotatedTextBuilder`
- &#x1f41b; *Bug fix:* Fix infinite loop with other line endings than `\n`
- &#x1f41b; *Bug fix:* Fix some more `fromPos must be less than toPos` LT errors
- &#x1f527; *Change:* Check for interrupts to avoid 100% CPU usage on timeout (this doesn't fix any bugs though)
- &#x2728; *New:* Add support for `\email`, `\href`, and `\verb|...|`
- &#x2728; *New:* Add support for more citation commands (`\citep`, `\citet`, etc.)
- &#x2728; *New:* Add support for float/theorem definition commands and starred sectioning commands

## 4.6.10 (September 18, 2019)

- &#x1f41b; *Bug fix:* Fix `NullPointerException` if LanguageTool has not been initialized &#x2014; [#1](https://github.com/valentjn/ltex/issues/1)

## 4.6.9 (September 8, 2019)

- &#x1f41b; *Bug fix:* Fix `NullPointerException` in `main`

## 4.6.8 (September 7, 2019)

- &#x2728; *New:* Initial release
