---
cssclass: customiseTitle
---
# Variable: `{{caret_paragraph}}`
> [!Quote] {{caret_position}} described in the *Shell commands* plugin's settings
> Gives a text line at the current caret position.

The returned text line constains everything on the caret's current line, i.e. everything between two linebreak characters. No linebreaks are included in the returned text.

> [!info] About _paragraph_
> The term _paragraph_ in the variable's name may sound a bit odd when considering that the variable actually returns a _line_. The variable is named `{{care_paragraph}}` instead of `{{caret_line}}` because _line_ could be confused with a _line number_ (which can be retrieved by [[{{caret_position}}|{{caret_position:line}}]]), especially when it appears with the word _caret_. 
>
> Also, Obsidian's [_Delete paragraph_ command](https://forum.obsidian.md/t/i-hope-there-is-a-hotkey-to-delete-a-whole-line/4213/2) uses _paragraph_ as a meaning of a _line_.

## Availability
> [!Warning] Only available:
> When a note pane is open, not in graph view, nor when viewing non-text files.

## See also
- [[{{caret_position}}]]

# History
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): Fixed not being able to define a [[Default values|default value]] for this variable. ([#311](https://github.com/Taitava/obsidian-shellcommands/issues/311)).
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The variable was born. ([#282](https://github.com/Taitava/obsidian-shellcommands/issues/282)).

> [!page-edit-history]- Page edit history: 2022-11-04 &#10132; 2023-01-06
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6d70dc84a6cdd69a185bc8aafb849ff694628bd7): {{caret_paragraph}}: Mention a bug fix.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-04</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8966b2f59d3695f807025df90b5c34142b7e4845): Add {{caret_paragraph}} variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bcaret_paragraph%7D%7D.md).
> ^page-edit-history