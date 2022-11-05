---
aliases:
  - "Current file"
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
- #TODO: Add a date [0.17.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channels *Current file: top* and *Current file: bottom* were created. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel *Current file: caret position* was created. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).