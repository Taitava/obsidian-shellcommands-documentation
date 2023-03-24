---
cssclass: customiseTitle
---
# Variable: `{{folder_name}}`
> [!Quote] {{folder_name}} described in the *Shell commands* plugin's settings
> Gives the current file's parent folder name, or a dot if the folder is the vault's root. No ancestor folders are included.

> [!Example] A dot `.` is given for the vault's root folder
If the folder is the root folder of the Obsidian vault, the variable gives a dot `.` in order to make the following types of path definitions work:
> 
> | Example situation | Old, problematic result (SC `0.17.0` and older) | Result with a dot (SC `0.18.0` and newer) |
> | ------------------ | ---------------------------- | ----------------------------- |
> | A file path where `{{folder_name}}` is one part, e.g. <span style="white-space: nowrap;">`echo "Content" > {{folder_name}}/NewNote.md`</span> | <span style="white-space: nowrap;">`echo "Content" > /NewNote.md`</span><br>Creates a file to the file system root, outside the Obsidian vault. | `echo "Content" > ./NewNote.md` <br>Creates a file correctly in the current working directory.|
> | When copying a directory, e.g. <span style="white-space: nowrap;">`cp -r {{folder_name}} /absolute/path/outside/the/vault`</span> | <span style="white-space: nowrap;">`cp -r  /absolute/path/outside/the/vault`</span><br>The first argument to `cp` is omitted because it was empty. | <span style="white-space: nowrap;">`cp -r . /absolute/path/outside/the/vault`</span><br>The first argument is correctly `.` so it's not accidentally omitted.|
> <small>(Before SC `0.18.0`, the variable returned an empty text for the vault's root folder.)</small> ^dot-examples

## Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_folder_name}}]]

# History
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): When the folder is the root folder of the vault, the variable now gives a dot `.` instead of an empty text. ([#304](https://github.com/Taitava/obsidian-shellcommands/issues/304)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was released.

> [!page-edit-history]- Page edit history: 2021-11-19 &#10132; 2023-01-06
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2cde8f14a2b8835509e6874315c74db3298cdb1b): {{folder_name}}.md: Fixed table borders (pipe symbols).
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4020bd503e26706f78c73bba87f472657c0054fe): {{folder_name}} and {{event_folder_name}}: Mention that the variables might now give a dot.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8610b6660a05e99d0cc0531db30ffde0bfc2fe8e): Variables: Add availability information.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62b9ff92e6c0ed82fb8d617b8644ba062cafa25a): Variables: add version history.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17cb062fae9850024325871b93694d81e5d67fa3): Documentation for each variable.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e5e64ba07d1979852b3f75f53ed3d1480ffdb09): Documentation for each variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bfolder_name%7D%7D.md).
> ^page-edit-history