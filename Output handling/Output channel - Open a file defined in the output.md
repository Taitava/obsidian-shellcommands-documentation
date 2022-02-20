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
- Negative indexes are also supported. E.g. `SomeFile.md:-1:-1` places the caret at the last column on the last line of the file.
- Caret positioning is delayed to happen **500 milliseconds after** opening the file. This makes a small, noticeable pause, but it helps to ensure correct editor scrolling in situations where a file might render slowly after opening: e.g. images and embedded blocks of content may change the height of the content just after opening a file. That's why scrolling to the desired place is delayed. The delay cannot be adjusted at the moment, but a setting for this might be added later.

# Select text
In addition to defining caret position, you can also define ranges of text to be selected.
- E.g. `SomeFile.md:5:1:10:-1` selects text between the first character of line 5, and last character of line 10.
- E.g. `SomeFile.md:5:1:10:-1:20:1:25:-1` creates two selections, with the first one being the same as above, and the second selection being from the beginning of line 20 till the end of line 25.
- The amount of selections is not limited.

### A summary for the amount of numeric parts in the output
- No numeric parts: caret positioning will not be done, Obsidian or other plugins may freely decide the position.
- 1 part: Defines a line for the caret. No selection. The caret will be placed at the beginning of the line.
- 2 parts: Defines a line and column for the caret. No selection.
- 3 parts: Not allowed.
- 4 parts: Defines a selection between two positions.
- More than four parts: Defines multiple selections, but the amount of parts must be dividable into groups of four. 

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

## Absolute paths on Windows
As Windows uses the colon `:` in absolute file paths (e.g. `C:\...`), and colon is also used by this output channel to separate different parts of output from each other, the output channel tries to be clever to notice when a colon `:` is used as a file path component and when as a part delimiter.
- E.g. `C:\path\to\Obsidian\vault\MyNote.md:new-pane` is correctly interpreted so that `C` and `\path\to\Obsidian\vault\MyNote.md` combined together do form an **absolute path**, and so they should be considered as a single part rather than two parts.
- E.g. `MyNote.md:new-pane` is correctly interpreted so that `MyNote.md` and `new-pane` are different parts.
- This inspection happens only on Windows systems, not on other platforms.

## History
- #TODO: Add a date. [0.. - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The output channel was created. ([#143](https://github.com/Taitava/obsidian-shellcommands/issues/#143)).