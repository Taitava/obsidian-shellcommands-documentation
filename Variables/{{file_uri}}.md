---
cssclass: customiseTitle
---
# Variable: `{{file_uri}}`
> [!Quote] {{file_uri}} described in the *Shell commands* plugin's settings
> Gives an Obsidian URI that opens the current file.

# URI details
%% Note: This section is dynamically shown in {{event_file_uri}} page, too, so make sure the content is valid for both of the variables. %%
- The URI uses [Obsidian's shorthand URI format](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI#Shorthand+formats) , so the resulting URI is like: `obsidian://vault/VAULT_NAME/path/to/note.md`.
- The file is always referred to by its relative path from the vault's root folder.
- The vault is always referred to by its name (= the vault's root folder's name). A possibility to use vault id as a reference might be added later, [if it's possible to get vault id's via Obsidian API](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI#Encoding.
- The file extension (e.g. `.md`, `.png`, `.pdf` etc.) is always included. Obsidian allows leaving it out when it's `.md`, but I've decided to always keep it.
- The vault name and file path values are properly [URI encoded](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI#Encoding).

# Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

# See also
- [[{{event_file_uri}}]]

# History
- [0.15.0 - 2022-08-20](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0150---2022-08-20): The variable was released. Idea by [catfist](https://github.com/catfist). ([#258](https://github.com/Taitava/obsidian-shellcommands/issues/258)).

> [!page-edit-history]- Page edit history: 2022-08-20 &#10132; 2022-08-20
> - [<small>2022-08-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/91fd9a4e2179cdd883ca563e76f57bfed72815b4): {{file_uri}} and {{event_file_uri}}: Mention that the idea came from catfist.
> - [<small>2022-08-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1a6dfee33a7690cbac10706fc1b064432c310bb2): 0.15.0 is released.
> - [<small>2022-08-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/77a2de80ce8655b41b595eda2ffe221ef2a36a02): New variables: {{file_uri}} and {{event_file_uri}}.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bfile_uri%7D%7D.md).
> ^page-edit-history