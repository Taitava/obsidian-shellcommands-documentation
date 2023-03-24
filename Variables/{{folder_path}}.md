---
cssclass: customiseTitle
---
# Variable: `{{folder_path:relative}}` or `{{folder_path:absolute}}`
> [!Quote] {{folder_path}} described in the *Shell commands* plugin's settings
> Gives path to the current file's parent folder, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

## Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_folder_path}}]]

# History
- [0.4.1 - 2021-09-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#041---2021-09-29):
	- `{{folder_path:absolute}}`: Fixed missing leading `/` or `\` slash.
	- Fixed `\` being replaced by `/` on Windows.
	- [For those two, see #44](https://github.com/Taitava/obsidian-shellcommands/issues/44).
	- `{{folder_path:relative}}`: Fixed returning `/` when the current file is in vault root. Will return `.` instead. ([#52](https://github.com/Taitava/obsidian-shellcommands/issues/52)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was released.

> [!page-edit-history]- Page edit history: 2021-11-19 &#10132; 2022-12-11
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8610b6660a05e99d0cc0531db30ffde0bfc2fe8e): Variables: Add availability information.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62b9ff92e6c0ed82fb8d617b8644ba062cafa25a): Variables: add version history.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17cb062fae9850024325871b93694d81e5d67fa3): Documentation for each variable.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e5e64ba07d1979852b3f75f53ed3d1480ffdb09): Documentation for each variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bfolder_path%7D%7D.md).
> ^page-edit-history