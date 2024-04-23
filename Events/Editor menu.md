---
cssclass: customiseTitle
---
# Event: Editor menu
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `menu` | `editor-menu-item` |
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
- [0.18.1 - 2023-01-22](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0181---2023-01-22): Fixed: Menu items appeared without text on macOS. ([#314](https://github.com/Taitava/obsidian-shellcommands/issues/314)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was released. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).


> [!page-edit-history]- Page edit history: 2022-01-01 &#10132; 2024-02-10
> - [<small>2024-02-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0ef4d4c717223599d69d32a92845bef694925026): Documentation for [[{{event_type}}]] variable.
> - [<small>2023-03-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/100c87e8b6aade32c84dd8416cd06ce010118711): Menu events: Add a note about Obsidian's "Native menus" setting.
> - [<small>2023-01-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d920e787236965331f1b1fc7d1341a86df53cbd3): 0.18.1 history records.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3b3db94cf15a6c0b1af609ff00e6289e565393e7): Events: Use callouts for the 'Executed when' sections.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/89c649149543fc253fb088b0a1c174138be9f1a1): Events: Add 'Examples' section.
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/13c1f6a730fafb892c14d6598b58592b3bdb5fc0): Typo fixes.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/Editor%20menu.md).
> ^page-edit-history