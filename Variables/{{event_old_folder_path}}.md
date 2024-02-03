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
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The variable was released. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).

> [!page-edit-history]- Page edit history: 2022-05-11 &#10132; 2022-09-01
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/02e98b52d70617d390d8b1dbfda581c9e03151bd): Prompts.md and {{event_old_folder_path}}.md: Typo fixes.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c717046e4c7e3b4e16cbe008fe05137550fbd1e7): {{event_old_folder_path}}.md: Fix the heading.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/71d62712b8fcb4d75eb82e2c59461e991365805d): Event variables: Small fixes in descriptions.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bevent_old_folder_path%7D%7D.md).
> ^page-edit-history