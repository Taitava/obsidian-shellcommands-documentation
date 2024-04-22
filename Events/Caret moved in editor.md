---
cssclasses:
  - customiseTitle
---
# Event: Caret moved in editor
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `editor` | `caret-moved` |
## Execution
> [!Success] Executed when
> - The text caret (sometimes called as _cursor_) moves in an editor.
>     - Including [canvas](https://obsidian.md/canvas) content editor.

> [!Fail] Not executed when
> - Caret moves in file name field.

## Line or column changes

The event can be configured to only execute a shell command...
 - ... only when a line changes.
 - ... only when a column changes.
 - ... in both cases.
![[Settings-modal-events-Caret-moved-in-editor.png]]

## Variables

This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[]] #TODO: Add a git lens example.

## Based on
This event is powered by a [custom CodeMirror extension](https://github.com/Taitava/obsidian-shellcommands/blob/96e7656a48dc5ca3bcaad7cfca052c39b4ac7252/src/events/SC_Event_CaretMoved.ts#L37-L69).

# History
- #TODO: Add a date [0.23.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was **finally** released. ([#345](https://github.com/Taitava/obsidian-shellcommands/issues/345)).
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2024--): Added information to the event's settings that it does not work. ([#345](https://github.com/Taitava/obsidian-shellcommands/issues/345)).
- [0.20.0 - 2023-06-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0200---2023-06-25): Incomplete code of the event was accidentally released. The event does not work yet. ([#345](https://github.com/Taitava/obsidian-shellcommands/issues/345)).

> [!page-edit-history]- Page edit history: 2023-06-25 &#10132; 2024-01-20
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/26d8f10feea73020c6108d632b8581e2f9e40c4e): [[Caret moves in editor.md]]: Add a draft structure.
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1399ca5f52956bd6ba2b3202720d6422f270c088): Rename [[Caret moved in editor.md]] to [[Caret moves in editor.md]].
> - [<small>2023-06-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/df52c62a0ea458e8f4c29614f5af7baca7573255): [[Caret moved in editor]] event got accidentally published before it's complete.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/Caret%20moves%20in%20editor.md).
> ^page-edit-history