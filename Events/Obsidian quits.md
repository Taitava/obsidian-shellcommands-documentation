---
cssclass: customiseTitle
---
# Event: Obsidian quits

## Execution
> [!Success] Executed when
> - User has commanded Obsidian to quit or restart. Execution is not guaranteed, as Obsidian might close even before the shell command execution. Even more likely is that there is no time to do output handling. There's no way for a shell command to make Obsidian wait or cancel from quitting.
> - Executed even when another vault is still left open.

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[Watch cat videos on YouTube after closing Obsidian]]

## Based on
The Obsidian event that powers this feature is [`quit` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3632).

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2021-12-13. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Obsidian%20quits.md">See page edit history</a>.</small>
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event's name was shortened from *Before Obsidian quits* to *Obsidian quits*. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).