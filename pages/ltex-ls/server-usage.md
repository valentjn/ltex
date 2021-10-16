---
# Copyright (C) 2019-2021 Julian Valentin, LTeX Development Community
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

title: "Server Usage"
permalink: "/ltex-ls/server-usage.html"
sidebar: "sidebar"
---

## Startup

It is recommended to use the startup scripts `bin/ltex-ls` (Linux, Mac) and `bin\ltex-ls.bat` (Windows) to start LTeX LS. These scripts are only part of the released versions (they are not contained in the source repository).

The startup scripts can be controlled by the following environment variables:

- `JAVA_HOME`: Path to the directory of the Java distribution to use (contains `bin`, `lib`, and other subdirectories). If set, this overrides the included Java distribution when using a platform-dependent LTeX LS archive.
- `JAVA_OPTS`: Java arguments to be fed to `java` (e.g., `-Xmx1024m`)

It is also possible to start LTeX LS directly without the startup scripts (not recommended).

### Command-Line Arguments

Any command-line arguments supplied to the startup scripts are processed by LTeX LS itself. The possible arguments are as follows:

- `--[no-]endless`: Keep the server alive when the client terminates the connection to allow reuse by the next client.
- `-h`, `--help`: Show help message and exit.
- `--host=<host>`: Listen for TCP connections on host `<host>` (IP address or hostname; default is `localhost`). Only relevant if server type is `tcpSocket`.
- `--log-file=<logFile>`: Tee server/client communication and server log to `<logFile>`. `${PID}` is replaced by the process ID of LTeX LS. The parent directory of `<logFile>` must exist. If `<logFile>` is an existing directory, then `ltex-ls-${PID}.log` is used as filename.
- `--port=<port>`: Listen for TCP connections on port `<port>`. Only relevant if server type is `tcpSocket`. A value of `0` (default) will have the system automatically determine a free port (the actual port number will be printed to the log).
- `--server-type=<serverType>`: Run the server as type `<serverType>`. Valid values are:
  - `standardStream` (default): Communicate with clients over standard input and standard output.
  - `tcpSocket`: Communicate with clients over a TCP socket.
- `-V`, `--version`: Print version information as JSON to the standard output and exit. The format is a JSON object with `"java"` and `"ltex-ls"` keys and string values. A key may be missing if no information about the corresponding version could be retrieved.

Instead of using the equals sign `=` to separate option names and values, it is also possible to use one or more spaces.

### Exit Codes

- 0: LTeX LS exited successfully.
- 1: An exception was thrown during the execution of LTeX LS.
- 2: An invalid command-line argument was supplied to LTeX LS.

## Checking Documents with the LSP

Once started, the language server may be used according to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/) to check documents.

Communication with the server is by default via standard input and standard output (except when the server type is `tcpSocket`). Logging messages are always printed to the standard error output.

## Settings

See the [list of all supported settings](../settings.html). Note that some settings are client-specific, i.e., they only affect vscode-ltex and coc-ltex.

## Quick Fixes

- `quickfix.ltex.acceptSuggestions`: Replace the text of the diagnostic with the specified suggestion.
- `quickfix.ltex.addToDictionary`: Trigger the `_ltex.addToDictionary` command.
- `quickfix.ltex.disableRules`: Trigger the `_ltex.disableRules` command.
- `quickfix.ltex.hideFalsePositives`: Trigger the `_ltex.hideFalsePositives` command.

## Commands

Some commands are handled by LTeX LS, while others must be handled by the language client. This is in contrast to the [LSP specification](https://microsoft.github.io/language-server-protocol/specification), which recommends that the server handles all commands. However, handling of some commands by the client is necessary as these commands change the client configuration, which the LSP does not allow server-side.

All commands are prefixed with `_ltex.` during usage. The purpose of the leading underscore is that in some clients, commands are directly exposed to the user of the client (e.g., for assigning keyboard shortcuts), which is not desirable for internal commands that require arguments. The leading underscore signals that the commands are internal.

As arguments, all commands take an array with exactly one element, whose type is specified by the respective `CommandParams` interface.

The result of all commands handled by the client is `null`.

The result of all commands handled by the server implements at least the following interface:

```typescript
interface ServerCommandResult {
  /**
   * Whether the command was executed successfully.
   */
  success: boolean;

  /**
   * Optional error message if `success` is `false`.
   */
  errorMessage?: string;
}
```

### `_ltex.addToDictionary` (Client)

`_ltex.addToDictionary` is executed by the client when it should add words to the dictionary by adding them to [`ltex.dictionary`](../settings.html#ltexdictionary).

```typescript
interface AddToDictionaryCommandParams {
  /**
   * URI of the document.
   */
  uri: string;

  /**
   * Words to add to the dictionary, specified as lists of strings by language.
   */
  words: {
    [language: string]: string[];
  };
}

type AddToDictionaryCommandResult = null;
```

### `_ltex.disableRules` (Client)

`_ltex.disableRules` is executed by the client when it should disable rules by adding the rule IDs to [`ltex.disabledRules`](../settings.html#ltexdisabledrules).

```typescript
interface DisableRulesCommandParams {
  /**
   * URI of the document.
   */
  uri: string;

  /**
   * IDs of the LanguageTool rules to disable, specified as lists of strings by language.
   */
  ruleIds: {
    [language: string]: string[];
  };
}

type DisableRulesCommandResult = null;
```

### `_ltex.hideFalsePositives` (Client)

`_ltex.hideFalsePositives` is executed by the client when it should hide false positives by adding them to [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives).

```typescript
interface HideFalsePositivesCommandParams {
  /**
   * URI of the document.
   */
  uri: string;

  /**
   * False positives to hide, specified as lists of JSON strings by language.
   */
  falsePositives: {
    [language: string]: string[];
  };
}

type HideFalsePositivesCommandResult = null;
```

### `_ltex.checkDocument` (Server)

`_ltex.checkDocument` is executed by the server to trigger the check of a specific document. The result will be sent to the client with a `textDocument/publishDiagnostics` notification.

```typescript
interface CheckDocumentCommandParams {
  /**
   * URI of the document.
   */
  uri: string;

  /**
   * Code language ID of the document (e.g., `latex`). Will be determined by the file extension
   * of `uri` if missing.
   */
  codeLanguageId?: string;

  /**
   * Text to check. Will be determined as the contents of the file at `uri` if missing.
   */
  text?: string;

  /**
   * Range inside `text` (or the contents of the file at `uri` if missing) if only a part
   * of the document should be checked. Will be set to the range spanning all of `text` if missing.
   */
  range?: Range;
}

type CheckDocumentCommandResult = ServerCommandResult;
```

### `_ltex.getServerStatus` (Server)

`_ltex.getServerStatus` is executed by the server to return information about the current resource consumption of LTeX LS. Some information might not be available.

```typescript
type GetServerStatusCommandParams = null;

interface GetServerStatusCommandResult extends ServerCommandResult {
  /**
   * Process ID of the Java process.
   */
  processId: number;

  /**
   * Wall-clock duration in seconds since the start of LTeX LS.
   */
  wallClockDuration: number;

  /**
   * Current CPU usage as a fraction between 0 and 1.
   */
  cpuUsage?: number;

  /**
   * Duration in seconds during which the CPU was occupied.
   */
  cpuDuration?: number;

  /**
   * Memory in bytes of all currently allocated Java objects (this is a part of `totalMemory`).
   */
  usedMemory: number;

  /**
   * Total memory in bytes currently taken by the JVM.
   */
  totalMemory: number;

  /**
   * Whether LTeX LS is currently busy checking text.
   */
  isChecking: boolean;

  /**
   * URI of the document currently being checked.
   * This field may still be missing even if `isChecking` is true.
   */
  documentUriBeingChecked?: string;
}
```

## Custom LSP Extensions

LTeX LS supports the following custom features that are not specified by the LSP:

- Custom initialization options
- Custom requests and notifications

To use custom LSP extensions, the client has to pass a `CustomInitializationOptions` object to the `InitializeParams.initializationOptions` field when sending the [`initialize`](https://microsoft.github.io/language-server-protocol/specification#initialize) request. If no such object is passed, LTeX LS will fall back to an LSP-compliant mode and not use any custom LSP extensions.

### Custom Initialization Options

Custom initialization options are directly specified in the fields of a `CustomInitializationOptions` object defined as follows:

```typescript
interface CustomInitializationOptions {
  /**
   * Possibility to supply the locale of the client, if LSP 3.15 is used.
   * For LSP 3.16 and later, use `InitializeParams.locale` instead.
   * @deprecated This will be removed once LTeX LS requires LSP 3.16.
   */
  locale?: string;

  /**
   * Capabilities for custom requests and notifications.
   */
  customCapabilities?: CustomCapabilities;
}

interface CustomCapabilities {
  /**
   * Whether `ltex/workspaceSpecificConfiguration` requests are supported.
   */
  workspaceSpecificConfiguration?: boolean;
}
```

### Custom Requests and Notifications

Support for custom server-to-client requests and notifications has to be announced by setting the value that corresponds to the name of the custom request or notification in `CustomInitializationOptions.customCapabilities` to `true`. Client-to-server requests and notifications are always enabled.

All custom requests and notifications are prefixed with `ltex/` during usage.

#### `ltex/workspaceSpecificConfiguration` (⮎)

`ltex/workspaceSpecificConfiguration` is a server-to-client request. Parameters and result are exactly like [`workspace/configuration`](https://microsoft.github.io/language-server-protocol/specification#workspace_configuration) (i.e., `ConfigurationParams` and `any[]`, respectively).

If enabled, LTeX LS will not only send a [`workspace/configuration`](https://microsoft.github.io/language-server-protocol/specification#workspace_configuration) request to the client every time a document is checked, but also an `ltex/workspaceSpecificConfiguration` request. Some settings used for the check are then taken from the result of the `ltex/workspaceSpecificConfiguration` request instead of the [`workspace/configuration`](https://microsoft.github.io/language-server-protocol/specification#workspace_configuration) request. These settings are:

- [`ltex.dictionary`](../settings.html#ltexdictionary)
- [`ltex.disabledRules`](../settings.html#ltexdisabledrules)
- [`ltex.enabledRules`](../settings.html#ltexenabledrules)
- [`ltex.hiddenFalsePositives`](../settings.html#ltexhiddenfalsepositives)

The reason of the existence of `ltex/workspaceSpecificConfiguration` is that some clients like VS Code have different configuration scopes (e.g., user and workspace). When a configuration like [`ltex.dictionary`](../settings.html#ltexdictionary) appears in multiple scopes, the value in the scope with the higher precedence will override the other values (e.g., workspace scope will override user scope). `ltex/workspaceSpecificConfiguration` makes it possible for the client to implement a merging mechanism instead, without having to change [`workspace/configuration`](https://microsoft.github.io/language-server-protocol/specification#workspace_configuration).
