---
cssclass: customiseTitle
---
# Event: File created
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `file` | `file-created` |
## Execution
> [!Success] Executed when
> - A new file has been created in the Obsidian vault.
> - The file may be created by Obsidian, or by an external application.

> [!Fail] Not executed when
> - A file is created in `.obsidian` or any other folder starting with a dot `.`

![[Events - general principles#^file-folder-events-detection]]

## Variables

In addition to [[Variables - general principles#^normal-variables|normal variables]], the following variables are available during this event:

- [[{{event_file_extension}}]]
- [[{{event_file_name}}]]
- [[{{event_file_path}}]]
- [[{{event_folder_name}}]]
- [[{{event_folder_path}}]]
- [[{{event_tags}}]]
- [[{{event_title}}]]
- [[{{event_yaml_value}}]]

**Note:** Accessing these variables outside an event that supports them will trigger an error message and prevent executing the shell command.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`create` on `vault` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3256).

# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event was released. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-05-11 &#10132; 2022-12-11
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/File%20created.md).
> ^page-edit-history