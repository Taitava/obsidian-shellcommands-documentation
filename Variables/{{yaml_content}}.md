---
cssclass: customiseTitle
---
# Variable: `{{yaml_content:with-dashes}}` or `{{yaml_content:no-dashes}}`
> [!Quote] {{yaml_content}} described in the *Shell commands* plugin's settings
> Gives the current note's [YAML frontmatter](https://help.obsidian.md/Advanced+topics/YAML+front+matter). Dashes `---` can be included or excluded.

## With dashes
`{{yaml_content:with-dashes}}` example:
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
`{{yaml_content:no-dashes}}` example:
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
> - When the active pane contains a file, not in graph view or other non-file view.
> - Also, a [YAML frontmatter](https://help.obsidian.md/Advanced+topics/YAML+front+matter) section needs to be present.

# See also
- [[{{file_content}}]]
- [[{{note_content}}]]
- [[{{event_yaml_content}}]]

# History
<small>This page was last modified on <strong>2023-01-06</strong> and created on 2023-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Byaml_content%7D%7D.md">See page edit history</a>.</small>
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): The variable was born. ([#267](https://github.com/Taitava/obsidian-shellcommands/issues/267)).