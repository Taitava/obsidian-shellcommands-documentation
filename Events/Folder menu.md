---
cssclass: customiseTitle
---
# Event: Folder menu

## Execution
> [!Success] Executed when
> When a user opens a folder context menu in the side navigation pane, all shell commands that have enabled this event, will be shown in the menu. A shell command is executed when a user clicks the shell command in the context menu.
> 
> ![[Event-folder-menu.png]]
> 
> A menu item's name is the same as a shell command's [[alias]]. If no alias is set for the shell command, the actual command text will be used in the menu.
> 
> Shell command menu items do not currently show any icons, but [an ability to define an icon might be added later](https://github.com/Taitava/obsidian-shellcommands/discussions/25).

![[Editor menu#^obsidian-native-menus-warning]]

## Variables
In addition to [[All variables#Normal variables|normal variables]], the following variables are available during this event:

- [[{{event_folder_name}}]]
- [[{{event_folder_path}}]]

**Tip:** These are similar variables as the normal variables that do not have the `event_` prefix, but they access a different folder:
 - The normal variables access a folder that is the parent of a file currently open in editor, while the `event_` prefixed variables refer to a folder in a navigation menu.
 - This allows you to utilize two different folders in a single shell command.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`file-menu` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3595). The same is used in the [[File menu]] event, although the menus have different contents.

# History
- [0.18.1 - 2023-01-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0181---2023-01-22): Fixed: Menu items appeared without text on macOS. ([#314](https://github.com/Taitava/obsidian-shellcommands/issues/314)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-01-01 &#10132; 2023-03-12
> - [<small>2023-03-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/100c87e8b6aade32c84dd8416cd06ce010118711): Menu events: Add a note about Obsidian's "Native menus" setting.
> - [<small>2023-01-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d920e787236965331f1b1fc7d1341a86df53cbd3): 0.18.1 history records.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3b3db94cf15a6c0b1af609ff00e6289e565393e7): Events: Use callouts for the 'Executed when' sections.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/89c649149543fc253fb088b0a1c174138be9f1a1): Events: Add 'Examples' section.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f4726bdfe26ab568d853e54794d171ddd8290dc4): Events: Folder menu: Add a list of event variables.
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/13c1f6a730fafb892c14d6598b58592b3bdb5fc0): Typo fixes.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Folder%20menu.md).
> ^page-edit-history