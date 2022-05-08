# Event: Editor menu

## Executed when
When a user opens a file context menu in the side navigation pane, all shell commands that have enabled this event, will be shown in the menu. A shell command is executed when a user clicks the shell command in the context menu.

![[Event-editor-menu.png]]

A menu item's name is the same as a shell command's [[alias]]. If no alias is set for the shell command, the actual command text will be used in the menu.

Shell command menu items do not currently show any icons, but [an ability to define an icon might be added later](https://github.com/Taitava/obsidian-shellcommands/discussions/25).

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`editor-menu` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3601).

## History
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).