# Event: After Obsidian starts

## Execution
> [!Success] Executed when
> - Obsidian has started (or restarted) and loaded a layout, i.e. when everything should be ready.
> - The *Shell commands* plugin is re-enabled.

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[]] #TODO: Add an example.

## Based on
The Obsidian event that powers this feature is [`onLayoutReady()` on `workspace` events](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L3444).

## History
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).