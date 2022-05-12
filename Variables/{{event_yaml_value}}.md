# Variable: `{{event_yaml_value}}`
> [!Quote] {{event_yaml_value}} described in the *Shell commands* plugin's settings
> Reads a single value from the event related file's frontmatter. Takes a property name as an argument. You can access nested properties with dot notation: property1.property2

## Availability
> <strong>Only available</strong> in events: [[File menu]].

## See also
- [[{{yaml_value}}]]

## History
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Fixed a crash when the argument was empty. The bug appeared in version `0.10.0` when the variable was created. ([#181](https://github.com/Taitava/obsidian-shellcommands/issues/181)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The variable was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).