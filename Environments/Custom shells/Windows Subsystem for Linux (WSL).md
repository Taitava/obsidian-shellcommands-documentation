---
aliases:
 - Windows Subsystem for Linux
 - WSL
---

## What is WSL? 

> [!Quote] From [Wikipedia: Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux):
> **Windows Subsystem for Linux** (**WSL**) is a feature of Windows that allows developers to run a Linux environment without the need for a separate [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine "Virtual machine") or [dual booting](https://en.wikipedia.org/wiki/Dual_booting "Dual booting")

> [!Quote] From [learn.microsoft.com](https://learn.microsoft.com/en-us/windows/wsl/install):
> Developers can access the power of both Windows and Linux at the same time on a Windows machine. The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc.) and use Linux applications, utilities, and Bash command-line tools directly on Windows, unmodified, without the overhead of a traditional virtual machine or dual-boot setup.

From the _Shell commands_ plugin's point-of-view, _Windows Subsystem for Linux (WSL)_ makes it easier to define cross-platform compliant shell commands in Obsidian, as a vault that is synced between multiple machines with different operating systems, can use a similar shell (e.g. [[Bash]]) on all operating systems. WSL is only available for Windows. Linux and macOS can use [[Bash]] (or some other Unix shell) natively without WSL-like system.

**From this point on, this page will only use the abbreviation _WSL_ to refer to _Windows Subsystem for Linux_.**

# Install WSL on Windows

As this documentation focuses on the usage of the _Shell commands_ plugin, WSL installation is out of the documentation's scope. If you don't have WSL installed already, you can follow the following installation guide: [Install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

> [!Info] WSL distro: Ubuntu
> This documentation assumes that WSL is installed with [Ubuntu](https://ubuntu.com/wsl) as it's <abbr title="distribution">distro</abbr>. That's also the default distro that `wsl --install` installs. However, this guide should work just perfectly for whatever distro. If you encounter problems with other distros, please start a discussion in the [_Debugging and testing_ discussion category on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/debugging-and-testing). 
> 
> <small>(Btw, if you have **multiple** distros installed, see [[#^multiple-distros|this tip for choosing which distro to use]] with your custom shell configuration.)</small>

# Configure a new _custom shell_: WSL

This section walks you through the configuring process step by step, just like [[Settings for custom shells]], but with the instructions adapted for WSL.

**To begin**, open up the settings panel in Obsidian by pressing the hotkey `Ctrl` + `,` . Navigate to _Shell commands_ -> _Environments_ -> _Custom shells_. Click the _New custom shell_ button. A modal pops up, where you can configure the custom shell's options as described in the below subchapters.

## Shell name and description

![[Settings-Custom-shell-WSL-Shell-name-and-description.png]]
The name and description are freely decidable, as they do not affect the custom shell's operation in any way.

_Shell name_: `Windows Subsystem for Linux (WSL)`
_Description_:
```
"WSL is a feature of Windows that allows developers to run a Linux environment without the need for a separate virtual machine or dual booting." (from: https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)

This custom shell configuration allows you to execute Linux/Bash commands from Obsidian on Windows.

Install WSL: https://learn.microsoft.com/en-us/windows/wsl/install
```

## Executable binary file path

![[Settings-Custom-shell-WSL-Executable-binary-file-path.png]]

WSL's executable binary file path is: `C:\Windows\System32\wsl.exe` (at least on Windows 10).

## Shell arguments

![[Settings-Custom-shell-WSL-Shell-arguments.png]]
Use the following shell arguments:
```
--shell-type login
--
{{!shell_command_content}}
```
- `--shell-type login` tells WSL that startup scripts should be executed when invoking the shell (e.g. `~/.profile` and `~/.bashrc`). In practise, this ensures that the [[Additions to the PATH environment variable|$PATH environment variable]] will contain all directories needed to execute third party programs.
- The two dashes `--` are meant to be **included**, and should be on its own line, before `{{!shell_command_content}}`. The dashes indicate that no shell options will be defined **after** them, so everything **after** the dashes should be interpreted as executable commands.

Note that WSL does not use a `-c` switch before the `{{!shell_command_content}}` part, unlike many other shells do.

> [!Tip]- If you have multiple distros installed
> If you have multiple distros installed, you can specify what distro should be used by adding `-d DistroName` to the list of arguments:
> ```
> -d Ubuntu-22.04
> --shell-type login
> --
> {{!shell_command_content}}
> ```
> To get the names of all installed distros, you can execute `wsl -l` in a terminal.
> If you want to run certain shell commands in one distro, and others in another distro, you can create multiple custom shells, one for each distro. ^multiple-distros

![[Settings for custom shells#^about-shell-command-content]]

## Host operating system

![[Settings-Custom-shell-General-Host-operating-system-Windows-Quote-off.png]]

_Host operating system_ must be **Windows**, as WSL is run on Windows.
_Windows: Quote shell arguments_ must be **disabled**.

## Shell's operating system

![[Settings-Custom-shell-General-Shells-operating-system-Linux.png]]
_Shell's operating system_ must be **Linux**.

## Special characters escaping

![[Settings-Custom-shell-General-Special-characters-escaping-Unix.png]]
Select **Unix shell style with \\ as escape character**. 

## Path translator

![[Settings-Custom-shell-WSL-Path-translator.png]]

As the [[#Shell's operating system]] differs from [[#Host operating system]], a _Path translator_ must be defined, so that Windows file paths get converted to a format that works in WSL. Use the following JavaScript function as the translator:
```javascript
const pathParts = absolutePath.match(/^([a-z]):\/(.+)$/ui);
const driveLetter = pathParts[1];
const trailingPath = pathParts[2];
return '/mnt/' + driveLetter.toLocaleLowerCase() + '/' + trailingPath;
```

> [!question]- Path translator code explained in detail
> Consider the following example path when interpreting the translator code: `C:\Obsidian vaults\My vault\MyNote.md`.
> 1. Before the translator code is called, the SC plugin has automatically replaced backslashes `\` with forward slashes `/` (because we selected `Linux` as the _Shell's operating system_ above).
>     - So, `absolutePath` has a value of `C:/Obsidian vaults/My vault/MyNote.md`.
> 2. Split the path into two parts using a regular expression (regex):
>     ```javascript
>     const pathParts = absolutePath.match(/^([a-z]):\/(.+)$/ui);
>     ```
>     1. `^` denotes a start of a string, as we want to pick up a letter that is the **first** character of the string.
>     2. `([a-z])` denotes that we want to pick up a drive letter that is any alphabet between `a` and `z`. (The letter can be upper or lower case, because a case-insensitive regex modifier `i` is used - see the point 2.5. below). Parenthesis `()` tell regex to store their content as the first part of the path.
>         - Considering the example path, `C` is picked up as the drive letter.
>     3. A colon and a forward slash `:\/` are literal characters that are just assumed to be present after the drive letter. The colon `:` is not needed in the translated path, so it's simply discarded.
>         - (The forward slash `/` is preceded with a backslash `\` to denote that it should be considered as a literal character, not as the end of the regex pattern).
>     4. `(.+)$` denotes that we want to pick up all the rest of the characters as the second part of the path. The dot `.` denotes any character (a letter, a number, a whitespace or a punctuation character) and `+` tells to pick up at least one, but possibly multiple characters. The dollar `$` denotes that all characters until the very end of the string should be picked up.
>         - Considering the example path, `Obsidian vaults/My vault/MyNote.md` is picked up as the trailing part of the path.
>     5. Characters `ui` after the last forward slash `/` indicate regex _modifiers_:
>         - `u` tells regex to support unicode characters, just in case any of them are present in `absolutePath`.
>         - `i` tells regex to pick up also uppercase drive letters, even though the pattern only expresses lowercase letters `a-z`.
> 3. Assign the picked up parts to constants `driveLetter` and `trailingPath`.
>     ```javascript
>     const driveLetter = pathParts[1];
>     const trailingPath = pathParts[2];
>     ```
>     - `driveLetter` becomes `C`.
>     - `trailingPath` becomes `Obsidian vaults/My vault/MyNote.md`.
> 4. Add a prefix, concatenate the path parts together, and return the result.
>     ```javascript
>     return '/mnt/' + driveLetter.toLocaleLowerCase() + '/' + trailingPath;
>     ```
>     - `/mnt/` is used in WSL as a special directory via which Windows file system can be accessed.
>     - `/mnt/` is followed by a Windows drive letter (which must be converted to lower case).
>     - The rest of the path is presented after the drive letter, separated by a forward slash `/`.
>     - The translator returns the result `/mnt/c/Obsidian vaults/My vault/MyNote.md`.

Test that the path translator works by clicking the _Test absolute path translation_ icon: ![[Translate-icon.png]]. It should provide three test paths:
![[Settings-Custom-shell-WSL-Path-translation-test.png]]
Your paths will be different, as you have your vault in a different directory, and differently named files. **Just make sure all the three paths start with `/mnt/`** .

![[Settings for custom shells#^what-file-system-paths-are-translated]]

## Wrapper for shell command

![[Settings-Custom-shell-General-Wrapper-for-shell-command-Empty.png]]

You can leave the wrapper field empty. A wrapper could be defined if you'd like to execute certain commands before and/or after the main command, but there's no explicit need for it.

![[Settings for custom shells#^about-shell-command-content]]

## Execute a command to test the shell

![[Settings-Custom-shell-WSL-Execute-command-to-test-shell.png]]

You can define e.g. the following test command:

```bash
echo "Hello $USER, current working directory is: $(pwd)"
```

Click the _Execute the test command using this shell_ icon button: ![[Execute-icon.png]]

Make sure that the outputted _current working directory_ is your Obsidian vault's path (assuming you have not changed the [[Working directory]] setting).

Example result for me:
![[Settings-Custom-shell-WSL-Execution-test.png]]

## Make shell commands use the newly created WSL shell

![[Settings for custom shells#Make shell commands use the newly created shell]]

# History
> [!page-edit-history]- Page edit history: 2023-04-02 &#10132; 2023-11-26
> - [<small>2023-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/91a0808dd6e1ddc64db26d6931ff73f1cbe4a918): [[Windows Subsystem for Linux (WSL).md]]: Add `-shell-type login` argument.
> - [<small>2023-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6306e0b87569083c9e6c1ceace8f4f4846001e23): [[Windows Subsystem for Linux (WSL).md]]: Explain path translator details.
> - [<small>2023-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/dfcbec7cdd993836578aeea96f002004ca33fb6b): [[Windows Subsystem for Linux (WSL).md]]: Mention that no `-c` switch is used with WSL.
> - [<small>2023-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f38c1167c404a492729f9e692029aa73b2fc2585): [[Windows Subsystem for Linux (WSL).md]]: Add a tip about choosing a distro.
> - [<small>2023-04-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/79ac0bd858ee53b8b721ba44d5d980c2325f0f1f): [[Windows Subsystem for Linux (WSL).md]]: Use WSL specific screenshots.
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/836d6a75e93c7664cf895a02722ec688f612f172): [[Windows Subsystem for Linux (WSL).md]]: Rename a heading.
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/92811b9c999f3459792dd2ab6639f77b9477466b): [[Windows Subsystem for Linux (WSL).md]]: Add more info to [[#Wrapper for shell command]].
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e10d73ad0efbeb59eccdd175d3c7c8628630dd54): [[Windows Subsystem for Linux (WSL).md]]: Add more info to [[#Path translator]].
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/47744de2b41b0ae2f44a8cbe83d4bcd0301bf3bc): [[Settings for custom shells.md]]: Add content.
> - [<small>2023-04-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7bd74c26aac68d0051a128d58fa15f8f3d6f03f5): Custom shell example: Windows Subsystem for Linux (WSL)
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Environments/Custom%20shells/Windows%20Subsystem%20for%20Linux%20%28WSL%29.md).
> ^page-edit-history