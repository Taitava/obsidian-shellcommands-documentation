---
cssclass: customiseTitle
---
# Variable: `{{event_old_folder_path:relative}}` or `{{event_old_folder_path:absolute}}`
> [!Quote] {{event_old_folder_path}} described in the *Shell commands* plugin's settings
> File events: Gives the moved file's old parent folder's path.
> Folder events: Gives the renamed/moved folder's old path.
> The path is either as absolute from the root of the file system, or as relative from the root of the Obsidian vault.

# Availability
> [!Warning] Only available:
> In events: [[File moved]], [[Folder moved]], [[Folder renamed]]
> Not in [[File renamed]], because the file **location** does not change in that event.

# See also
- [[{{event_folder_path}}]]: Gives the folder's current (aka *new*) path that it has after moving/renaming.

# History
<small>This page was last modified on <strong>2022-09-01</strong> and created on 2022-05-11. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bevent_old_folder_path%7D%7D.md">See page edit history</a>.</small>
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The variable was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).