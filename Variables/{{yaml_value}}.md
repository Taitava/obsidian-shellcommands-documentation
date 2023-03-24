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
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Fixed a crash when the argument was empty. The bug appeared in version `0.10.0` at the same time when variable `{{event_yaml_value}}` was released. ([#181](https://github.com/Taitava/obsidian-shellcommands/issues/181)).
- [0.9.0 - 2021-12-18](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#090---2021-12-18): The variable was released. ([#120](https://github.com/Taitava/obsidian-shellcommands/issues/120)).

> [!page-edit-history]- Page edit history: 2021-12-10 &#10132; 2023-01-01
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b7321d2509c80b5788d19c2ea080f035e94f7b94): {{yaml_value}} and {{event_yaml_value}}: Improve availability texts.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2f5517b6bf9435d158c6175c23c5f8320345dcb1): {{yaml_value}}.md: Fix YAML example indentation.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-04-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0885db826a0ab3b09b05907bc4817bb520e3e2cb): {{yaml_value}}.md and {{event_yaml_value}}.md: Mark that bug #181 is fixed in 0.12.0.
> - [<small>2022-04-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f3cd87e0e3450fff3d67188feef83afb0deadf88): {{yaml_value}}.md: History: Fixed a link to an issue where the variable was created.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8610b6660a05e99d0cc0531db30ffde0bfc2fe8e): Variables: Add availability information.
> - [<small>2021-12-18</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/798838b1b921a0b1e832c95af7d60fcbc02eb448): Add some forgotten 0.9.0 history details.
> - [<small>2021-12-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/02310bd4b2e2938a2879d35b5276d5621c3f5c46): {{yaml_value}} variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Byaml_value%7D%7D.md).
> ^page-edit-history