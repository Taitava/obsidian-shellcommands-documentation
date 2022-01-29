---
aliases:
  - "Status bar"
---
# Output channel: Status bar
Outputs text to the bottom of the Obsidian window. The last line of the output is visible permanently. If the output contains multiple lines, you can hover the status bar with mouse to see all the outputted lines.
 
**Good for:** Output that is wanted to be easily visible for a longer time, and that usually needs just one line.
 
The text is visible until another shell command execution outputs text to the status bar, replacing the old text. If the new execution produces empty text output, possible old text will be removed, and the status bar may disappear, if no other plugins provide content to it.
 
![[Output-status-bar.png]]
 
The position and available space of the status bar output element depends on how many other things have inserted content in the status bar (e.g. other plugins). The *Shell commands* plugin will never replace or remove other content in the status bar.

## History
- [0.9.0 - 2021-12-18](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#090---2021-12-18): If output is empty, the status bar content is now cleared. In earlier versions, old status bar content was not changed if new output was empty. ([#124](https://github.com/Taitava/obsidian-shellcommands/issues/124))
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channel was created. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).