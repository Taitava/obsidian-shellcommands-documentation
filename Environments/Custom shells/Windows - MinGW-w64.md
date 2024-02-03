---
cssclass: customiseTitle
aliases:
 - MinGW-w64
---

# Windows: MinGW-w64
 
## What is MinGW-w64?

> [!Quote] From [Wikipedia: MinGW-w64](https://en.wikipedia.org/wiki/Mingw-w64):
> **Mingw-w64** is a [free and open source](https://en.wikipedia.org/wiki/Free_and_open-source_software "Free and open-source software") [software development](https://en.wikipedia.org/wiki/Software_development "Software development") environment to create ([cross-compile](https://en.wikipedia.org/wiki/Cross_compiler "Cross compiler")) [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "Microsoft Windows") [PE](https://en.wikipedia.org/wiki/Portable_Executable "Portable Executable") applications. It was [forked](https://en.wikipedia.org/wiki/Fork_(software_development) "Fork (software development)") in 2005–2010 from [MinGW](https://en.wikipedia.org/wiki/MinGW "MinGW") (_Minimalist GNU for Windows_).
> 
> Mingw-w64 includes a [port](https://en.wikipedia.org/wiki/Porting "Porting") of the [GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection "GNU Compiler Collection") (GCC), [GNU Binutils](https://en.wikipedia.org/wiki/GNU_Binutils "GNU Binutils") for Windows ([assembler](https://en.wikipedia.org/wiki/Assembler_(computing) "Assembler (computing)"), [linker](https://en.wikipedia.org/wiki/Linker_(computing) "Linker (computing)"), [archive manager](https://en.wikipedia.org/wiki/Archive_file "Archive file")), a set of freely distributable Windows specific [header files](https://en.wikipedia.org/wiki/Header_file "Header file") and [static import libraries](https://en.wikipedia.org/wiki/Static_library "Static library") which enable the use of the [Windows API](https://en.wikipedia.org/wiki/Windows_API "Windows API"), a Windows native build of the [GNU Project](https://en.wikipedia.org/wiki/GNU_Project "GNU Project")'s [GNU Debugger](https://en.wikipedia.org/wiki/GNU_Debugger "GNU Debugger"), and miscellaneous utilities.

From the _Shell commands_ plugin's point-of-view, MinGW-w64 makes it easier to define cross-platform compliant shell commands in Obsidian, as a vault that is synced between multiple machines with different operating systems, can use the same shell ([[Bash]]) on all operating systems. This means that the same shell commands should work on both Windows and Linux/macOS. MinGW-w64 is only available for Windows. Linux and macOS can use [[Bash]] natively without MinGW-w64.

You could use [[Windows Subsystem for Linux (WSL)]] to achieve the same cross-platform ability. However, **if** you have [Git for Windows](https://gitforwindows.org/) installed on your Windows machine, you also have MinGW-w64 installed, in which case you can choose not to install WSL if you don't need it otherwise.

# Install MinGW-w64 on Windows

As this documentation focuses on the usage of the _Shell commands_ plugin, MinGW-w64 installation is out of the documentation's scope. If you don't have MinGW-w64 installed already, you can install one of the following:
- Install [Git for Windows](https://gitforwindows.org/): This installs [Git](https://git-scm.com) together with MinGW-w64. Handy, if you need both of them.
- Install [MinGW-w64](https://www.mingw-w64.org/) without [Git](https://git-scm.com).

# Configure a new _custom shell_: MinGW-w64

This section walks you through the configuring process step by step, just like [[Settings for custom shells]], but with the instructions adapted for MinGW-w64.

**To begin**, open up the settings panel in Obsidian by pressing the hotkey `Ctrl` + `,` . Navigate to _Shell commands_ -> _Environments_ -> _Custom shells_. Click the _New custom shell_ button. A modal pops up, where you can configure the custom shell's options as described in the below subchapters.

## Shell name and description

![[Settings-Custom-shell-MinGW-w64-Shell-name-and-description.png]]
The name and description are freely decidable, as they do not affect the custom shell's operation in any way.

_Shell name_: `MinGW-w64`
_Description_:
```
"Mingw-w64 is an advancement of the original mingw.org project, created to support the GCC compiler on Windows systems." (from: https://www.mingw-w64.org/)

This custom shell configuration allows you to execute some Linux/Bash commands from Obsidian on Windows.
```

## Executable binary file path

![[Settings-Custom-shell-MinGW-w64-Executable-binary-file-path.png]]

The executable binary file path is: `C:\Program Files\Git\bin\bash.exe` .

## Shell arguments

![[Settings-Custom-shell-MinGW-w64-Shell-arguments.png]]

Use the following shell arguments:
```
--login
-c
{{!shell_command_content}}
```

![[Settings for custom shells#^about-shell-command-content]]

## Host operating system

![[Settings-Custom-shell-General-Host-operating-system-Windows-Quote-on.png]]

_Host operating system_ must be **Windows**, as MinGW-w64 is run on Windows.
_Windows: Quote shell arguments_ must be **enabled**.

## Shell's operating system

![[Settings-Custom-shell-General-Shells-operating-system-Linux.png]]
_Shell's operating system_ must be **Linux**.

## Special characters escaping

![[Settings-Custom-shell-General-Special-characters-escaping-Unix.png]]
Select **Unix shell style with \\ as escape character**. 

## Path translator

![[Settings-Custom-shell-MinGW-w64-Path-translator.png]]

As the [[#Shell's operating system]] differs from [[#Host operating system]], a _Path translator_ must be defined, so that Windows file paths get converted to a format that works in MinGW-w64. Use the following JavaScript function as the translator:
```javascript
const pathParts = absolutePath.match(/^([a-z]):\/(.+)$/ui);  
const driveLetter = pathParts[1];  
const trailingPath = pathParts[2];  
return '/' + driveLetter.toLocaleLowerCase() + '/' + trailingPath;
```

Test that the path translator works by clicking the _Test absolute path translation_ icon: ![[Translate-icon.png]]. It should provide three test paths:
![[Settings-Custom-shell-MinGW-w64-path-translation-test.png]]
Your paths will be different, as you have your vault in a different directory, and differently named files. **Just make sure all the three paths start with `/*/`**, where **`*`** is a drive letter.

![[Settings for custom shells#^what-file-system-paths-are-translated]]

## Wrapper for shell command

![[Settings-Custom-shell-General-Wrapper-for-shell-command-Example.png]]

You can leave the wrapper field empty. A wrapper could be defined if you'd like to execute certain commands before and/or after the main command, but there's no explicit need for it.

![[Settings for custom shells#^about-shell-command-content]]

## Execute a command to test the shell

![[Settings-Custom-shell-MinGW-w64-Execute-command-to-test-shell.png]]

You can define e.g. the following test command:

```bash
echo "Hello, current working directory is: $(pwd)"
```

Click the _Execute the test command using this shell_ icon button: ![[Execute-icon.png]]

Make sure that the outputted _current working directory_ is your Obsidian vault's path (assuming you have not changed the [[Working directory]] setting).

Example result for me:
![[Settings-Custom-shell-MinGW-w64-execution-test.png]]

## Make shell commands use the newly created MinGW-w64 shell

![[Settings for custom shells#Make shell commands use the newly created shell]]

# History
> [!page-edit-history]- Page edit history: 2023-04-16 &#10132; 2023-04-16
> - [<small>2023-04-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6140e894cc01c13780f78f4a186f2d1fd4796368): [[Windows - MinGW-w64.md]]: Use MinGW-w64 specific screenshots.
> - [<small>2023-04-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4a3ee0b869ed7bdcb420e867b1d0c7f769fbb4cb): Create [[Windows - MinGW-w64.md]] custom shell documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Environments/Custom%20shells/Windows%20-%20MinGW-w64.md).
> ^page-edit-history