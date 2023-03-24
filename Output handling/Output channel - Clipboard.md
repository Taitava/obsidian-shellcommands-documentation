---
aliases:
 - Clipboard
cssclass: customiseTitle
---
# Output channel: Clipboard
Output will be copied to the clipboard as text.

In addition, the output will be shown in a notification balloon, so that you can see what was copied to the clipboard. This can be disabled in the plugin's settings panel (in *Output* tab):
![[Settings-main-output-tab.png]]

# Differences in *realtime* mode

If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.

> [!tldr] _Clipboard_ - realtime mode differences:
> - Clipboard content is updated multiple times during execution. Each time when new output is received, it gets added at the end of old output, making the clipboard always contain **all output** that have been received so far. No early output is lost.
> - You may see multiple _Copied to clipboard_ notifications, if you have the _Outputting to 'Clipboard' displays a notification message_ setting turned on (it's on by default).
> - `stdout` and `stderr` are mixed together in the order they are outputted in *realtime* mode. In *wait* mode they are grouped together so that either **all** `stdout` output comes first, and then comes **all** `stderr` output (or vice-versa, depending on settings).
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channel was released. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).

> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2022-11-26
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c246d0dfab942a8dabaf05fee5d17073fc893d82): Output channel: Clipboard: Fix heading.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/64f383151f457c2fc72d844566d8a8a4d92a2b3c): Output channels: Add version history.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e98d750bc24d867629c6de1fa5019c31b6e87f49): Exract output channels to separate files.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Clipboard.md).
> ^page-edit-history