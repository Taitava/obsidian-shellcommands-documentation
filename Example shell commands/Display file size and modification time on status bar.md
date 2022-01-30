# Example: Display file size and modification time on status bar
==This feature is currently only available in [0.10.0 BETA TEST](https://github.com/Taitava/obsidian-shellcommands/discussions/138)! #TODO: Remove this text when the beta is over.==

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
On Windows, it's easier to use `PowerShell` to get file size and modification times, rather than `CMD`. Go to the *Operating systems & shells* tab in your shell command's extra options modal and switch *Windows shell* to either *PowerShell Core* or *PowerShell 5*, depenging on which you have installed.

Here's the PowerShell command:

```PowerShell
Write-Host("Size: ", [math]::Round((Get-Item {{file_path:absolute}}).length/1KB), "kB. Last modified: ", (Get-Item {{file_path:absolute}}).LastWriteTime)
```

## Linux
#TODO 

## Macintosh
#TODO