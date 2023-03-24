---
aliases:
  - shell
---
Knowing your shell allows you to find out what shell commands are available for you to use, although most of the differences in command sets depend on which operating system you use, not so much on which shell you use. Then again, some commands may act a bit differently in different shells.

## Currently supported shells
At the moment, the *Shell commands* plugin only supports a limited set of shells. Support for customisable shells might be added later.

### Windows
- [[CMD.EXE]]
- [[PowerShell#PowerShell Core|PowerShell Core]]
- [[PowerShell#PowerShell 5|PowerShell 5]]

### Linux and macOS
- [[Bash]]
- [[Dash]]
- [[Zsh]]

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


> [!page-edit-history]- Page edit history: 2021-11-21 &#10132; 2023-02-28
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