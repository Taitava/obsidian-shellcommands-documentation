# All built-in variables

This page contains a list of all `{{variables}}` that are built-in to the *Shell commands* plugin. For information about what `{{variables}}` are and how to use them, please read [[Variables - general principles]].

## Normal variables
| Variable               | Availability                                                |
| ---------------------- | ----------------------------------------------------------- |
| [[{{caret_position}}]] | When a note pane is open.                                   |
| [[{{clipboard}}]]      | Always.                                                     |
| [[{{date}}]]           | Always.                                                     |
| [[{{file_extension}}]] | When a file is open.                                        |
| [[{{file_name}}]]      | When a file is open.                                        |
| [[{{file_path}}]]      | When a file is open.                                        |
| [[{{folder_name}}]]    | When a file is open.                                        |
| [[{{folder_path}}]]    | When a file is open.                                        |
| [[{{selection}}]]      | When a note pane is open in *editing view*.                 |
| [[{{tags}}]]           | When a note pane is open.                                   |
| [[{{title}}]]          | When a file is open.                                        |
| [[{{vault_path}}]]     | Always.                                                     |
| [[{{yaml_value}}]]     | When a note pane is open and a YAML frontmatter is defined. |
| [[{{workspace}}]]      | When the *Workspaces* core plugin is enabled.               |

# Event variables
These variables are only available when a shell command is executed by a specific event that supports the variables.

| Variable                      | Available during events                              |
| ----------------------------- | ---------------------------------------------------- |
| [[{{event_file_extension}}]]  | [[File menu]]                                        |
| [[{{event_file_name}}]]       | [[File menu]]                                        |
| [[{{event_file_path}}]]       | [[File menu]]                                        |
| [[{{event_folder_name}}]]     | [[File menu]], [[Folder menu]]                       |
| [[{{event_folder_path}}]]     | [[File menu]], [[Folder menu]]                       |
| [[{{event_old_file_name}}]]   | [[File renamed]]                                     |
| [[{{event_old_file_path}}]]   | [[File moved]], [[File renamed]]                     |
| [[{{event_old_folder_name}}]] | [[File moved]], [[Folder moved]]                     |
| [[{{event_old_folder_path}}]] | [[File moved]], [[Folder moved]], [[Folder renamed]] |
| [[{{event_old_title}}]]       | [[File renamed]]                                     |
| [[{{event_title}}]]           | [[File menu]]                                        |
| [[{{event_tags}}]]            | [[File menu]]                                        |

## When a variable is not available
Read about [[Default values|defining default values for variables]].