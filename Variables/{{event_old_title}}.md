# Variable: `{{event_old_title}}`
> [!Quote] {{event_old_title}} described in the *Shell commands* plugin's settings
> Gives the renamed file's old name without a file extension. If you need it with the extension, use [[{{event_old_file_name}}]] instead.

# Availability
%% Use either this: %%
> [!Success] This variable is always available.

%% Or this: %%
> [!Warning] Only available:
> In events: [[File renamed]]
> Not in [[File moved]], because the file **name** does not change in that event.

# See also
- [[{{event_title}}]]: Gives the file's current (aka *new*) title that it has after renaming.
- [[{{event_old_file_name}}]]: Gives the old file name with a file extension.

# History
- #TODO: Add a date [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).