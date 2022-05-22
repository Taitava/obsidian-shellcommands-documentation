# Event: File content modified
==This feature is only available in a [0.13.0-beta.1 test](https://github.com/Taitava/obsidian-shellcommands/discussions/228). #TODO: Remove this annotation when the final version is released.== 
## Execution
> [!Success] Executed when
> - A file's content is edited. The file must reside in the Obsidian vault.
> - The change may be done by Obsidian, or by an external application.

> [!Fail] Not executed when
> - Any changes happen in `.obsidian` or any other folder starting with a dot `.`
> - Non-content related changes occur to a file, i.e. a file is renamed or moved to another folder. For these, see [[File renamed]] and [[File moved]].

> [!Important] Executed BEFORE Obsidian's metadata cache is updated
> In case you happen to use e.g. [[{{event_yaml_value}}]] variable in your shell command, and you modify the YAML front matter section of the current note, this event might execute the shell command **before** Obsidian updates the YAML information, and so [[{{event_yaml_value}}]] will give an **outdated** value.

> [!Warning] Warning: May cause frequent executions
> While a user writes to - or otherwise edits - files in Obsidian, Obsidian saves the changes very often to the file system. This may cause shell commands using this event to be executed multiple times during a short time.
> 
> **It is recommended not to execute any computationally heavy or long-running shell commands via this event.**

> [!Warning] Warning: May cause forever repeated executions
> If this event is used to execute commands that modify files in the vault (either the shell command itself or the output channel it uses), it will likely cause an infinite loop, because the modifications made by the shell command trigger this event to execute the same shell command again.
> 
> **It is recommended not to execute any file system altering shell commands via this event.**

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

## History
- #TODO: Add date. [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was born. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/123)).