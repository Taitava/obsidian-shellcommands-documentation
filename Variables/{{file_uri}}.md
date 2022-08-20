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
- [0.15.0 - 2022-08-20](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0150---2022-08-20): The variable was born. Idea by [catfist](https://github.com/catfist). ([#258](https://github.com/Taitava/obsidian-shellcommands/issues/258)).