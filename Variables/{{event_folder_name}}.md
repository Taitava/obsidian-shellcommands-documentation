---
cssclass: customiseTitle
---
# Variable: `{{event_folder_name}}`
> [!Quote] {{event_folder_name}} described in the *Shell commands* plugin's settings
> File events: Gives the event related file's parent folder name.
> Folder events: Gives the selected folder's name.
> Gives a dot if the folder is the vault's root. No ancestor folders are included.

![[{{folder_name}}#^dot-examples]]

## Availability
> [!Warning] Only available:
> In events: [[File menu]], [[Folder menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]], [[Folder created]], [[Folder deleted]], [[Folder moved]], [[Folder renamed]].

## See also
- [[{{folder_name}}]]

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2022-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bevent_folder_name%7D%7D.md">See page edit history</a>.</small>
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): When the folder is the root folder of the vault, the variable now gives a dot `.` instead of an empty text. ([#304](https://github.com/Taitava/obsidian-shellcommands/issues/304)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The variable was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).