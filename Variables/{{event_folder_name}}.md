---
cssclass: customiseTitle
---
# Variable: `{{event_folder_name}}`
> [!Quote] {{event_folder_name}} described in the *Shell commands* plugin's settings
> File events: Gives the event related file's parent folder name.
> Folder events: Gives the selected folder's name.
> Gives a dot if the folder is the vault's root. No ancestor folders are included.

![[{{folder_name}}#^dot-examples]]

## Availability
> [!Warning] Only available:
> In events: [[File menu]], [[Folder menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]], [[Folder created]], [[Folder deleted]], [[Folder moved]], [[Folder renamed]].

## See also
- [[{{folder_name}}]]

# History
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): When the folder is the root folder of the vault, the variable now gives a dot `.` instead of an empty text. ([#304](https://github.com/Taitava/obsidian-shellcommands/issues/304)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The variable was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-01-01 &#10132; 2023-01-06
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4020bd503e26706f78c73bba87f472657c0054fe): {{folder_name}} and {{event_folder_name}}: Mention that the variables might now give a dot.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a2e619cfd3ae02a95d6bc76991e409cdf98ad5b1): Event variables: Add missing event references.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/845491f12242f672707c4d1a408547d41474416b): Event variables: Update descriptions according to new events.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3ca3ab49bb838e832ee435cb1427161cfa8c1444): Add event related variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bevent_folder_name%7D%7D.md).
> ^page-edit-history