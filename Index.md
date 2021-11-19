# Shell commands - Documentation
*Shell commands* is a community plugin for [Obsidian.md Markdown editor](https://obsidian.md). It's purpose is to make it possible to execute system commands from within Obsidian (the same commands that you can execute in a [terminal](https://en.wikipedia.org/wiki/Terminal_emulator)).

The plugin's development can be followed in [Taitava/obsidian-shellcommands GitHub repository](https://en.wikipedia.org/wiki/Terminal_emulator).

## Who is this plugin for, and the expected skill level
This plugin is aimed for people who **want to**:
- Launch external applications - with a possibility to make them use Obsidian vault's files and folders.
- Create commands for automatic creation, modification and/or deletion of files and folders in the vault.
- Use certain content related information as part of their commands, e.g. the *name*, *title* or *tags* of the currently open file, or currently selected text, or text present in the clipboard. (These are called [[Variables|{{variables}}]]).

... and people who **know how**:
- To use some basic shell commands in a terminal.
- To identify commands that are safe to execute. Or rather: do not use a command whose meaning is not completely recognized.

## Basic usage

### First things first
- [[Example shell commands]]: Sources of ideas for what you can achieve with this plugin. Modify and make them fit your particular needs.
- [[Output channels]]: Where to put possible text outputted by your commands: in a notification balloon, status bar, in the currently open file, in the clipboard, or just ignore.

### Variables
- [[Variables - general principles]]: How to pass vault related information to your commands.
- [[Escaping special characters in variable values]]: Using variables safely.

## Advanced features
You will probably not need to look at these features in the beginning. These might come in handy in some use-cases, though.

### Output
- [[Ignoring errors]]

### Operating systems and shells
- [[Choosing a shell to execute commands in]]
- [[How to know which shell is used]]
- [[Operating system specific versions of shell commands]]

## Installation
See [installation instructions in the plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands#installation--usage).