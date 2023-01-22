---
cssclass: customiseTitle
---
# Event: File menu

## Execution
> [!Success] Executed when
> 1. When a user opens a file context menu in the side navigation pane, all shell commands that have enabled this event, will be shown in the menu. A shell command is executed when a user clicks the shell command in the context menu.
> 
> ![[Event-file-menu.png]]
> 
> A menu item's name is the same as a shell command's [[alias]]. If no alias is set for the shell command, the actual command text will be used in the menu.
> 
> 2. When a user right clicks a link in the editor, all shell commands that have enabled this event, will be shown in the link's menu. This works exactly the same way as in the file navigation menu:
> 
> ![[Event-file-menu-on-a-link.png]]
> 
> Shell command menu items do not currently show any icons, but [an ability to define an icon might be added later](https://github.com/Taitava/obsidian-shellcommands/discussions/25).
> 
> 3. Also works in search: When a search result is right clicked, all shell commands that have enabled this event, will be shown in the context menu related to that search result. #TODO: Add a screenshot.

## Variables
In addition to [[All variables#Normal variables|normal variables]], the following variables are available during this event:

- [[{{event_file_extension}}]]
- [[{{event_file_name}}]]
- [[{{event_file_path}}]]
- [[{{event_folder_name}}]]
- [[{{event_folder_path}}]]
- [[{{event_tags}}]]
- [[{{event_title}}]]
- [[{{event_yaml_value}}]]

**Tip:** These are similar variables as the normal variables that do not have the `event_` prefix, but they access a different file/folder:
 - The normal variables access a file that is currently open in editor, while the `event_` prefixed variables refer to a file in a navigation menu.
 - This allows you to utilize two different files in a single shell command, e.g. merge two files' contents together, or open an external [file comparison application](https://en.wikipedia.org/wiki/File_comparison) to see differences/similarities between two files.

**Note:** Accessing these variables outside of an event that supports them will trigger an error message and prevent executing the shell command.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`file-menu` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3595). The same is used in the [[Folder menu]] event, although the menus have different contents.

# History
<small>This page was last modified on <strong>2023-01-22</strong> and created on 2022-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/File%20menu.md">See page edit history</a>.</small>
- [0.18.1 - 2023-01-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0181---2023-01-22): Fixed: Menu items appeared without text on macOS. ([#314](https://github.com/Taitava/obsidian-shellcommands/issues/314)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).