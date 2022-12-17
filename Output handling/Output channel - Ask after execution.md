---
aliases:
 - "Ask after execution"
cssclass: customiseTitle
---

---
# Output channel: Ask after execution
This channel creates a modal window that displays output from a shell command.
- Output can be manually redirected (=applied) to [[Output channels|other output channels]], even to multiple channels at once. Output can be discarded just by closing the modal.
- Output can be manually edited before the redirection, to do cleanup etc. The field is resizable.
- If you select text before clicking any of the redirection buttons, you can only use the selected part of the output text.
- If both `stdout` and `stderr` streams are channeled to the modal, it will display two output fields and two redirection control rows.
- If output is empty, no modal is shown.
- Displays the executed shell command's [[exit code]]. It's usually zero if the command succeeded.

**Good for:** Long output that takes time to read through.

![[Output-modal.png]]

## Hotkeys
- Each redirection button has a keyboard hotkey: `Ctrl`/`Cmd` + a letter. 
- Hitting `Ctrl`/`Cmd` + `Shift` + a letter closes the modal in addition to redirecting.
- `Ctrl`/`Cmd` + clicking a button does the same, redirects output and closes the modal.
- Hover over each redirection button with mouse to see its hotkey letter.

# Differences in *realtime* mode

If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.

> [!tldr] _Ask after execution_ - realtime mode differences:
> - You can edit early outputted text even when not all the output has been received. New output will go automatically to the bottom of the output textarea, regardless of your caret position.
> - *Exit code* will only show up after the shell command finishes execution. Before that, an *Executing...* text indicates that the process is still running. 
> - A stop icon can be clicked to terminate execution before it's finished:
>   ![[Icon-Terminate-execution-Ask-after-execution.png]]
>   (Sends a `SIGTERM` signal to the process.)
> ^differences-in-realtime

# History
<small>This page was last modified on <strong>2022-11-26</strong> and created on 2022-01-02. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Ask%20after%20execution.md">See page edit history</a>.</small>
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26):
	- The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
	- Added a button for terminating long-running shell commands - only appears in realtime mode. ([#289](https://github.com/Taitava/obsidian-shellcommands/issues/289)).
	- Fixed: Redirecting output content repeated possible output wrapping ([#278](https://github.com/Taitava/obsidian-shellcommands/issues/278)).
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): Hitting the `Enter` key in the modal now closes it, although it won't probably be used much, because it requires that the output text field is not focused. Also `Esc` key can be used for closing, which has always been possible. ([#216](https://github.com/Taitava/obsidian-shellcommands/issues/216)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Added hotkeys for redirecting the output. Also, `Ctrl`/`Cmd` + clicking a button closes the modal. ([#145](https://github.com/Taitava/obsidian-shellcommands/issues/145)).
- [0.11.1 - 2022-03-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0111---2022-03-05): Fixed line splitting glitches: ([#172](https://github.com/Taitava/obsidian-shellcommands/issues/172))
	- Long shell commands were not splitted to multiple lines.
	- When the window is narrow, redirection buttons were not splitted to multiple lines. This fix also made the buttons wider, but smaller in height.
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26): If some text is selected, only the selected text will be used instead of the whole text. ([#158](https://github.com/Taitava/obsidian-shellcommands/issues/158)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The output channel was created. ([#134](https://github.com/Taitava/obsidian-shellcommands/issues/134)).