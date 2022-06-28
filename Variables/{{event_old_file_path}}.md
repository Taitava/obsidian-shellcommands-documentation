# Variable: `{{event_old_file_path:relative}}` or `{{event_old_file_path:absolute}}`
> [!Quote] {{event_old_file_path}} described in the *Shell commands* plugin's settings
> Gives the renamed/moved file's old path, either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

## Availability
> [!Warning] Only available:
> In events: [[File moved]], [[File renamed]]

## See also
- [[{{event_file_path}}]]: Gives the file's current (aka *new*) path that it has after moving/renaming.

## History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).