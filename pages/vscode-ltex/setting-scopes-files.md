---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Setting Scopes &amp; Files"
permalink: "/vscode-ltex/setting-scopes-files.html"
sidebar: "sidebar"
---

## Multi-Scope Settings

Some of LTeX's settings are *multi-scope settings.* These settings are:

- [`ltex.dictionary`](../settings.html#ltexdictionary)
- [`ltex.disabledRules`](../settings.html#ltexdisabledrules)
- [`ltex.enabledRules`](../settings.html#ltexenabledrules)
- [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives)

To explain what multi-scope settings do, let us recap that VS Code has multiple scopes of settings:

- [User settings](https://code.visualstudio.com/docs/getstarted/settings) saved in the `settings.json` file of the user
- [Workspace settings](https://code.visualstudio.com/docs/getstarted/settings) saved in the `.vscode/settings.json` file of the workspace (or in the `*.code-workspace` file in the case of multi-root workspaces)
- [Workspace folder (resource-specific) settings](https://code.visualstudio.com/docs/editor/multi-root-workspaces#_settings) set in the `.vscode/settings.json` file of the workspace folder (or in the `.vscode/settings.json` file of the workspace in the case of single-folder workspaces)

If you set a setting in multiple scopes at the same time, the scope with higher precedence usually shadows the scope with lower precedence. For instance, it would be impossible to supply additional words for the dictionary in workspace settings to amend the user dictionary, as the workspace dictionary would shadow the user dictionary.

However, multi-scope settings are specially treated by LTeX. When checking text, LTeX implicitly joins the lists of these settings in user, workspace, and workspace folder scopes (in that order) to a single list. This means if your user dictionary contains just `cromulent` and your workspace dictionary contains just `B-spline`, then the dictionary used by LTeX will consist of `cromulent` *and* `B-spline` (i.e., not just `B-spline`).

If you want to remove an entry from a workspace-specific setting in a scope with higher precedence without removing it altogether, you can include it with a dash (`-`) as prefix. For example, if your user dictionary includes the word `cromulent`, but you want that word to be marked as a spelling error in a specific project, simply add `-cromulent` to [`ltex.dictionary`](../settings.html#ltexdictionary) in the project's workspace settings.

You can specify the target scope for changing settings with quick fixes (e.g., `Add to dictionary`) with the [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) setting.

## External Setting Files

*See also [“Where does vscode-ltex save its settings (e.g., dictionary, false positives)?”](../faq.html#where-does-vscode-ltex-save-its-settings-eg-dictionary-false-positives) in the FAQ.*

Some of LTeX's settings support settings in external files. These settings are:

- [`ltex.dictionary`](../settings.html#ltexdictionary)
- [`ltex.disabledRules`](../settings.html#ltexdisabledrules)
- [`ltex.enabledRules`](../settings.html#ltexenabledrules)
- [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives)

These settings contain lists (e.g., lists of words in the case of [`ltex.dictionary`](../settings.html#ltexdictionary)), which may be partly or fully put in external files. To do so, there are two options:

- Explicitly specify an external file
- Use one of LTeX's implicit defaults for external files

To use the first option and explicitly specify an external file, add the path of the external file with a colon (`:`) as prefix to the list (e.g., `:/path/to/externalFile.txt`). Each line of the file will be implicitly inserted as an entry into the value of the setting at the position where you specify the external file. External files must be in UTF-8 encoding.

A leading tilde (`~`) in the path is resolved with the home directory of the user. Relative paths are resolved relative to the `.vscode` directory in which you specify the external file, except for user settings, in which the path is resolved to the global storage path of the LTeX extension (this path is printed when using the [`LTeX: Show Status Information`](commands.html#ltex-show-status-information) command). If in doubt, use absolute paths instead.

The other option is using one of LTeX's implicit defaults for external files. The following files are automatically read (if existing). By default, all quick fixes such as `Add to dictionary` write into these files when being executed.

- `LTEX_GLOBAL_STORAGE_PATH/ltex.SETTING.LANGUAGE.txt`, where `LTEX_GLOBAL_STORAGE_PATH` is the global storage path of the LTeX extension
- `WORKSPACE/.vscode/ltex.SETTING.LANGUAGE.txt`, where `WORKSPACE` is the root directory of the opened workspace, if any
- `WORKSPACE_FOLDER/.vscode/ltex.SETTING.LANGUAGE.txt`, where `WORKSPACE_FOLDER` is the directory of the opened workspace folder, if any

`SETTING` is the name of the setting, and `LANGUAGE` is the language code (like in [`ltex.language`](../settings.html#ltexlanguage)), for example `ltex.dictionary.en-US.txt`. You can use the [`LTeX: Show Status Information`](commands.html#ltex-show-status-information) command to see the paths of these three directories. For examples, see [“Where does vscode-ltex save its settings (e.g., dictionary, false positives)?”](../faq.html#where-does-vscode-ltex-save-its-settings-eg-dictionary-false-positives) in the FAQ.

When executing a quick fix such as `Add to dictionary`, LTeX will do the following if the value of [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) ends with `ExternalFile` (which it does by default): First, retrieve the list of the setting corresponding to the quick fix and to the language of the text in which the quick fix was executed. Then, pick the first entry that explicitly specifies an external file (i.e., the first entry starting with `:`). If there is no such entry, the implicit default path (see above) is used. The resulting external file is then appended with the entry to be added by the quick fix. If the file doesn't exist, it will be created, along with all necessary parent directories, if any are missing.

The scope in which this procedure is applied is determined by the [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) setting, and by the relevant workspaces or workspace folders.

*Example:* [`ltex.configurationTarget`](../settings.html#ltexconfigurationtarget) is by default `workspaceFolderExternalFile` for `dictionary`. Therefore, when clicking `Add to dictionary` in an `en-US` document, LTeX will by default do the following:

1. If the document belongs to an open workspace folder:
   1. Retrieve the `en-US` part of the value of [`ltex.dictionary`](../settings.html#ltexdictionary) that is set in the workspace folder settings.
   2. Pick the first external file in that list. If there is none, choose `WORKSPACE_FOLDER/.vscode/ltex.dictionary.en-US.txt` (create the file if necessary).
   3. Append the file by the new word.
2. Otherwise, if the document belongs to an open workspace:
   1. Retrieve the `en-US` part of the value of [`ltex.dictionary`](../settings.html#ltexdictionary) that is set in the workspace settings.
   2. Pick the first external file in that list. If there is none, choose `WORKSPACE/.vscode/ltex.dictionary.en-US.txt` (create the file if necessary).
   3. Append the file by the new word.
3. Otherwise:
   1. Retrieve the `en-US` part of the value of [`ltex.dictionary`](../settings.html#ltexdictionary) that is set in the user settings.
   2. Pick the first external file in that list. If there is none, choose `LTEX_GLOBAL_STORAGE_PATH/ltex.dictionary.en-US.txt` (create the file if necessary).
   3. Append the file by the new word.
