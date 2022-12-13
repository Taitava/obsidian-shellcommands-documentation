---
aliases:
  - Ignore
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
<small>This page was last modified on <strong>2022-11-26</strong> and created on 2021-11-25. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Ignore.md">See page edit history</a>.</small>
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel was created. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).