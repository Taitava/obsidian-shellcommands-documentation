# Variable: `{{new_note_folder_path:relative}}` or `{{new_note_folder_path:absolute}}`
> [!Quote] {{new_note_folder_name}} described in the *Shell commands* plugin's settings
> Gives path to the *Default location for new notes* folder (a setting in Obsidian), either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

The *Default location for new notes* setting in Obsidian has three possible options:
- *Vault folder*: If mode is `relative`, gives just a dot `.` instead of the vault folder's name to indicate that this is not a subfolder. If mode is `absolute`, gives the same as [[{{vault_path}}]].
- *Same folder as current file*: In this case, gives the same as [[{{folder_path}}]].
- *In the folder specified below*: Gives the freely specified folder's path.

This variable is handy e.g. when you execute shell commands that generate new files, and you want them to be always located in the same folder where Obsidian creates new note files. If you change the setting in Obsidian later, you don't need to change the shell command.

# Availability
> [!Success] This variable is always available.

# See also
- [[{{new_note_folder_name}}]]

# History
- #TODO: Add a date [0.. - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#235](https://github.com/Taitava/obsidian-shellcommands/issues/235)).