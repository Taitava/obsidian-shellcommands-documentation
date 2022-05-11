# Event: File moved

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

## History
- #TODO: Add date. [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).