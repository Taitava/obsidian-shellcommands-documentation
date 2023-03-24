---
cssclass: customiseTitle
---
# All built-in variables

This page contains a list of all `{{variables}}` that are built-in to the *Shell commands* plugin. For information about what `{{variables}}` are and how to use them, please read [[Variables - general principles]].

## Normal variables
| Variable                     | Availability                                                |
| ---------------------------- | ----------------------------------------------------------- |
| [[{{caret_paragraph}}]]      | When a note pane is open.                                   |
| [[{{caret_position}}]]       | When a note pane is open.                                   |
| [[{{clipboard}}]]            | Always.                                                     |
| [[{{date}}]]                 | Always.                                                     |
| [[{{file_content}}]]         | When a file is open.                                        |
| [[{{file_extension}}]]       | When a file is open.                                        |
| [[{{file_name}}]]            | When a file is open.                                        |
| [[{{file_path}}]]            | When a file is open.                                        |
| [[{{file_uri}}]]             | When a file is open.                                        |
| [[{{folder_name}}]]          | When a file is open.                                        |
| [[{{folder_path}}]]          | When a file is open.                                        |
| [[{{new_note_folder_name}}]] | Always.                                                     |
| [[{{new_note_folder_path}}]] | Always.                                                     |
| [[{{note_content}}]]         | When a file is open.                                        |
| [[{{selection}}]]            | When a note pane is open in *editing view*.                 |
| [[{{tags}}]]                 | When a note pane is open.                                   |
| [[{{title}}]]                | When a file is open.                                        |
| [[{{vault_path}}]]           | Always.                                                     |
| [[{{yaml_content}}]]         | When a note pane is open and a YAML frontmatter is defined. |
| [[{{yaml_value}}]]           | When a note pane is open and a YAML frontmatter is defined. |
| [[{{workspace}}]]            | When the *Workspaces* core plugin is enabled.               |

## Event variables
These variables are only available when a shell command is executed by a specific event that supports the variables.

| Variable                      | Available during events                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[{{event_file_content}}]]    | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_file_extension}}]]  | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_file_name}}]]       | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_file_path}}]]       | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_file_uri}}]]        | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_folder_name}}]]     | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]],<br>[[Folder menu]], [[Folder created]], [[Folder deleted]], [[Folder moved]], [[Folder renamed]] |
| [[{{event_folder_path}}]]     | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]],<br>[[Folder menu]], [[Folder created]], [[Folder deleted]], [[Folder moved]], [[Folder renamed]] |
| [[{{event_note_content}}]]    | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_old_file_name}}]]   | [[File renamed]]                                                                                                                                                                                                 |
| [[{{event_old_file_path}}]]   | [[File moved]], [[File renamed]]                                                                                                                                                                                 |
| [[{{event_old_folder_name}}]] | [[File moved]], [[Folder moved]]                                                                                                                                                                                 |
| [[{{event_old_folder_path}}]] | [[File moved]], [[Folder moved]], [[Folder renamed]]                                                                                                                                                             |
| [[{{event_old_title}}]]       | [[File renamed]]                                                                                                                                                                                                 |
| [[{{event_tags}}]]            | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_title}}]]           | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_yaml_content}}]]    | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                                                                                   |
| [[{{event_yaml_value}}]]    | [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]                                       |                                                                                                                                                                                                                  |

## Special purpose variables

This list contains variables that are usually used somewhere else than in actual shell commands.

| Variable            | Availability                                                                                                                                                                        |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[{{environment}}]] | Usually used in [[Additions to the PATH environment variable#An easier way to add directories to PATH\|PATH additions]]. Available, if the passed environment variable name exists. |
| [[{{output}}]]      | In [[Output wrappers\|output wrappers]], cannot be used as input for shell commands.                                                                                                |
| [[{{shell_command_content}}]] | In [[Settings for custom shells|custom shell settings]] : for defining shell arguments, or a shell command wrapper. |

## When a variable is not available
Read about [[Default values|defining default values for variables]].

# History


> [!page-edit-history]- Page edit history: 2022-05-08 &#10132; 2023-03-23
> - [<small>2023-03-23</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/07644d90d4a01c20fd0a151a7fec543000df0a54): Documentation for {{shell_command_content}}.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e47cc468318c9508af6883489793dcdcf3e5ca4a): All variables.md: Add missing {{event_yaml_value}}
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/13cb8b33b0c260833240f024cb4cb20f52717fbe): All variables.md: Fix table spacing.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/265fbffa086a29cdabb125380c773b1060a682ee): New variables {{yaml_content}} and {{event_yaml_content}}.
> - [<small>2022-11-04</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8966b2f59d3695f807025df90b5c34142b7e4845): Add {{caret_paragraph}} variable.
> - [<small>2022-09-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/790d38b8cb8f9299abd93e2b6e3f39e114e46294): {{file_content}} and {{event_file_content}} variables.
> - [<small>2022-09-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/57eab54eef74305f6ee9868344249ae79115c699): {{note_content}} and {{event_note_content}} variables.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fd9edbf69c25863a39526cf3fe00077625f6a01d): Output wrappers.
> - [<small>2022-08-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5cf7c0763debabf3ff09e304f1ad709cd0c262e5): All variables.md: {{environment}} was forgotten from the list.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/36d7f8916e7a75ee3a3faed95a88b60ab5dfd4b2): All variables.md: Put {{event_title}} and {{event_tags}} in correct order.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a2e619cfd3ae02a95d6bc76991e409cdf98ad5b1): Event variables: Add missing event references.
> - [<small>2022-08-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/77a2de80ce8655b41b595eda2ffe221ef2a36a02): New variables: {{file_uri}} and {{event_file_uri}}.
> - [<small>2022-07-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/12b7600cbffc94290e9fe54476b395cb93a02e7f): New variables: {{new_note_folder_name}} and {{new_note_folder_path}}.
> - [<small>2022-07-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb4e3da794b9bd1fb01e2d432361217ca09e85bb): All variables.md: Fix 'Event variables' heading level.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cccb2b1e0ce4f86ccefc6831f13ba119ef8c30ab): All variables.md: Convert 'Normal variables' list to a table.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/All%20variables.md).
> ^page-edit-history