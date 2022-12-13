# Variable: `{{folder_path:relative}}` or `{{folder_path:absolute}}`
> [!Quote] {{folder_path}} described in the *Shell commands* plugin's settings
> Gives path to the current file's parent folder, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

## Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_folder_path}}]]

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2021-11-19. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bfolder_path%7D%7D.md">See page edit history</a>.</small>
- [0.4.1 - 2021-09-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#041---2021-09-29):
	- `{{folder_path:absolute}}`: Fixed missing leading `/` or `\` slash.
	- Fixed `\` being replaced by `/` on Windows.
	- [For those two, see #44](https://github.com/Taitava/obsidian-shellcommands/issues/44).
	- `{{folder_path:relative}}`: Fixed returning `/` when the current file is in vault root. Will return `.` instead. ([#52](https://github.com/Taitava/obsidian-shellcommands/issues/52)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was created.