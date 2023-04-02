---
aliases:
 - Windows Subsystem for Linux
 - WSL
---

 > [!Warning] This feature is only available in a beta test
 > - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/108#discussioncomment-5277523).
 > %% #TODO: Remove this annotation when the final version is released. %%

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

# Configure the _Shell commands_ plugin to use WSL

This section walks you through the configuring process step by step, just like [[Settings for custom shells]], but with the instructions adapted for WSL.

**To begin**, open up the settings panel in Obsidian by pressing the hotkey `Ctrl` + `,` . Navigate to _Shell commands_ -> _Environments_ -> _Custom shells_. Click the _New custom shell_ button. A modal pops up, where you can configure the custom shell's options as described in the below subchapters.

> [!Attention]
> The screenshots used on this page are general screenshots for the [[custom shells]] feature, and might not show correct values for WSL. They are meant to only show **where** specific values should be defined in. **Always read the configuration values below the images.**

## Shell name and description

![[Settings-Custom-shell-Shell-name-and-description.png]]
The name and description are freely decidable, as they do not affect the custom shell's operation in any way.

_Shell name_: `Windows Subsystem for Linux (WSL)`
_Description_:
```
"WSL is a feature of Windows that allows developers to run a Linux environment without the need for a separate virtual machine or dual booting." (from: https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)

This custom shell configuration allows you to execute Linux/Bash commands from Obsidian on Windows.

Install WSL: https://learn.microsoft.com/en-us/windows/wsl/install
```

## Executable binary file path

![[Settings-Custom-shell-Executable-binary-file-path.png]]

WSL's executable binary file path is: `C:\Windows\System32\wsl.exe` (at least on Windows 10).

## Shell arguments

![[Settings-custom-shell-shell-arguments.png]]

Use the following shell arguments:
```
--
{{!shell_command_content}}
```
The two dashes `--` are meant to be **included**, and should be on its own line, before `{{!shell_command_content}}`. The dashes indicate that no shell options will be defined after them, so everything after the dashes should be interpreted as executable commands.

> [!Info] About `{{!shell_command_content}}`
> `{{!shell_command_content}}` is a placeholder for any executable shell command. `!` means that special characters in the shell command are **not** [[Escaping special characters in variable values|escaped]] when passing the command as an argument. However, the shell command's content may contain already escaped special characters before it gets passed as an argument.

## Host operating system

![[Settings-Custom-shell-Host-operating-system.png]]

_Host operating system_ must be **Windows**, as WSL is run on Windows.
_Windows: Quote shell arguments_ must be **disabled**.

## Shell's operating system

![[Settings-Custom-shell-Shells-operating-system.png]]
_Shell's operating system_ must be **Linux**.

## Special characters escaping

![[Settings-Custom-shell-Special-characters-escaping.png]]
Select **Unix shell style with \\ as escape character**. 

## Path translator

![[Settings-Custom-shell-Path-translator.png]]

As the [[#Shell's operating system]] differs from [[#Host operating system]], a _Path translator_ must be defined, so that Windows file paths get converted to a format that works in WSL. Use the following JavaScript function as the translator:
```javascript
const pathParts = absolutePath.match(/^([a-z]):\/(.+)$/ui);
const driveLetter = pathParts[1];
const trailingPath = pathParts[2];
return '/mnt/' + driveLetter.toLocaleLowerCase() + '/' + trailingPath;
```

Test that the path translator works by clicking the _Test absolute path translation_ icon: ![[Translate-icon.png]]. It should provide three test paths:
![[Settings-Custom-shell-WSL-path-translation-test.png]]
Your paths will be different, as you have your vault in a different directory, and differently named files. **Just make sure all the three paths start with `/mnt/`** .

## Wrapper for shell command

![[Settings-custom-shell-wrapper-for-shell-command.png]]

You can leave the wrapper field empty. A wrapper could be defined if you'd like to execute certain commands before and/or after the main command, but there's no explicit need for it.

## Execute a command to test the shell

![[Settings-Custom-shell-Execute-command-to-test-shell.png]]

You can define e.g. the following test command:

```bash
echo "Hello $USER, current working directory is: $(pwd)"
```

Click the _Execute the test command using this shell_ icon button: ![[Execute-icon.png]]

Make sure that the outputted _current working directory_ is your Obsidian vault's path (assuming you have not changed the [[Working directory]] setting).

Example result for me:
![[Settings-Custom-shell-WSL-execution-test.png]]

## Make shell commands to use the newly created WSL shell

Now that the WSL is configured as a custom shell, it still needs to be taken into use. There are two ways to select the shell:
 - **A**) a default shell can be selected for all shell commands that do not have an explicitly selected shell, or
 - **B)** a shell can be selected for each shell command individually.

> [!Info]- A) Select WSL as a _default_ shell
> You can follow this guide about finding out the current default shell. You can change the default shell there, too.
> ![[Shells#How to know which shell is used]]

> [!Info]- B) Select WSL for an individual shell command
> ![[Shells#Choosing a shell on a per shell command basis]]

Now all the configuration should be done. Try to execute your shell commands!