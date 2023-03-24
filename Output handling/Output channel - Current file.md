---
aliases:
  - "Current file"
cssclass: customiseTitle
---
# Output channel: Current file: top/bottom/caret position
Output will be inserted to the file that is currently open and active in Obsidian. If no file is active (e.g. you have Graph view active instead of a file), the output will be shown in a message balloon.
 
If *caret position* is used, then the output can replace text if you have something selected.

# Differences in *realtime* mode  
  
If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.  
  
> [!tldr] _Current file_ - realtime mode differences:
> - *Current file: caret position*: If you move text caret in editor during execution, subsequent output will go to different locations. Can lead to accidents if you don't notice that a shell command has not finished executing.
> - *Current file: top*: As each outputted text part is always inserted at the top of a note, the first output line will end up being **under** the second line, and so on. This reversed output order might be either a hit or a miss.
> - *Current file: bottom*: Should work quite the same as in *wait* mode, no big surprises should happen.
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channels *Current file: top* and *Current file: bottom* were created. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel *Current file: caret position* was released. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).

> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2022-11-26
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/64f383151f457c2fc72d844566d8a8a4d92a2b3c): Output channels: Add version history.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e98d750bc24d867629c6de1fa5019c31b6e87f49): Exract output channels to separate files.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Current%20file.md).
> ^page-edit-history