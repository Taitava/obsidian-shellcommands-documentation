# All built-in variables

This page contains a list of all `{{variables}}` that are built-in to the *Shell commands* plugin. For information about what `{{variables}}` are and how to use them, please read [[Variables - general principles]].

## Normal variables
- [[{{caret_position}}]]
- [[{{clipboard}}]]
- [[{{date}}]]
- [[{{file_extension}}]]
- [[{{file_name}}]]
- [[{{file_path}}]]
- [[{{folder_name}}]]
- [[{{folder_path}}]]
- [[{{selection}}]]
- [[{{tags}}]]
- [[{{title}}]]
- [[{{vault_path}}]]
- [[{{workspace}}]]
- [[{{yaml_value}}]]

# Event variables
These variables are only available when a shell command is executed by a specific event that supports the variables.

| Variable                     | Available during events        |
| ---------------------------- | ------------------------------ |
| [[{{event_file_extension}}]] | [[File menu]]                  |
| [[{{event_file_name}}]]      | [[File menu]]                  |
| [[{{event_file_path}}]]      | [[File menu]]                  |
| [[{{event_folder_name}}]]    | [[File menu]], [[Folder menu]] |
| [[{{event_folder_path}}]]    | [[File menu]], [[Folder menu]] |
| [[{{event_title}}]]          | [[File menu]]                  |
| [[{{event_tags}}]]           | [[File menu]]                  |