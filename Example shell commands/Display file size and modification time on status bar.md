---
cssclass: customiseTitle
---
# Example: Display file size and modification time on status bar

This example uses events to keep an (almost) up-to-date information about file size and modification time of the currently active file on the status bar. The information is updated:
- When Obsidian starts
- When you switch to another file
- Every 60 seconds so that possible changes to the file will eventually be noticed. This is just because SC version `0.10.x` does not yet have events for detecting file modifications.

This might yield the following error message if you switch to a panel that does not contain a file (e.g. graph view):

![[Error-file-path-no-active-file.png]]

## Events that need to be enabled
![[Settings-modal-events-Example-display-file-size.png]]

## Stdout channel must be *Status bar*
![[Settings-modal-Output-stdout-status-bar.png]]

## Windows
On Windows, it's easier to use `PowerShell` to get file size and modification times, rather than `CMD`. Go to the *Environments* tab in your shell command's extra options modal and switch *Windows shell* to either *PowerShell Core* or *PowerShell 5*, depenging on which you have installed.

Here's the PowerShell command:

```PowerShell
Write-Host("Size: ", [math]::Round((Get-Item {{file_path:absolute}}).length/1KB), "kB. Last modified: ", (Get-Item {{file_path:absolute}}).LastWriteTime)
```

## Linux
#TODO 

## macOS
#TODO

# History


> [!page-edit-history]- Page edit history: 2022-01-04 &#10132; 2023-02-28
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fad0f25eae8bdfa9ecd82fda2d32fbbddbe3654f): Change 'Operating systems & shells' tab name to 'Environments'.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-04</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3aa41de3fe5fbc68f915bb05dc3313ba598ce3a8): WIP: Example: Display file size and modification time on status bar.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Example%20shell%20commands/Display%20file%20size%20and%20modification%20time%20on%20status%20bar.md).
> ^page-edit-history