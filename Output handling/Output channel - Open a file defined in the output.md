---
aliases:
 - "Open a file"
 - "Open file"
---
# Output channel: Open a file defined in the output
This output channel expects that the output of a shell command is a file name or path in the Obsidian vault. The file will be opened in Obsidian.

**This output channel is not available for `stderr`**, because error messages can be unpredictable.

## Accepted file definitions
- A file name with an extension, e.g. *MyNote.md* or *MyImage.png*.
- A file name without an extension, e.g. *MyNote*. Only applicable for markdown note files, not for e.g. images, PDFs or other files.
- An absolute or relative path to a file. The file must reside in the vault.
- The file must exist. Creating new files is not supported at the moment, but might become supported later. #TODO: Create an issue in GitHub and add a link.

## Caret position definition
The output can also define where the caret should be positioned in the editor.
- E.g. `SomeFile.md:5` defines to place the caret on line 5.
- E.g. `SomeFile.md:5:6` defines to place the caret on line 5 and column 6.
- Negative indexes are not supported at the moment. Maybe in the future they could be used to refer to placing the caret at or near the end of the file. #TODO: Create an issue in GitHub and add a link.

## History
- #TODO: Add a date. [0.. - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The output channel was created. ([#143](https://github.com/Taitava/obsidian-shellcommands/issues/#143)).