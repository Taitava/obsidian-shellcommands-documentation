# Event: Folder menu

## Executed when
When a user opens a folder context menu in the side navigation pane, all shell commands that have enabled this event, will be shown in the menu. A shell command is executed when a user clicks the shell command in the context menu.

![[Event-folder-menu.png]]

A menu item's name is the same as a shell command's [[alias]]. If no alias is set for the shell command, the actual command text will be used in the menu.

Shell command menu items do not currently show any icons, but [an ability to define an icon might be added later](https://github.com/Taitava/obsidian-shellcommands/discussions/25).

## Variables
In addition to [[Variables - general principles#^normal-variables|normal variables]], the following variables are available during this event:

- [[{{event_folder_name}}]]
- [[{{event_folder_path}}]]

**Tip:** These are similar variables as the normal variables that do not have the `event_` prefix, but they access a different folder:
 - The normal variables access a folder that is the parent of a file currently open in editor, while the `event_` prefixed variables refer to a folder in a navigation menu.
 - This allows you to utilize two different folders in a single shell command.

## Based on
The Obsidian event that powers this feature is [`file-menu` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3595). The same is used in the [[File menu]] event, although the menus have different contents.

## History
- #TODO: Add date. [0.10.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).