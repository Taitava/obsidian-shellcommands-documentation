---
aliases:
 - 
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

## History
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Added hotkeys for redirecting the output. Also, `Ctrl`/`Cmd` + clicking a button closes the modal. ([#145](https://github.com/Taitava/obsidian-shellcommands/issues/145)).
- [0.11.1 - 2022-03-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0111---2022-03-05): Fixed wrapping glitches: ([#172](https://github.com/Taitava/obsidian-shellcommands/issues/172))
	- Long shell commands were not wrapped to multiple lines.
	- When the window is narrow, redirection buttons were not wrapped to multiple lines. This fix also made the buttons wider, but smaller in height.
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26): If some text is selected, only the selected text will be used instead of the whole text. ([#158](https://github.com/Taitava/obsidian-shellcommands/issues/158)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The output channel was created. ([#134](https://github.com/Taitava/obsidian-shellcommands/issues/134)).