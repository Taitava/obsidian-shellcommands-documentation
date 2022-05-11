# Variable: `{{event_old_folder_name}}`
> [!Quote] {{event_old_folder_name}} described in the *Shell commands* plugin's settings
> File events: Gives the moved file's old parent folder's name.
> Folder events: Gives the renamed folder's old name.

# Availability
> [!Warning] Only available:
> In events: [[File moved]], [[Folder renamed]]
> Not in [[File renamed]], because the file **location** does not change in that event.
> Not in [[Folder moved]], because the folder **name** does not change in that event.

# See also
- [[{{event_folder_name}}]]: Gives the folder's current (aka *new*) name that it has after renaming.

# History
- #TODO: Add a date [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).