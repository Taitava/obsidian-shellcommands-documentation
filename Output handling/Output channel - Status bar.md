---
aliases:
  - "Status bar"
---
# Output channel: Status bar
Outputs text to the bottom of the Obsidian window. The last line of the output is visible permanently. If the output contains multiple lines, you can hover the status bar with mouse to see all the outputted lines.
 
**Good for:** Output that is wanted to be easily visible for a longer time, and that usually needs just one line.
 
The text is visible until another shell command execution outputs text to the status bar, replacing the old text. **Note that if the new execution produces empty text output, the old text will not be removed**, because empty text is considered to be "no output at all", so it's not processed. This might change in the future.
 
![[Output-status-bar.png]]
 
The position and available space of the status bar output element depends on how many other things have inserted content in the status bar (e.g. other plugins). The *Shell commands* plugin will never replace or remove other content in the status bar.