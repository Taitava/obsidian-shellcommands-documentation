---
aliases:
  - "Status bar"
cssclass: customiseTitle
---
# Output channel: Status bar
Outputs text to the bottom of the Obsidian window. The last line of the output is visible permanently. If the output contains multiple lines, you can hover the status bar with mouse to see all the outputted lines.
 
**Good for:** Output that is wanted to be easily visible for a longer time, and that usually needs just one line.
 
The text is visible until another shell command execution outputs text to the status bar, replacing the old text. If the new execution produces empty text output, possible old text will be removed, and the status bar may disappear, if no other plugins provide content to it.
 
![[Output-status-bar.png]]
 
The position and available space of the status bar output element depends on how many other things have inserted content in the status bar (e.g. other plugins). The *Shell commands* plugin will never replace or remove other content in the status bar.

# Differences in *realtime* mode  
  
If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.  
  
> [!tldr] _Status bar_ - realtime mode differences:
> - The latest output line is shown on the status bar, but old output is also available when you hover over the status bar with mouse.
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.9.0 - 2021-12-18](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#090---2021-12-18): If output is empty, the status bar content is now cleared. In earlier versions, old status bar content was not changed if new output was empty. ([#124](https://github.com/Taitava/obsidian-shellcommands/issues/124))
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channel was released. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).

> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2022-11-26
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d2dd8ac4e3141b3f94d1958e121446f72b40bd1a): Output channel: Status bar: Add forgotten 0.9.0 history links and date.
> - [<small>2021-12-18</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2cb631e06ceba05aadea751db85824a8a882b001): Output channel - Status bar: If output is empty, the status bar content is now cleared.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/64f383151f457c2fc72d844566d8a8a4d92a2b3c): Output channels: Add version history.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e98d750bc24d867629c6de1fa5019c31b6e87f49): Exract output channels to separate files.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Output%20handling/Output%20channel%20-%20Status%20bar.md).
> ^page-edit-history