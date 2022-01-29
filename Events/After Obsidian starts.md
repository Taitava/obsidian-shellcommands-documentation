# Event: After Obsidian starts
## Executed when
- Obsidian has started (or restarted) and loaded a layout, i.e. when everything should be ready.
- The *Shell commands* plugin is re-enabled.

## Variables
This event does not provide additional event specific variables, but all [[Variables - general principles#^normal-variables|normal variables]] are available.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`onLayoutReady()` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3444).

## History
- #TODO: Add date. [0.10.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).