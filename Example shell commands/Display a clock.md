# Example: Display a clock

This example uses [[Events - general principles|events]] to keep an up-to-date information about the current time on the status bar. The time is updated every second.

## [[Every n seconds]] event needs to be enabled
![[Settings-modal-events-Example-display-clock.png]]

Configure the [[Every n seconds]] event to execute this shell command every 1 second.

## Stdout channel must be *Status bar*
![[Settings-modal-Output-stdout-status-bar.png]]

## Windows, Linux & Macintosh
The following shell command should work on every operating system. It's actually so simple that it should not need a shell at all (it's just about outputting the [[{{date}}]] variable's value), but the *Shell commands* plugin does not currently offer a way to just output stuff without passing it to a shell first.

`echo {{date:HH:mm:ss}}`

## Result
This is how the clock will look like in the status bar:
![[Example-display-clock.gif]]

# History
<small>This page was last modified on <strong>2022-02-06</strong> and created on 2022-01-29. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Example%20shell%20commands/Display%20a%20clock.md">See page edit history</a>.</small>
