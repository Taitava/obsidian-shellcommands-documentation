# Shell commands - Documentation
*Shell commands* is a community plugin for [Obsidian.md Markdown editor](https://obsidian.md). Its purpose is to make it possible to execute system commands from within Obsidian (the same commands that you can execute in a [terminal](https://en.wikipedia.org/wiki/Terminal_emulator)).

The plugin's development can be followed in [Taitava/obsidian-shellcommands GitHub repository](https://github.com/Taitava/obsidian-shellcommands).

## Who is this plugin for, and the expected skill level
This plugin is aimed for people who **want to**:
- Launch external applications - with a possibility to make them use Obsidian vault's files and folders.
- Create commands for automatic creation, modification and/or deletion of files and folders in the vault.
- Use certain content related information as part of their commands, e.g. the *name*, *title* or *tags* of the currently open file, or currently selected text, or text present in the clipboard. (These are called [[Variables - general principles|{{variables}}]]).

... and people who **know**:
- How to use some basic shell commands in a terminal.
- How to identify commands that are safe to execute. Or rather: do not use a command whose meaning is not completely recognized.
- Approximately that there are different *shells* (e.g. Bash, Dash, Zsh, CMD, PowerShell 5 and PowerShell Core). You don't need to know all of them, but at least get to know [[Shells|what is your own shell]].

## Installation
See [installation instructions in the plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands#installation--usage).

[[Upgrading (and downgrading)|Upgrading instructions - and downgrading, if necessary]]

## Basic usage

### Defining your shell commands
- [[How to define shell commands]]: Start from this.
- [[Example shell commands]]: Sources of ideas for what you can achieve with this plugin. Modify and make them fit your particular needs.
- [[Output channels]]: Where to put possible text outputted by your commands: in a notification balloon, status bar, in the currently open file, in the clipboard, or just ignore.
- [[Working directory]]: Defining in which folder your shell commands will operate.

### Variables
- [[Variables - general principles]]: How to pass vault related information to your commands.
- [[Escaping special characters in variable values]]: Using variables safely.

### Execution
There are a few different ways to execute your shell commands:
- All shell commands can be executed via [Obsidian's command palette](https://help.obsidian.md/Plugins/Command+palette) (unless they are [[Events - general principles#^exlude-from-command-palette|excluded]]).
- You can assign keyboard hotkeys to shell commands. #TODO: Add instructions.
- [[Shell commands URI]] can be used to create custom links that execute your shell commands - both inside Obsidian notes, and externally from other applications.
- [[Events - general principles|Events]] can execute your shell commands automatically when certain things happen, e.g. when Obsidian starts or quits.

## Advanced features
You will probably not need to look at these features in the beginning. These might come in handy in some use-cases, though.

### Output
- [[Ignoring errors]]

### Preactions
Actions that are performed before executing a shell command, i.e. preparations.
- [[Prompts]]: Ask values from a user  ==This feature is only available in a [0.12.0-beta.1 test](https://github.com/Taitava/obsidian-shellcommands/discussions/201). #TODO: Remove this annotation when the final version is released.== 

### Variables
- ==These two features are only available in a [0.12.0-beta.1 test](https://github.com/Taitava/obsidian-shellcommands/discussions/201). #TODO: Remove this annotation when the final version is released.== 
- [[Custom variables]]
- [[Default values|Default values for variables]]

### Environments: Operating systems and shells
- [[Operating system specific versions of shell commands]]
- [[Shells]]

### Hidden settings
- [[Hidden settings|There are some minor settings that do not have a visible field in the settings user interface]]

## Improving the documentation
- For ideas on how to improve the documentation: [Create a new discussion in the *Shell commands* plugin's GitHub repository's *Ideas* discussion category](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas).
- For clear errors in the documentation (that are simple to fix): Change it yourself and [create a pull request in the documentation's GitHub repository](https://github.com/Taitava/obsidian-shellcommands-documentation/pulls). If you are unsure how to work with Git and how to make PRs, it's also okay to just create a new discussion.

All feedback and ideas are greatly appreciated! 🙂

## Screenshots in the documentation
The documentation is partly illustrated with screenshots. The screenshots may look different from how the plugin's user interface looks in your Obsidian, as you might use a different theme, a different color mode, a different version of Obsidian, and a different operating system.

The screenshots are taken in the following environment:
- Theme: [Red graphite](https://github.com/seanwcom/Red-Graphite-for-Obsidian)
- Color mode: Light (with dark contrast side panes, provided by *Red graphite*)
- Operating system: Windows

Also, some screenshots may be from older versions of SC, in case no significant changes have occurred, or if screenshots have been forgotten to update. You can see from which version of SC a particular screenshot has been taken from, by looking at which folder it resides in (e.g. `Assets/Images/SC 0.10.0 - Obsidian 0.13.23`).

![[Settings-main-shell-commands-tab.png]]
(An example screenshot from the main settings view of SC version `0.10.0`. You can tell it's taken on Windows, because the shell command previews show an escape character `` ` `` that is used by *PowerShell*, instead of `\`, that is used by e.g. *Bash* on Linux and Macintosh. Also, the hotkeys `Ctrl` + `G` and `Ctrl` + `Shift` + `G` indicate that the screenshot is not taken on Macintosh, which would have `Cmd` instead of `Ctrl`.)
