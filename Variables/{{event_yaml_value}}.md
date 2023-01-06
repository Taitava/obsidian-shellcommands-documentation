---
cssclass: customiseTitle
---
# Variable: `{{event_yaml_value}}`
> [!Quote] {{event_yaml_value}} described in the *Shell commands* plugin's settings
> Reads a single value from the event related file's frontmatter. Takes a property name as an argument. You can access nested properties with dot notation: property1.property2

## Availability
> [!Warning] Only available:
> - In events: [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]].
> - Also, the given YAML property must exist in the file's frontmatter.

## See also
- [[{{yaml_value}}]]

# History
<small>This page was last modified on <strong>2023-01-01</strong> and created on 2022-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bevent_yaml_value%7D%7D.md">See page edit history</a>.</small>
- [0.12.1 - 2022-05-16](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0121---2022-05-16): Fixed a bug that caused a wrong error message to be displayed when the desired YAML property was not found. The bug appeared in version `0.12.0` when support for [[default values]] was implemented. ([#220](https://github.com/Taitava/obsidian-shellcommands/issues/220)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Fixed a crash when the argument was empty. The bug appeared in version `0.10.0` when the variable was created. ([#181](https://github.com/Taitava/obsidian-shellcommands/issues/181)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The variable was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).