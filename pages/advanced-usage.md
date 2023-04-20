---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Advanced Usage"
permalink: "/advanced-usage.html"
sidebar: "sidebar"
---

## Magic Comments

Magic comments are special comments which contents are interpreted by LTeX and which can be used to change some LTeX settings in the middle of the document. The accepted syntax depends on the language and is shown in the following list. Except when otherwise noted, magic comments have to be on their own line, and they can be surrounded by whitespace.

- BibTeX: Same as LaTeX
- LaTeX: `% LTeX: SETTINGS`
- Markdown: One of the following:
  - `<!-- LTeX: SETTINGS -->`
  - `[comment]: <> "LTeX: SETTINGS"`
- Org: `# LTeX: SETTINGS`
- reStructuredText: `.. LTeX: SETTINGS`
- R Sweave: Same as LaTeX
- XHTML: No support for magic comments
- Programming languages: `LTeX: SETTINGS` inside a line comment or a single-line block comment

Magic comments are case-insensitive (except for the setting values), and the spaces in the magic comment line can be any amount of whitespace, even no amount at all.

`SETTINGS` has to be replaced with a whitespace-separated list of `KEY=VALUE` pairs. Neither `KEY` nor `VALUE` are enclosed in quotation marks. The following settings are supported:

- `enabled`: One of `true` or `false`. Makes it possible to disable LTeX for the rest of the document, or to enable it again.

  *Example:* `enabled=false`

- `language`: Changes the value of [`ltex.language`](settings.html#ltexlanguage) for the rest of the document.

  *Example:* `language=de-DE`

## Multilingual LaTeX Documents with the babel Package

While magic comments can be used to switch languages in a LaTeX document, this only makes sense for long parts of text. If you just want to use few words from another language, using magic comments can be cumbersome.

The preferred way of having multiple languages in one LaTeX document is using the [babel package](https://ctan.org/pkg/babel). This statement even holds if you don't use LTeX, as otherwise hyphenation and other language-specific aspects will be wrong in your typeset document. For instance, some words that exist in both English and German are hyphenated differently, depending on which language is used (example: `ham·​burg·​er` vs. `Ham·​bur·​ger`).

LTeX supports automatically switching its [`ltex.language`](settings.html#ltexlanguage) setting for a number of basic babel commands and environments. These are:

- `\usepackage[LANGUAGE]{babel}`: Switches the language for the rest of the document.
- `\selectlanguage{LANGUAGE}`: Switches the language for the rest of the document.
- `\foreignlanguage{LANGUAGE}{TEXT}`: Switches the language for the contents `TEXT` of the last argument.
- `\begin{otherlanguage}{LANGUAGE}TEXT\end{otherlanguage}`: Switches the language for the contents `TEXT` of the environment.

Here, `LANGUAGE` is one of babel's language names like `english`, `american`, `ngerman`, etc. Refer to the [babel manual](https://ctan.org/pkg/babel) for a list of possible language names. Keep in mind that not all languages supported by LTeX are supported by babel, and vice versa.

For the first point of the list, multiple comma-separated babel package options are allowed instead of just one `LANGUAGE`. If you specify multiple languages in the package options, e.g., `\usepackage[american,ngerman]{babel}` (since your document is multilingual), then babel and LTeX will default to the language that is mentioned last.

In addition, as the commands and environments given above are quite long, LTeX supports the following shortcuts:

- `\textLANGUAGETAG{TEXT}`: Short version of `\foreignlanguage{LANGUAGE}{TEXT}`.
- `\begin{LANGUAGETAG}TEXT\end{LANGUAGETAG}`: Short version of `\begin{otherlanguage}{LANGUAGE}TEXT\end{otherlanguage}`.

`LANGUAGETAG` can be any of the following:

- A language name like `english`, `american`, `ngerman`.
- A language short code like `en-US` or `de-DE` (see [`ltex.language`](settings.html#ltexlanguage)).
- A language short code with dashes removed. `\textLANGUAGETAG` only works without dashes (`\textenUS`).

In order for babel to recognize the shortcuts, you have to use the `\babeltags` command in the form `\babeltags{LANGUAGETAG1=LANGUAGE1, LANGUAGETAG2=LANGUAGE2, ...}` (e.g., `\babeltags{enUS=american, de-DE=ngerman, french=french}`). The `\babeltags` command should be in your preamble, and it's not required that it's in the same document as the text to be checked.

As `it` (Italian) and `sl` (Slovene) would lead to `\textit` and `\textsl`, which are already taken by LaTeX, these two language short codes are not supported. In this case, you have to resort to using the language names `italian` and `slovene`.

Please note the following caveat: Similarly to magic comments, LTeX only switches languages for the rest of the file that contains the babel commands. There is no inheritance for files that are included, e.g., via `\input` or `\include`. This is because LTeX is a file-based checker and has no notion of “LaTeX projects” that comprise multiple TeX files. In particular, `\usepackage[LANGUAGE]{babel}` will not switch languages if your preamble is in a different file than your text. In this case, use one of the other supported babel commands.

## Set Language in Markdown with YAML Front Matter

In Markdown, LTeX supports setting its [`ltex.language`](settings.html#ltexlanguage) setting with [Pandoc's language variable `lang`](https://pandoc.org/MANUAL.html#language-variables) in YAML front matter.

To use this, start your Markdown document with YAML front matter and include a variable named `lang`:

```markdown
---
lang: LANGUAGE
---
```

`LANGUAGE` is a language short code supported by [`ltex.language`](settings.html#ltexlanguage).

## Hiding False Positives with Regular Expressions

It's possible to use [`ltex.hiddenFalsePositives`](settings.html#ltexhiddenfalsepositives) to make LTeX hide false positives based on regular expressions.

The recommended way of using [`ltex.hiddenFalsePositives`](settings.html#ltexhiddenfalsepositives) is via the `Hide false positive` quick fix. This will add a JSON string containing the ID of the LanguageTool rule and the “sentence” to [`ltex.hiddenFalsePositives`](settings.html#ltexhiddenfalsepositives). LanguageTool internally splits every document into “sentences,” based on language-dependent rules (usually punctuation).

If you want to hide sentences based on a general pattern, you can add JSON strings with rule/sentence pairs yourself to [`ltex.hiddenFalsePositives`](settings.html#ltexhiddenfalsepositives). The format of the JSON string is documented in the description of the setting.

The sentence in the JSON string is a [Java-compatible regular expression](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html). Note that you have to replace all backslashes `\` in the regular expression with four backslashes `\\\\` as the JSON string will be parsed twice, once by the editor to read the JSON settings and once by LTeX to parse the JSON string itself.

In addition, note that if you wanted to match a literal backslash `\` in your regular expression, without the JSON escaping, you would have to use two backslashes `\\` due to the regular expression parser. Therefore, together with the JSON escaping, you actually have to use eight backslashes `\\\\\\\\` in total in your `settings.json` if you want to match a literal backslash. (In contrast, four backslashes are used, for instance, if you want to match the newline character `\n` as the backslash in there is not a literal backslash.)

Hiding false positives with [`ltex.hiddenFalsePositives`](settings.html#ltexhiddenfalsepositives) has the following caveats:

- Checking whether a match returned by LanguageTool is a false positive happens after the document has been converted from LaTeX, Markdown, etc. to plain text by LTeX. LanguageTool only returns the plain text sentence, but not the corresponding sentence in the original code. Therefore, the regular expression is matched against the plain text, not the original code. For instance, it's not possible to have a regular expression that matches all sentences that contain a specific LaTeX command.
- Checking whether a match returned by LanguageTool is a false positive happens after the document has been split into sentences. Therefore, it's not possible to have regular expressions that span multiple sentences.

## LanguageTool HTTP Servers and Using LanguageTool Premium

Although LTeX ships with its own version of LanguageTool (LT), it's possible to run LT independently of LTeX and have LTeX communicate with [LT via HTTP](https://dev.languagetool.org/http-server). There are multiple scenarios in which this might be useful:

- You want to run your own LT HTTP server, usually on `localhost`. This might be because the version of LT that comes with LTeX does not work, because you want to use an older or newer version of LT than LTeX's LT, or because you use other programs that use LT as well and you only want one instance of LT running.
- You want to use [LanguageTool Premium](https://languagetool.com/premium), the paid version of LT. In this case, you need to set [`ltex.languageToolHttpServerUri`](settings.html#ltexlanguagetoolhttpserveruri) to `https://api.languagetoolplus.com/`, [`ltex.languageToolOrg.username`](settings.html#ltexlanguagetoolusername) to your username/email, and [`ltex.languageToolOrg.apiKey`](settings.html#ltexlanguagetoolapikey) to your [API key](https://languagetool.org/editor/settings/access-tokens).

To connect to an LT HTTP server, set the setting [`ltex.languageToolHttpServerUri`](settings.html#ltexlanguagetoolhttpserveruri) to the root URI of the server, for instance, `http://localhost:8081/`. Note that in this mode, LTeX will still depend on ltex-ls and Java, as the interface for communicating with LT over HTTP is in ltex-ls.
