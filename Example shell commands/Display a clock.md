---
cssclass: customiseTitle
---
# Example: Display a clock

This example uses [[Events - general principles|events]] to keep an up-to-date information about the current time on the status bar. The time is updated every second.

## [[Every n seconds]] event needs to be enabled
![[Settings-modal-events-Example-display-clock.png]]

Configure the [[Every n seconds]] event to execute this shell command every 1 second.

## Stdout channel must be *Status bar*
![[Settings-modal-Output-stdout-status-bar.png]]

## Windows, Linux & macOS
The following shell command should work on every operating system. It's actually so simple that it should not need a shell at all (it's just about outputting the [[{{date}}]] variable's value), but the *Shell commands* plugin does not currently offer a way to just output stuff without passing it to a shell first.

`echo {{date:HH:mm:ss}}`

## Result
This is how the clock will look like in the status bar:
![[Example-display-clock.gif]]

# History


> [!page-edit-history]- Page edit history: 2022-01-29 &#10132; 2023-02-28
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e5b806c587863e196b130ee859c05d9ac9ff0fae): Examples: Display a clock.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Example%20shell%20commands/Display%20a%20clock.md).
> ^page-edit-history