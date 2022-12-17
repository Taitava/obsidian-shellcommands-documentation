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

## Macintosh
#TODO

# History
<small>This page was last modified on <strong>2022-04-08</strong> and created on 2022-01-04. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Example%20shell%20commands/Display%20file%20size%20and%20modification%20time%20on%20status%20bar.md">See page edit history</a>.</small>
