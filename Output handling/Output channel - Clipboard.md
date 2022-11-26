---
aliases:
 - Clipboard
---
# Output channel: Clipboard
Output will be copied to the clipboard as text.

In addition, the output will be shown in a notification balloon, so that you can see what was copied to the clipboard. This can be disabled in the plugin's settings panel (in *Output* tab):
![[Settings-main-output-tab.png]]

# Differences in *realtime* mode

If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.

> [!tldr] _Clipboard_ - realtime mode differences:
> - Clipboard content is updated multiple times during execution. Each time when new output is received, it gets added at the end of old output, making the clipboard always contain **all output** that have been received so far. No early output is lost.
> - You may see multiple _Copied to clipboard_ notifications, if you have the _Output channel 'Clipboard' displays a notification message_ setting turned on (it's on by default).
> - `stdout` and `stderr` are mixed together in the order they are outputted in *realtime* mode. In *wait* mode they are grouped together so that either **all** `stdout` output comes first, and then comes **all** `stderr` output (or vice-versa, depending on settings).
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The output channel was created. ([#68](https://github.com/Taitava/obsidian-shellcommands/issues/68)).