---
cssclass: customiseTitle
---
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
- [0.14.0 - 2022-07-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0140---2022-07-22): The variable was born. ([#235](https://github.com/Taitava/obsidian-shellcommands/issues/235)).

> [!page-edit-history]- Page edit history: 2022-07-16 &#10132; 2022-08-21
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5ad0dd8064c892901f885d7b2ab8037179f3c40d): Fix line endings.
> - [<small>2022-07-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5f492a6510449bdbf0a873382f08d7d7ef9863c3): 0.14.0 is released.
> - [<small>2022-07-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/12b7600cbffc94290e9fe54476b395cb93a02e7f): New variables: {{new_note_folder_name}} and {{new_note_folder_path}}.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bnew_note_folder_path%7D%7D.md).
> ^page-edit-history