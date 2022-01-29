# Event: After switching the active pane

## Executed when
- User switches between panes, including panes that are not files, e.g. Graph view.
- Another file is opened in the current pane.
- Go back/go forward functions are used to open previous/next notes in the current pane.

## Variables
This event does not provide additional event specific variables, but all [[Variables - general principles#^normal-variables|normal variables]] are available.

## Examples
- [[Display file size and modification time on status bar]]

## Based on
The Obsidian event that powers this feature is [`active-leaf-change` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3576).

- `active-leaf-change` (at least on Obsidian `0.12.19`) has a tendency to trigger the event also right after Obsidian starts (= that's also counted as a pane becoming active). The *Shell commands* plugin notices this and prevents triggering this *After switching the active pane* event during start-up. If you want to execute your shell command also during start-up, enable the [[After Obsidian starts]] event, too.

## History
- #TODO: Add date. [0.10.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).