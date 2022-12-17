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
> | A file path where `{{folder_name}}` is one part, e.g. <span style="white-space: nowrap;">`echo "Content" > {{folder_name}}/NewNote.md`</span> | <span style="white-space: nowrap;">`echo "Content" > /NewNote.md`</span><br>Creates a file to the file system root, outside the Obsidian vault. | `echo "Content" > ./NewNote.md` <br>Creates a file correctly in the current working directory.
> | When copying a directory, e.g. <span style="white-space: nowrap;">`cp -r {{folder_name}} /absolute/path/outside/the/vault`</span> | <span style="white-space: nowrap;">`cp -r  /absolute/path/outside/the/vault`</span><br>The first argument to `cp` is omitted because it was empty. | <span style="white-space: nowrap;">`cp -r . /absolute/path/outside/the/vault`</span><br>The first argument is correctly `.` so it's not accidentally omitted.
> <small>(Before SC `0.18.0`, the variable returned an empty text for the vault's root folder.)</small> ^dot-examples

## Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_folder_name}}]]

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2021-11-19. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bfolder_name%7D%7D.md">See page edit history</a>.</small>
- #TODO: Add a date [0.18.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): When the folder is the root folder of the vault, the variable now gives a dot `.` instead of an empty text. ([#304](https://github.com/Taitava/obsidian-shellcommands/issues/304)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was created.