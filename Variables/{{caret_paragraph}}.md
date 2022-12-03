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

## History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The variable was born. ([#282](https://github.com/Taitava/obsidian-shellcommands/issues/282)).