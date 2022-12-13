# Event: File deleted
## Execution
> [!Success] Executed when
> - A file has been deleted from the Obsidian vault.
> - The deletion may be done by Obsidian, or by an external application.
> - Also executed when a folder containing files is deleted. The event is then executed as many times as there were files in the folder.

> [!Fail] Not executed when
> - A file is deleted in `.obsidian` or any other folder starting with a dot�`.`

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
The Obsidian event that powers this feature is [`delete` on `vault` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3264).

# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).