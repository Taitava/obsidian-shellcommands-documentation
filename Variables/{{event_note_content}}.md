---
cssclass: customiseTitle
---
# Variable: `{{event_note_content}}`
> [!Quote] {{event_note_content}} described in the *Shell commands* plugin's settings
> Gives the event related file's content without YAML frontmatter. If you need YAML included, use [[{{event_file_content}}]] instead.

# Availability
> [!Warning] Only available:
> In events: [[File menu]], [[File created]], [[File content modified]], [[File deleted]], [[File moved]], [[File renamed]]

# See also
- [[{{event_file_content}}]]
- [[{{note_content}}]]

# History
- [0.21.0 - 2023-12-30](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0210---2023-12-30): Prevent a crash when using the variable in Obsidian version `>= 1.4.0`. No practical changes in behavior. ([#372](https://github.com/Taitava/obsidian-shellcommands/issues/372)).
- [0.16.0 - 2022-09-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0160---2022-09-25): The variable was released. ([#77](https://github.com/Taitava/obsidian-shellcommands/issues/77)).

> [!page-edit-history]- Page edit history: 2022-09-11 &#10132; 2023-12-30
> - [<small>2023-12-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/88a58d8b5359f98cd1e385f569f85ae3c948b739): [[{{note_content}}]], [[{{yaml_content}}]], [[{{event_note_content}}]] and [[{{event_yaml_content}}]] are now compatible with Obsidian `>= 1.4.0`.
> - [<small>2022-09-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1a6b6b5d9d7153a45d308923056a67a8737a2e6): 0.16.0 is released.
> - [<small>2022-09-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/57eab54eef74305f6ee9868344249ae79115c699): {{note_content}} and {{event_note_content}} variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bevent_note_content%7D%7D.md).
> ^page-edit-history