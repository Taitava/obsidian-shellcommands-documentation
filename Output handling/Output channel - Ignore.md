---
aliases:
  - Ignore
cssclass: customiseTitle
---
# Output channel: Ignore
Simply hides the output, doing nothing with it. This is the default for all commands' `stdout` output, because for many commands, the normal output is not so important. E.g. when creating a folder, launching an application or modifying a file - in these cases, the lack of error messages is usually enough to tell that the command executed successfully.

# Differences in *realtime* mode  
  
If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.  
  
> [!tldr] _Ignore_ - realtime mode differences:
> - No differences, when chosen as an *output channel* so that it ignores e.g. all `stderr` output.
> - In *realtime* mode, there's no way to filter `stderr` by *exit codes*, because an exit code is not available at the time `stderr` output is received.
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel was released. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).

> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2022-11-26
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/64f383151f457c2fc72d844566d8a8a4d92a2b3c): Output channels: Add version history.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e98d750bc24d867629c6de1fa5019c31b6e87f49): Exract output channels to separate files.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Ignore.md).
> ^page-edit-history