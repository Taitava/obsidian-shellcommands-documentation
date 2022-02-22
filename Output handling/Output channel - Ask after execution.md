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

## History
- #TODO: Add date [0.11.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#): If some text is selected, only the selected text will be used instead of the whole text. ([#158](https://github.com/Taitava/obsidian-shellcommands/issues/158)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The output channel was created. ([#134](https://github.com/Taitava/obsidian-shellcommands/issues/134)).