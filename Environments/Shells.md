---
aliases:
  - shell
---
Knowing your shell allows you to find out what shell commands are available for you to use, although most of the differences in command sets depend on which operating system you use, not so much on which shell you use. Then again, some commands may act a bit differently in different shells.

## Built-in shells
> [!Info]
> The *Shell commands* plugin has built-in support for the shells listed below. In case you want to use a different shell, you can define a [[Custom shells|custom shell]]. Even when using one of the built-in shells listed below, it might make sense to configure it as a custom shell, as that offers more control over the shell's settings, e.g. the ability to define a different path for the shell.
> 
> **Built-in shells do not offer any settings.**

### Windows
| Shell                                           | Executable name  | Used switches                                                                                                                        |
| ----------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [[CMD.EXE\|Command Prompt]]                     | `CMD.EXE`        | [`/d /s /c`](https://ss64.com/nt/cmd.html)                                                                                           |
| [[PowerShell#PowerShell Core\|PowerShell Core]] | `pwsh.exe`       | [`-c`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.3)           |
| [[PowerShell#PowerShell 5\|PowerShell 5]]       | `powershell.exe` | [`-c`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1) |
- These shells are executed by their executable names only, not by a complete file path, so their location doesn't matter, but they need to be declared in the [[Additions to the PATH environment variable|Path environment variable]] if they are used.
- Used switches cannot be altered for built-in shells. If needed, define a [[Custom shells|custom shell]] instead.

### Linux and macOS
| Shell    | Binary path | Used switches                                                               |
| -------- | ----------- | --------------------------------------------------------------------------- |
| [[Bash]] | `/bin/bash` | [`-c`](https://www.man7.org/linux/man-pages/man1/bash.1.html)               |
| [[Dash]] | `/bin/dash` | [`-c`](https://man7.org/linux/man-pages/man1/dash.1.html)                   |
| [[Zsh]]  | `/bin/zsh`  | [`-c`](https://zsh.sourceforge.io/Doc/Release/Invocation.html#Invocation-1) |
- Binary paths cannot be altered for built-in shells. If you need to use different paths, you can define a [[Custom shells|custom shell]] instead.
- Used switches cannot be altered for built-in shells.

## Custom shells
> [!Warning] This feature is only available in a beta test
> - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/108#discussioncomment-5277523).
		> %% #TODO: Remove this annotation when the final version is released. %%

![[Custom shells#^custom-shells-summary]]

> [!Tip] [[Custom shells|Read more about custom shells]]

## How to know which shell is used
1. Open up the plugin's settings pane and click the *Environments* tab.
![[Settings-main-environments-default-shell.png]]
2. Look at *default shell* drop-down menu next to the operating system you are currently using. It shows you the name of the shell that is currently used.
	If *Use system default ()* is selected, then the shell name is indicated in the parenthesis.
	
## Choosing a shell on a per shell command basis
In the above section, you are able to change the shell that all of your shell commands use **by default**. However, if you have a certain shell command that needs to be executed in another shell, you can select a shell for that shell command explicitly.
1. Open up the plugin's settings pane and locate a shell command that you want to select a different shell for.
2. Click the *Shell selection, Operating system specific shell commands* icon button next to the shell command:
	![[Settings-main-click-environments-icon.png]]
3. An *extra options* modal pops up. You can switch the shell at the bottom of the modal:
	![[Settings-modal-environments.png]]

# History


> [!page-edit-history]- Page edit history: 2021-11-21 &#10132; 2023-03-25
> - [<small>2023-03-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4f304a3cafb96df717a589d73194c3998e45f997): Custom shells.md: Begin writing documentation.
> - [<small>2023-03-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8e8a5f52843516c77953875f773d0f760bbb1855): Shells.md: More information about built-in shells.
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2022-04-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/893a7098c3a22942bf115447418212a97c616dcb): Forgot to rename directory 'Operating systems and shells' to 'Environments'.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b5c6aabefb69afcf387fb2a4fd20e9c223f080bc): 0.12.0: Updated old screenshots to contain 'Environments', 'Preactions' and 'Variables' tabs.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fad0f25eae8bdfa9ecd82fda2d32fbbddbe3654f): Change 'Operating systems & shells' tab name to 'Environments'.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/118aaeb67eed11873cbe54c98b0f74b152b1c210): Shells.md: Add 'Choosing a shell on a per shell command basis'.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3010cd79f48e79b997509b6a8a1b0bad5a23993b): Create Shells.md.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Environments/Shells.md).
> ^page-edit-history