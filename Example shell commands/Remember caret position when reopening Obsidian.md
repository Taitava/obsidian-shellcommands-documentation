---
cssclass: customiseTitle
---
# Example: Remember caret position when reopening Obsidian
This example shows you how to automatically store the current file's caret position in a file every time Obsidian quits, and then read it next time Obsidian starts.

The example is only meant for remembering the position for a single file when quitting/starting Obsidian. For an ability to remember caret positions when switching between files, I recommend you to take a look at the following community plugin for Obsidian: [Remember cursor position](https://github.com/dy-sh/obsidian-remember-cursor-position)  ([quick installation link](obsidian://show-plugin?id=remember-cursor-position)). It can also remember selections and multiple cursors per file.

This example is just meant for a fun do-it-yourself poor man's version of the said feature. 🙂

Remembering the caret position requires actually *two* shell commands:
- One for storing the caret position to a file when Obsidian quits.
- One for reading the caret position when Obsidian starts.

I'll first list the actual shell commands (dependent on your operating system) and after that I'll tell the common settings needed for the shell commands to work correctly.

## Windows
1. Shell command: `echo {{caret_position}} > caret_position.txt`
2. Shell command: ``Write-Host {{file_path:relative}}`: -NoNewLine; type caret_position.txt``

On Windows, the second shell command assumes you are using PowerShell instead of CMD. The first shell command should work ok both on PowerShell and CMD.

## Linux and macOS
1. Shell command: `echo {{caret_position}} > caret_position.txt`
2. Shell command: `echo -n {{file_path:relative}}\:; cat caret_position.txt`

## Common settings
1. For the first shell command:
	- Enable event [[Obsidian quits]]
	- (Optional) Define an alias: *Remember caret position*
	- (Optional) [[Events - general principles#^exlude-from-command-palette|Exclude the shell command from Obsidian's command palette]].
2. For the second shell command: 
	- Enable event [[Obsidian starts]]
	- Set `stdout` output channel to [[Output channel - Open files|Open a file]]
	- (Optional) Define an alias: *Restore caret position*
	- (Optional) [[Events - general principles#^exlude-from-command-palette|Exclude the shell command from Obsidian's command palette]].

The idea in the second shell command is to print out the current file's path together with the restored caret position numbers (line and column). Obsidian does open the last file during startup, but it does not remember the caret position. So we do not need to store the file name. The output channel [[Output channel - Open files|Open a file]] handles placing the caret in the position we want. It also needs the file name, although it's the same file that is already open.

You can change the `caret_position.txt` file name freely in the commands. For example, you can "hide" the file by using e.g. this instead: `.obsidian/caret_position.txt`.

# History


> [!page-edit-history]- Page edit history: 2022-03-05 &#10132; 2022-08-21
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5ad0dd8064c892901f885d7b2ab8037179f3c40d): Fix line endings.
> - [<small>2022-08-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c6f5146f8f90047f63fd90bfbe81f024d6513ea): Rename Output channel "Open a file" to "Open files".
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bcc0e63a8382fdbe8c42242d3df28cbc4fe63d18): Shorten event names.
> - [<small>2022-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da3fab304cf1ecd9f7134fa969e4e6b3f8a9fa11): Add an example: Remember caret position when reopening Obsidian
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Example%20shell%20commands/Remember%20caret%20position%20when%20reopening%20Obsidian.md).
> ^page-edit-history