---
cssclass: customiseTitle
---
# Event: File moved
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `file` | `file-moved` |
## Execution
> [!Success] Executed when
> - A file has been moved inside the Obsidian vault. The moving needs to be done by Obsidian, otherwise this event won't notice it (see below).
> - Also executed when a folder containing files is moved (or renamed, which can be seen as moving a file from one folder to another). The event is then executed as many times as there are files in the folder.

> [!Fail] Not executed when
> - A file is located in `.obsidian` or any other folder starting with a dot `.`

![[Events - general principles#^file-folder-events-detection]]

## Variables

In addition to [[Variables - general principles#^normal-variables|normal variables]], the following variables are available during this event:

- [[{{event_file_extension}}]]
- [[{{event_file_name}}]]
- [[{{event_file_path}}]]
- [[{{event_folder_name}}]]
- [[{{event_folder_path}}]]
- [[{{event_old_file_path}}]]
- [[{{event_old_folder_name}}]]
- [[{{event_old_folder_path}}]]
- [[{{event_tags}}]]
- [[{{event_title}}]]
- [[{{event_yaml_value}}]]

**Note:** Accessing these variables outside an event that supports them will trigger an error message and prevent executing the shell command.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`rename` on `vault` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3268). In Obsidian API, the `rename` event handles both renames and moves. The *Shell commands* plugin makes it more precise, and detects whether the file has been moved or renamed, by checking if the file name has changed or not. This is why SC's both [[File moved]] and [[File renamed]] events are based on the same Obsidian API event.

# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event was released. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-05-11 &#10132; 2024-02-10
> - [<small>2024-02-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0ef4d4c717223599d69d32a92845bef694925026): Documentation for [[{{event_type}}]] variable.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/File%20moved.md).
> ^page-edit-history