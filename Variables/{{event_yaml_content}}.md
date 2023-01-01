---
cssclass: customiseTitle
---
# Variable: `{{event_yaml_content:with-dashes}}` or `{{event_yaml_content:no-dashes}}`
> [!Quote] {{event_yaml_content}} described in the *Shell commands* plugin's settings
> Gives the event related note's [YAML frontmatter](https://help.obsidian.md/Advanced+topics/YAML+front+matter). Dashes `---` can be included or excluded.

## With dashes
`{{event_yaml_content:with-dashes}}` example:
```yaml
---
key: value
key2: value2
key3: [one, two, three]
key4:
- four
- five
- six
---
```

The top and bottom dashes `---` are included.

## Without dashes
`{{event_yaml_content:no-dashes}}` example:
```yaml
key: value
key2: value2
key3: [one, two, three]
key4:
- four
- five
- six
```

No dashes `---` are included.

# Availability
> [!Warning] Only available:
> - In events: [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]
> - Also, a [YAML frontmatter](https://help.obsidian.md/Advanced+topics/YAML+front+matter) section needs to be present.

# See also
- [[{{event_file_content}}]]
- [[{{event_note_content}}]]
- [[{{yaml_content}}]]

# History
- #TODO: Add a date [0.18.0 - 2023--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#267](https://github.com/Taitava/obsidian-shellcommands/issues/267)).