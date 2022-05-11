# Variable: `{{event_old_file_name}}`
> [!Quote] {{event_old_file_name}} described in the *Shell commands* plugin's settings
> Gives the renamed/moved file's old name with a file extension. If you need it without the extension, use [[{{event_old_title}}]] instead.

# Availability
> [!Warning] Only available:
> In events: [[File renamed]]
> Not in [[File moved]], because the file **name** does not change in that event.

# See also
- [[{{event_file_name}}]]: Gives the file's current (aka *new*) name that it has after renaming.
- [[{{event_old_title}}]]: Gives the old file name without a file extension.

# History
- #TODO: Add a date [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).