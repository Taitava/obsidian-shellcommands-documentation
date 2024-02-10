---
cssclass: customiseTitle
---
# Event: File content modified
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `file` | `file-content-modified` |
## Execution
> [!Success] Executed when
> - A file's content is edited. The file must reside in the Obsidian vault.
> - The change may be done by Obsidian, or by an external application.
> - The file may be the currently focused file, or some other file in the vault.

> [!Fail] Not executed when
> - Any changes happen in `.obsidian` or any other folder starting with a dot `.`
> - Non-content related changes occur to a file, i.e. a file is renamed or moved to another folder. For these, see [[File renamed]] and [[File moved]].

> [!Important] Executed BEFORE Obsidian's metadata cache is updated
> In case you happen to use e.g. [[{{event_yaml_value}}]] variable in your shell command, and you modify the YAML front matter section of the current note, this event might execute the shell command **before** Obsidian updates the YAML information, and so [[{{event_yaml_value}}]] will give an **outdated** value.

> [!Warning] Warning: May cause frequent executions
> While a user writes to - or otherwise edits - files in Obsidian, Obsidian saves the changes very often to the file system. This may cause shell commands using this event to be executed multiple times during a short time. Also, external programs can edit multiple files at once, causing this event to trigger for every changed file.
> 
> To prevent redundant executions, it's recommended to use [[Events - debouncing|debouncing]] with this event. A good debouncing mode for this event could be [[Events - debouncing#Mode Cooldown first, then execute|Cooldown first, then execute]].

> [!Warning] Warning: May cause forever repeated executions
> If this event is used to execute commands that modify files in the vault (either the shell command itself or the output channel it uses), it will likely cause an infinite loop, because the modifications made by the shell command trigger this event to execute the same shell command again.
> 
> To avoid eternal modification loops, you can design your shell command in a way that will not react to all file modifications. This example if for [[Bash]]:
> ```bash
> if [ {{event_file_name}} != "OutputNote.md" ]
> then
>     echo "Hello world!" >> OutputNote.md
> fi
> ```
> The `if` condition breaks infinite loops by demanding that modifications to `OutputNote.md` must not cause further modifications. The requirement of this design is that a shell command must **not** modify **the same** file whose modifications it's reacting to.

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
The Obsidian event that powers this feature is [`modify` on `vault` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3260).

# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event was released. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-05-11 &#10132; 2024-02-03
> - [<small>2024-02-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cf515ff133396d89b8a365577e47dff6b7b894b7): [[File content modified.md]]: Mention debouncing in frequent executions warning.
> - [<small>2024-02-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7984c975a239604b8940c8165d3727a5001645a6): [[File content modified.md]]: Emphasize that the modified file can be any file in the vault.
> - [<small>2024-02-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/35079f682dcce7df20ec23c514d0a6c9d4da42a2): [[File content modified.md]]: An example for avoiding infinite modification loops.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/File%20content%20modified.md).
> ^page-edit-history