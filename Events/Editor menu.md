---
cssclass: customiseTitle
---
# Event: Editor menu

## Execution
> [!Success] Executed when
> When a user opens a file context menu in the side navigation pane, all shell commands that have enabled this event, will be shown in the menu. A shell command is executed when a user clicks the shell command in the context menu.
> 
> ![[Event-editor-menu.png]]
> 
> A menu item's name is the same as a shell command's [[alias]]. If no alias is set for the shell command, the actual command text will be used in the menu.
> 
> Shell command menu items do not currently show any icons, but [an ability to define an icon might be added later](https://github.com/Taitava/obsidian-shellcommands/discussions/25).

> [!Warning]- Note: Values of [[Variables - general principles|{{variables}}]] might not show up in menus if Obsidian's _Native menus_ setting is on
> - If Obsidian's _Native menus_ setting is turned on, menu generating happens so fast that the _Shell commands_ plugin doesn't have enough time to parse [[Variables - general principles|{{variables}}]] in menu titles. I.e. you'll see the variables' names instead of actual content.
> - However, [[Variables - general principles|{{variables}}]] will work correctly in the actual shell command when it's executed, so this is just an annoyance rather than a practical problem.
> - **So, if you have this setting turned on:**
>     ![[Obsidian-native-menus-setting.png]]
> - **Then this is what you'll see in a menu:**
>     ![[Obsidian-native-menus-unparsed-variable.png]]
>     (`{{title}}}` should normally contain a note's file name without an extension.) ^obsidian-native-menus-warning

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`editor-menu` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3601).

# History
<small>This page was last modified on <strong>2023-01-22</strong> and created on 2022-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Editor%20menu.md">See page edit history</a>.</small>
- [0.18.1 - 2023-01-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0181---2023-01-22): Fixed: Menu items appeared without text on macOS. ([#314](https://github.com/Taitava/obsidian-shellcommands/issues/314)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).