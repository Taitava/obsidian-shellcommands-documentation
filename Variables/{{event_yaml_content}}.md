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
- [0.21.0 - 2023-12-30](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0210---2023-12-30): Prevent a crash when using the variable in Obsidian version `>= 1.4.0`. No practical changes in behavior. ([#372](https://github.com/Taitava/obsidian-shellcommands/issues/372)).
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): The variable was released. ([#267](https://github.com/Taitava/obsidian-shellcommands/issues/267)).

> [!page-edit-history]- Page edit history: 2023-01-01 &#10132; 2023-12-30
> - [<small>2023-12-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/88a58d8b5359f98cd1e385f569f85ae3c948b739): [[{{note_content}}]], [[{{yaml_content}}]], [[{{event_note_content}}]] and [[{{event_yaml_content}}]] are now compatible with Obsidian `>= 1.4.0`.
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/265fbffa086a29cdabb125380c773b1060a682ee): New variables {{yaml_content}} and {{event_yaml_content}}.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bevent_yaml_content%7D%7D.md).
> ^page-edit-history