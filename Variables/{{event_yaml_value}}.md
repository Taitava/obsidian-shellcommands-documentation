---
cssclass: customiseTitle
---
# Variable: `{{event_yaml_value:property}}`
> [!Quote] {{event_yaml_value}} described in the *Shell commands* plugin's settings
> Reads a single value from the event related file's frontmatter. Takes a property name as an argument. You can access nested properties with dot notation: property1.property2

![[{{yaml_value}}#Using dot notation to access nested properties]]

![[{{yaml_value}}#Accessing list values with numeric indexes]]

## Availability
> [!Warning] Only available:
> - In events: [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]].
> - Also, the given YAML property must exist in the file's frontmatter.

## See also
- [[{{yaml_value}}]]
- [[{{yaml_values}}]]
- [[{{event_yaml_values}}]]

# History
- [0.12.1 - 2022-05-16](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0121---2022-05-16): Fixed a bug that caused a wrong error message to be displayed when the desired YAML property was not found. The bug appeared in version `0.12.0` when support for [[default values]] was implemented. ([#220](https://github.com/Taitava/obsidian-shellcommands/issues/220)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Fixed a crash when the argument was empty. The bug appeared in version `0.10.0` when the variable was released. ([#181](https://github.com/Taitava/obsidian-shellcommands/issues/181)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The variable was released. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-01-01 &#10132; 2024-11-03
> - [<small>2024-11-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2eaa0dd425ed6b1a993f417c5d278accdfaac01f): Pages for [[{{yaml_values}}]] and [[{{event_yaml_values}}]].
> - [<small>2024-11-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b4a056b01c9a10047467ffea63912227cd40be2d): [[{{event_yaml_value}}.md]]: Add information about dot notation and list indexes.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b7321d2509c80b5788d19c2ea080f035e94f7b94): {{yaml_value}} and {{event_yaml_value}}: Improve availability texts.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a2e619cfd3ae02a95d6bc76991e409cdf98ad5b1): Event variables: Add missing event references.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/473af76985ff3dbe0d2311fab301407fcf7152af): 0.12.1 is released.
> - [<small>2022-05-13</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/15d1b10ce1761ef37d094e9f4bf3a1ed9559dfd5): {{event_yaml_value}}: Add a record about a bug fix.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/845491f12242f672707c4d1a408547d41474416b): Event variables: Update descriptions according to new events.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-04-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0885db826a0ab3b09b05907bc4817bb520e3e2cb): {{yaml_value}}.md and {{event_yaml_value}}.md: Mark that bug #181 is fixed in 0.12.0.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3ca3ab49bb838e832ee435cb1427161cfa8c1444): Add event related variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bevent_yaml_value%7D%7D.md).
> ^page-edit-history