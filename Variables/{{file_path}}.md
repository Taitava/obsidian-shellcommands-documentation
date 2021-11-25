# Variable: `{{file_path:relative}}` or `{{file_path:absolute}}`

> Gives path to the current file, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

_(The above description can also be seen in the plugin's settings.)_

## History
- [0.4.1 - 2021-09-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#041---2021-09-29):
	- `{{file_path:absolute}}`: Fixed missing leading `/` or `\` slash.
	- Fixed `\` being replaced by `/` on Windows.
	- [See #44](https://github.com/Taitava/obsidian-shellcommands/issues/44).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was created.