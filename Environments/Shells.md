---
aliases:
  - shell
---
Knowing your shell allows you to find out what shell commands are available for you to use, although most of the differences in command sets depend on which operating system you use, not so much on which shell you use. Then again, some commands may act a bit differently in different shells.

## Currently supported shells
At the moment, the *Shell commands* plugin only supports a limited set of shells. Support for customisable shells might be added later.

### Windows
- [[CMD]]
- [[PowerShell 5]]
- [[PowerShell Core]]

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
<small>This page was last modified on <strong>2023-02-28</strong> and created on 2021-11-21. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Environments/Shells.md">See page edit history</a>.</small>
