# Variable: `{{new_note_folder_name}}`
> [!Quote] {{new_note_folder_name}} described in the *Shell commands* plugin's settings
> Gives the folder name for *Default location for new notes* (a setting in Obsidian). No ancestor folders are included.

The *Default location for new notes* setting in Obsidian has three possible options:
- *Vault folder*: In this case, the variable gives just a dot `.` instead of the vault folder's name to indicate that this is not a subfolder.
- *Same folder as current file*: In this case, gives the same as [[{{folder_name}}]].
- *In the folder specified below*: Gives the freely specified folder's name.

This variable is handy e.g. when you execute shell commands that generate new files, and you want them to be always located in the same folder where Obsidian creates new note files. If you change the setting in Obsidian later, you don't need to change the shell command.

# Availability
> [!Success] This variable is always available.

# See also
- [[{{new_note_folder_path}}]]

# History
<small>This page was last modified on <strong>2022-07-22</strong> and created on 2022-07-16. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bnew_note_folder_name%7D%7D.md">See page edit history</a>.</small>
- [0.14.0 - 2022-07-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0140---2022-07-22): The variable was born. ([#235](https://github.com/Taitava/obsidian-shellcommands/issues/235)).