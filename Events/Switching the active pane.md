---
cssclass: customiseTitle
---
# Event: Switching the active pane

## Execution
> [!Success] Executed when
> - User switches between panes, including panes that are not files, e.g. Graph view.
> - Another file is opened in the current pane.
> - Go back/go forward functions are used to open previous/next notes in the current pane.

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[Display file size and modification time on status bar]]

## Based on
The Obsidian event that powers this feature is [`active-leaf-change` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3576).

- `active-leaf-change` (at least on Obsidian `0.12.19`) has a tendency to trigger the event also right after Obsidian starts (= that's also counted as a pane becoming active). The *Shell commands* plugin notices this and prevents triggering this *After switching the active pane* event during start-up. If you want to execute your shell command also during start-up, enable the [[Obsidian starts]] event, too.

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2021-12-13. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Switching%20the%20active%20pane.md">See page edit history</a>.</small>
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event's name was shortened from *After switching the active pane* to *Switching the active pane*. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).