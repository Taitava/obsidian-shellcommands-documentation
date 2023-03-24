---
cssclass: customiseTitle
---
# Example: Launch external applications
## Windows
On Windows, you can use a shell command `start`.
- For example `start git-gui` would launch an application named [Git GUI](https://git-scm.com/docs/git-gui), which can be used for keeping version history of for example Markdown files.
- You can also launch a terminal window like this: `start wt.exe` (launches [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)). Or just simply: `wt.exe`.
- For opening up Microsoft Paint, you can: do `mspaint`. So, some applications can be launched even without the `start` command.


### If `start` does not work

Sometimes you might need to add  an empty argument `""` to the `start` command to make launching your application work. For example, launching [a Windows version of Git Bash] requires to use the following command: `start "" "%PROGRAMFILES%\Git\bin\sh.exe" --login`.

### Strange error messages
`start` may sometimes yell error messages even though the application launches correctly. For example, `start git-gui` gives an error code *259* and an error message *Command failed: git-gui*. If something like this happens to you, you can [[Ignoring errors|ignore specific error codes, or all errors altogether]].

## Linux
Open the current file in a text editor: `gedit {{file_path:absolute}}`.

## macOS
Open the current file in a text editor: `open -a TextEdit {{file_path:absolute}}`.

# History


> [!page-edit-history]- Page edit history: 2021-11-19 &#10132; 2023-02-28
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/920506704755013392420d110d2d90319cc0cf51): Example shell commands: Add Linux and Mac versions.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/07f94b03e4e8a79f1269c1dab598b5e7f536b652): Example shell commands.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Example%20shell%20commands/Launch%20external%20applications.md).
> ^page-edit-history