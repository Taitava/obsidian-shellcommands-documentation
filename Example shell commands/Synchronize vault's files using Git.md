---
cssclasses:
  - customiseTitle
---
# Example: Synchronize vault's files using Git

This example demonstrates how to upload changed files to a remote [Git](https://git-scm.com) repository, and also download changes periodically.
## Prerequisites
- It is assumed that you know what Git is, how to use basic features of Git, and how to set up a remote repository in GitHub or some other platform.
- This example does not do `git init` nor `git remote add` - it assumes that a repository is already set up.
- Possible merge conflicts are not taken into account at all. It is assumed that the Obsidian vault is opened only on one computer at a time, changes are done, committed and pushed, and finally Obsidian is closed. After that, Obsidian can be opened in another computer and changes can be pulled automatically before editing files again.
- The shell commands are written in [[Bash]] (although they could be easily ported to other shells, too), so on Windows, [[Windows Subsystem for Linux (WSL)]] is used. This enables using the same commands across all operating systems: macOS, Linux and Windows without maintaining separate commands for Windows.
## An example vault
The example is located in a separate [Git sync vault stored in GitHub](https://github.com/Taitava/git-sync-example-vault) which contains predefined shell commands. You can clone the vault on your machine and inspect the shell commands there.

After cloning the vault, **the _Shell commands_ plugin needs to be installed**. [How to install the plugin](https://github.com/Taitava/obsidian-shellcommands?tab=readme-ov-file#installation--usage).
## Features

The vault has the following features:
- `git pull` is executed every time Obsidian starts, and every 60 seconds. These can be changed in the vault's settings, e.g. the interval can be made longer or removed completely.
- `git add --all && git commit -m "..." && git push` is executed automatically when any of the following events trigger:
    - [[File content modified]]
    - [[File created]]
    - [[File deleted]]
    - [[File moved]]
    - [[File renamed]]
    - The events use [[Events - debouncing|debouncing]] with 20 seconds cooldown duration, so if multiple events occur during 20 seconds, the execution is postponed to happen 20 seconds after the last event, to avoid creating too many commits with incomplete changes.
    - The commit message `-m "..."` depends on event, and can be customised.
    - If wanted, `git push` could be extracted to a separate shell command and executed e.g. every 10 minutes and every time Obsidian quits.
     - **Note that events are disabled by default in the vault.** This is to ensure you have the opportunity to inspect the shell commands before they are executed. After inspecting, you can [[Events - general principles#See which events are currently enabled|read this to know how to enable events]].
 - To make `git push` work, the repository needs to be forked in GitHub, as only I can push to the original repository.

# History
> [!page-edit-history]- Page edit history: 2024-04-20 &#10132; 2024-04-20
> - [<small>2024-04-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/85d8f71d01aaeeefc39de8dce892e119d7da297e): Example: [[Synchronize vault's files using Git.md]].
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Example%20shell%20commands/Synchronize%20vault%27s%20files%20using%20Git.md).
> ^page-edit-history