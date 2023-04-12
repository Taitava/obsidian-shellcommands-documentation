---
aliases:
 - "custom shell settings"
---
 > [!Warning] This feature is only available in a beta test
 > - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/108#discussioncomment-5277523).
 > %% #TODO: Remove this annotation when the final version is released. %%

# Configure a new _custom shell_

This page walks you through the general configuring process of creating a new [[Custom shells|custom shell]]. However, for a few specific shells, there are tailored guides available. If you happen to be configuring one of these, you can follow their specific instructions instead of reading this page:
![[Custom shells#^tailored-configuration-guides]]

In case you are configuring a shell not present in the list above, just continue following this general guide.

**To begin**, open up the settings panel in Obsidian by pressing the hotkey `Ctrl`/`Cmd` + `,` . Navigate to _Shell commands_ -> _Environments_ -> _Custom shells_. Click the _New custom shell_ button. A modal pops up, where you can configure the custom shell's options as described in the below subchapters.

![[Settings-main-environments-tab.png]]

## Shell name and description

![[Settings-Custom-shell-Shell-name-and-description.png]]
The name and description are freely decidable, as they do not affect the custom shell's operation in any way.

## Executable binary file path

![[Settings-Custom-shell-Executable-binary-file-path.png]]

This defines a program file that will be executed when a shell command needs to be run.

No [[Variables - general principles|{{variables}}]] are supported in this field.

> [!Question] Relative or absolute path?
> - It's recommended to enter an absolute path here, as it clarifies clearly which file will be used.
> - Relative paths are also supported, but they refer to the [Obsidian's system directory](https://help.obsidian.md/Advanced+topics/How+Obsidian+stores+data#System+directory), **not to the Obsidian vault**. The [[Working directory]] setting of this plugin **does not affect** the shell binary path.
> - The binary path can also be just a sole file name, if it's located in a directory that can be found in the [`PATH` environment variable](https://en.wikipedia.org/wiki/PATH_(variable)).
> 
> Terminology: A path is **absolute** if it starts with a slash `/` on macOS or Linux; or a letter and a colon `C:`, or with two backslashes `\\` on Windows. If it doesn't start with any of those, it's **relative**.

> [!Tip]- On Windows, a file _extension_ is optional
> If a binary file name has an <abbr title=".COM .EXE .BAT .CMD .VBS .VBE .JS .JSE .WSF .WSH .MSC .PY .PYW .CPL">executable file extension</abbr>, it can be left out. I.e. the following two examples work just the same:
>  - `C:\Windows\System32\wsl.exe` (normal, has a file extension)
>  - `C:\Windows\System32\wsl` (alternative, no file extension)
>  
>  However, for the sake of clarity, it's recommended to always include a file extension. This helps users reading the binary path setting to easily distinguish that it's a file instead of a folder.

## Shell arguments

![[Settings-custom-shell-shell-arguments.png]]

> [!Info] Arguments for custom shells
> Each shell defines arguments and options that control their behavior when they execute commands. The most important argument is the executable command itself.
> ^arguments-summary

Each shell has its own invocation options and arguments that are used to adjust the shell's behavior.
- Each option or argument should be defined on its own line in order to separate it from other options/arguments.
- When the shell is executed, the lines are gathered as an array (on Linux and macOS) or a single line string (on Windows), so the shell will **not** receive any of the newline characters that are used as argument separators here. Possible newlines coming from [[Variables - general principles|{{variable}} values]] or the shell command content are of course included, however.

> [!Info]- About the `{{!shell_command_content}}` variable
> - `{{!shell_command_content}}` is a placeholder that will be substituted with an executable shell command.
> - The preceding exclamation mark `!` means that special characters in the shell command are **not** [[Escaping special characters in variable values|escaped]]. However, the shell command's content may contain already escaped special characters originating from other [[Variables - general principles|{{variables}}]]. Using `!` avoids adding double escaping, but does not remove prior escaping.
> - `{{!shell_command_content}}` is used in two fields in custom shell settings:
>     - [[Settings for custom shells#Shell arguments|Shell arguments]]: Denotes a place where a command (together with a possible _wrapper_) is placed when invoking a shell. **(Mandatory).**
>     - [[Settings for custom shells#Wrapper for shell command|Wrapper for shell command]]: Denotes a place where a command is placed when being surrounded with extra commands. **(Optional).**
> - In special cases, `{{!shell_command_content}}` (or `{{shell_command_content}}`) can be used multiple times to repeat a shell command.
> - [[{{shell_command_content}}|More information about the {{shell_command_content}} variable.]]
> ^about-shell-command-content

## Host operating system

![[Settings-Custom-shell-Host-operating-system.png]]

The _Host operating system_ setting defines an operating system that your computer must be currently running in order to use this shell. It's a bit "dummy" setting, because you probably never need to change it, as it defaults to the current operating system when creating a new custom shell.

This setting mainly affects the settings user interface by deciding on what operating system's shell selection menu the custom shell will appear in.

However, in case you synchronize your vault between multiple computers that have different operating system, you have the opportunity to define custom shell settings also for shells that you plan to use on your other computers. You just can't test the execution in practise when configuring a shell that is designed for another operating system.

### Windows: Quote shell arguments
Like mentioned in the screenshot, on Windows, this setting _wraps shell arguments in double quotes `"` **if** they contain spaces_. Possibly pre-existing double quotes `"` are escaped by preceding them with a backslash: `\"`.
 - Some shells expect this kind of quoting (e.g. [[CMD.EXE]]).
 - However, there are other shells that are not designed to parse any wrapping quotes, so they will probably interpret quoted arguments incorrectly.
 - If you are on Windows, you just need to try it out: If your shell gives you weird error messages claiming that a command does not exist, try to toggle this setting from on to off, or vice-versa.
 - If you are on some other platform, this quoting is never done, and there's no way nor any reason to enable it. Lucky you - less confusing settings to think about!

> [!Info]- Background: The shell argument quoting feature comes from `Node.js`
> Unlike [[Escaping special characters in variable values|escaping special characters in {{variable}} values]], this quoting feature is **not** developed in the source code of the _Shell commands_ plugin. Instead, it comes from Node.js's `child_process` module, and is operated by an option named [`windowsVerbatimArguments`](https://nodejs.org/api/child_process.html#child_processspawncommand-args-options):
> - When _Quote shell arguments_ is **off**, `windowsVerbatimArguments` is set to `true`.
> - When _Quote shell arguments_ is **on**, `windowsVerbatimArguments` is set to `false`.
> - So the setting's terminological logic is inverted.
> 
> > [!Quote] The behavior of `windowsVerbatimArguments` when it's `true` (i.e. when _Quote shell arguments_ is _off_), as described in [Node.js's `child_process` documentation](https://nodejs.org/api/child_process.html#child_processspawncommand-args-options) 
> > `windowsVerbatimArguments` `<boolean>` No quoting or escaping of arguments is done on Windows. Ignored on Unix.

## Shell's operating system

![[Settings-Custom-shell-Shells-operating-system.png]]

The _Shell's operating system_ gives an insight to how certain structures work in the shell, in case they differ from the [[#Host operating system]]. It's currently only used for determining a correct directory separator when [[Variables - general principles|{{variables}}]] return file/folder paths. I.e. `\` for Windows, and `/` for Linux and macOS. Other uses might be implemented later, if needed.

## Special characters escaping

![[Settings-Custom-shell-Special-characters-escaping.png]]

When [[Variables - general principles|{{variables}}]] are used in shell commands (or in some settings for custom shells), [[Escaping special characters in variable values|special characters in their values are usually escaped]]. In this setting, you can select the desired escaping mechanism according to what your shell understands and interprets correctly:
 - _Unix shell style with `\` as escape character_: Select this, if the shell is one of (or similar to): [[Bash]], [[Dash]], or [[Zsh]]. This will precede e.g. a double quote `"` with a backslash: `\"`
 - _PowerShell style with `` ` `` as escape character_: Select this, if using PowerShell. This will precede e.g. a double quote `"` with a backtick: `` `" ``
 - _No escaping (not recommended)_: If the shell's escaping character is different from a backslash `\` or a backtick `` ` ``, or both escapers produce otherwise incompatible values for the shell, you might decide to disable the escaping altogether. Just keep in mind that [[Escaping special characters in variable values#^dangerous-special-characters|unescaped special characters can be dangerous]], if they occur in wrong places.

## Path translator

![[Settings-Custom-shell-Path-translator.png]]

If the [[#Shell's operating system]] differs from the [[#Host operating system]], a _Path translator_ should be written in a form of a JavaScript function, so that your main operating system's file paths get converted to a structure that works in your shell.

After you've written a path translator, test that it works by clicking the _Test absolute path translation_ icon: ![[Translate-icon.png]]. It should show you three test paths that are translated using the function.

> [!Info] The file paths that need translating
> - Path translating is only applied for [[Variables - general principles|{{variables}}]] when they need to return a file path or a folder path.
> - Path translating might be extended to other features later, if needed.
> - Current working directory is not affected by the path translator, because it is assumed that shells do this translation by themselves.
> - Directories contained in the [`PATH` environment variable](https://en.wikipedia.org/wiki/PATH_(variable)) are also not affected by the path translator. Again, this is something the shell itself is assumed to handle.
> ^what-file-system-paths-are-translated

## Wrapper for shell command

![[Settings-custom-shell-wrapper-for-shell-command.png]]

> [!Info] A wrapper can add extra shell commands around the main command
> Each [[Custom shells|custom shell]] may optionally define a wrapper that consist of normal shell command expressions that prefix and/or postfix the actual shell command in order to perform some preparing and/or finishing tasks, such as:
>  - setting character encodings (prefix)
>  - adding directories to the `PATH` environment variable (prefix)
>  - storing executed shell commands in a log file (prefix/postfix)
>  - converting output from one format to another (postfix)
>  ^wrapper-summary

If you do define a wrapper, you need to include [[{{shell_command_content}}]] in the wrapper to denote a place where the main shell command will be inserted.

![[#^about-shell-command-content]]

## Execute a command to test the shell

![[Settings-Custom-shell-Execute-command-to-test-shell.png]]

Click the _Execute the test command using this shell_ icon button: ![[Execute-icon.png]]

## Make shell commands use the newly created shell

Now that the custom shell is configured, it still needs to be taken into use. There are two ways to select the shell:
 - **A**) a default shell can be selected for all shell commands that do not have an explicitly selected shell, or
 - **B)** a shell can be selected for each shell command individually.

> [!Info]- A) Select WSL as a _default_ shell
> You can follow this guide about finding out the current default shell. You can change the default shell there, too.
> ![[Shells#How to know which shell is used]]

> [!Info]- B) Select WSL for an individual shell command
> ![[Shells#Choosing a shell on a per shell command basis]]
> You can follow this guide about finding out the current default shell. You can change the default shell there, too.
> ![[Shells#How to know which shell is used]]


Now all the configuration should be complete. Try to execute your shell commands!

# History
> [!page-edit-history]- Page edit history: 2023-03-28 &#10132; 2023-04-10
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/47744de2b41b0ae2f44a8cbe83d4bcd0301bf3bc): [[Settings for custom shells.md]]: Add content.
> - [<small>2023-04-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0d3f39d1b90f015e834fe1471deb091e225f2c38): Settings for custom shells.md: Add "Shell name and description" section.
> - [<small>2023-03-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ac2b9e500546136d598346f559a1275dd7f749f7): Create draft `Settings for custom shells.md`, including screenshots.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Environments/Custom%20shells/Settings%20for%20custom%20shells.md).
> ^page-edit-history