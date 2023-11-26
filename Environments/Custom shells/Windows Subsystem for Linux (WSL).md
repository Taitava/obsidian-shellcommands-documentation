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
--
{{!shell_command_content}}
```
The two dashes `--` are meant to be **included**, and should be on its own line, before `{{!shell_command_content}}`. The dashes indicate that no shell options will be defined after them, so everything after the dashes should be interpreted as executable commands.

Note that WSL does not use a `-c` switch before the `{{!shell_command_content}}` part, unlike many other shells do.

> [!Tip]- If you have multiple distros installed
> If you have multiple distros installed, you can specify what distro should be used by adding `-d DistroName` to the list of arguments:
> ```
> -d Ubuntu-22.04
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
> [!page-edit-history]- Page edit history: 2023-04-02 &#10132; 2023-04-16
> - [<small>2023-04-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/79ac0bd858ee53b8b721ba44d5d980c2325f0f1f): [[Windows Subsystem for Linux (WSL).md]]: Use WSL specific screenshots.
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/836d6a75e93c7664cf895a02722ec688f612f172): [[Windows Subsystem for Linux (WSL).md]]: Rename a heading.
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/92811b9c999f3459792dd2ab6639f77b9477466b): [[Windows Subsystem for Linux (WSL).md]]: Add more info to [[#Wrapper for shell command]].
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e10d73ad0efbeb59eccdd175d3c7c8628630dd54): [[Windows Subsystem for Linux (WSL).md]]: Add more info to [[#Path translator]].
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/47744de2b41b0ae2f44a8cbe83d4bcd0301bf3bc): [[Settings for custom shells.md]]: Add content.
> - [<small>2023-04-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7bd74c26aac68d0051a128d58fa15f8f3d6f03f5): Custom shell example: Windows Subsystem for Linux (WSL)
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Environments/Custom%20shells/Windows%20Subsystem%20for%20Linux%20%28WSL%29.md).
> ^page-edit-history