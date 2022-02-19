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

## Caret position definition
The output can also define where the caret should be positioned in the editor.
- E.g. `SomeFile.md:5` defines to place the caret on line 5.
- E.g. `SomeFile.md:5:6` defines to place the caret on line 5 and column 6.
- Negative indexes are not supported at the moment. Maybe in the future they could be used to refer to placing the caret at or near the end of the file. #TODO: Create an issue in GitHub and add a link.

## Open in a new pane
By default, the file will be opened in the currently active pane as long as it's not *pinned*. If the pane is *pinned* (= "locked"), then Obsidian will decide another pane where the file will be opened, which may be another already existing pane, or a completely new pane.

If you want to force creating a new pane, add `:new-pane`  to the end of the output. E.g. `MyNote.md:new-pane`.

## If the file does not exist
If you want to allow creating a file in case it does not exist, add `:can-create-file` to the end of the output. E.g. `MyNote.md:can-create-file`. If this flag is not present in the output, and if the file does not exist, the *Shell commands* plugin will cancel the operation and show an error message telling that new files cannot be created.

Preventing new file creation with this kind of flag is good in a situation where a shell command or script might accidentally output an incorrect file name.

## Combining different features
The output can contain all of the extra features that were mentioned in this page in addition to file path:
- Caret position
- `:new-pane`
- `:can-create-file`

The order of the features in the output is **almost** freely decidable, only the file path **must** come first. After that, the order of other features is not important.
- E.g. `MyNote.md:5:6:new-pane:can-create-file` works as well as `MyNote.md:can-create-file:new-pane:5:6`.
- All numeric parts are considered to mean a caret position.

## History
- #TODO: Add a date. [0.. - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The output channel was created. ([#143](https://github.com/Taitava/obsidian-shellcommands/issues/#143)).