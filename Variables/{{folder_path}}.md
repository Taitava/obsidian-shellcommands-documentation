# Variable: `{{folder_path:relative}}` or `{{folder_path:absolute}}`

> Gives path to the current file's parent folder, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

_(The above description can also be seen in the plugin's settings.)_

## Availability
> <strong>Only available</strong> when the active pane contains a file, not in graph view or other non-file view.

## History
- [0.4.1 - 2021-09-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#041---2021-09-29):
	- `{{folder_path:absolute}}`: Fixed missing leading `/` or `\` slash.
	- Fixed `\` being replaced by `/` on Windows.
	- [For those two, see #44](https://github.com/Taitava/obsidian-shellcommands/issues/44).
	- `{{folder_path:relative}}`: Fixed returning `/` when the current file is in vault root. Will return `.` instead. ([#52](https://github.com/Taitava/obsidian-shellcommands/issues/52)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was created.