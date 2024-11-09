---
cssclass: customiseTitle
---
# Variable: `{{event_yaml_values:property:separator}}`
> [!Quote] {{event_yaml_values}} described in the *Shell commands* plugin's settings
> Reads a list of values from the event related file's frontmatter. Takes a property name and separator as arguments. You can access nested properties with dot notation: property1.property2

![[{{yaml_value}}#Using dot notation to access nested properties]]

![[{{yaml_value}}#Accessing list values with numeric indexes]]

![[{{yaml_values}}#Examples]]

![[{{yaml_values}}#Key-value pairs (map objects) are not supported yet]]

![[{{yaml_values}}#Special characters in _separator_ are escaped]]
## Availability
> [!Warning] Only available:
> - In events: [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]].
> - Also, the given YAML property must exist in the file's frontmatter, and it must be a list instead of a single value.

## See also
- [[{{yaml_value}}]]
- [[{{yaml_values}}]]
- [[{{event_yaml_values}}]]

# History
- [0.23.0 - 2024-11-09](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0230---2024-11-09): The variable was released. ([#424](https://github.com/Taitava/obsidian-shellcommands/issues/424)).