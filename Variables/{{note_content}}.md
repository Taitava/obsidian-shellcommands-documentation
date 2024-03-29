---
cssclass: customiseTitle
---
# Variable: `{{note_content}}`
> [!Quote] {{note_content}} described in the *Shell commands* plugin's settings
> Gives the current note's content without YAML frontmatter. If you need YAML included, use [[{{file_content}}]] instead.

# Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

# See also
- [[{{file_content}}]]
- [[{{event_note_content}}]]

# History
- [0.21.0 - 2023-12-30](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0210---2023-12-30): Prevent a crash when using the variable in Obsidian version `>= 1.4.0`. No practical changes in behavior. ([#372](https://github.com/Taitava/obsidian-shellcommands/issues/372)).
- [0.16.0 - 2022-09-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0160---2022-09-25): The variable was released. ([#77](https://github.com/Taitava/obsidian-shellcommands/issues/77)).

> [!page-edit-history]- Page edit history: 2022-09-11 &#10132; 2023-12-30
> - [<small>2023-12-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/88a58d8b5359f98cd1e385f569f85ae3c948b739): [[{{note_content}}]], [[{{yaml_content}}]], [[{{event_note_content}}]] and [[{{event_yaml_content}}]] are now compatible with Obsidian `>= 1.4.0`.
> - [<small>2023-11-27</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7736b53cd5c2294fefe8856521e7b4d8188aa20b): Add broken variable warnings to [[{{note_content}}.md]], [[{{yaml_content}}.md]] and [[{{yaml_value}}.md]].
> - [<small>2022-09-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1a6b6b5d9d7153a45d308923056a67a8737a2e6): 0.16.0 is released.
> - [<small>2022-09-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/57eab54eef74305f6ee9868344249ae79115c699): {{note_content}} and {{event_note_content}} variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bnote_content%7D%7D.md).
> ^page-edit-history