---
cssclass: customiseTitle
---
# Variable: `{{yaml_value}}`
> [!Quote] {{yaml_value}} described in the *Shell commands* plugin's settings
> Reads a single value from the current file's frontmatter. Give a property name as an argument. You can access nested properties with dot notation: property1.property2

## Using dot notation to access nested properties

Nested properties can be accessed with a dot `.` notation:
```YAML
---
cssclass: some-class
book_details:
  author: "Me!"
  title: "My life"
  description: "A miserable story......"
  chapters:
    first: "Birth"
    second: "Childhood"
    third: "Etc..."
---
```
The value of the first chapter can be retrieved with `{{yaml_value:book_details.chapters.first}}`. This gives *Birth*.

## Accessing list values with numeric indexes

List items can be accessed like this:
```YAML
---
cssclass: some-class
tags:
  - first-tag
  - second-tag
---
```

First tag: `{{yaml_value:tags.0}}` gives *first-tag*.
Second tag: `{{yaml_value:tags.1}}` gives *second-tag*.
So lists are 0-indexed!
**Note that for [Obsidian tags](https://help.obsidian.md/How+to/Working+with+tags), you cannot access inline tags with this variable - only tags that are defined in the YAML frontmatter.**

### Also negative indexes are supported
Last tag: `{{yaml_value:tags.-1}}` gives *second-tag*.

### Get list length
Count tags that appear in YAML: `{{yaml_value:tags.length}}` gives *2*. (No inline tags included). Note that this is only supported for lists, not key value pairs:
```YAML
---
ordered_list_has_a_length_property:
  - first-tag
  - second-tag

key_value_pair_list_does_not_have_a_length_property:
  key1: value1
  key2: value2
---
```
The `length` property comes from the Obsidian API, it's not any kind of custom feature of the *Shell commands* plugin.

## Availability
> [!Warning] Only available:
> - When the active pane contains a file, not in graph view or other non-file view.
> - Also, the given YAML property must exist in the file's frontmatter.

## See also
- [[{{event_yaml_value}}]]

# History
<small>This page was last modified on <strong>2023-01-01</strong> and created on 2021-12-10. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Byaml_value%7D%7D.md">See page edit history</a>.</small>
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Fixed a crash when the argument was empty. The bug appeared in version `0.10.0` at the same time when variable `{{event_yaml_value}}` was created. ([#181](https://github.com/Taitava/obsidian-shellcommands/issues/181)).
- [0.9.0 - 2021-12-18](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#090---2021-12-18): The variable was created. ([#120](https://github.com/Taitava/obsidian-shellcommands/issues/120)).