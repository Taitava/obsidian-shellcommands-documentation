# Variable: `{{event_old_folder_path:relative}}` or `{{event_old_folder_path:absolute}}`
==This feature is only available in a [0.13.0-beta.1 test](https://github.com/Taitava/obsidian-shellcommands/discussions/228). #TODO: Remove this annotation when the final version is released.==
> [!Quote] {{event_old_folder_path}} described in the *Shell commands* plugin's settings
> File events: Gives the moved file's old parent folder's path.
> Folder events: Gives the renamed/moved folder's old path.
> The path is either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

# Availability
> [!Warning] Only available:
> In events. [[File moved]], [[Folder moved]], [[Folder renamed]]
> Not in [[File renamed]], because the file **location** does not change in that event.

# See also
- [[{{event_folder_path}}]]: Gives the folder's current (aka *new*) path that it has after moving/renaming.

# History
- #TODO: Add a date [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).