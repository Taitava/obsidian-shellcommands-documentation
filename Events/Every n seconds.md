# Event: Every *n* seconds

## Executed when
- On a freely decidable frequency defined in seconds.

![[Event-every-n-seconds.png]]

## Variables
This event does not provide additional event specific variables, but all [[Variables - general principles#^normal-variables|normal variables]] are available.

## Based on
This feature utilizes [JavaScript's `window.setInterval()` method](https://developer.mozilla.org/en-US/docs/Web/API/setInterval).

(The interval reference is also passed to [Obsidian API's `component.registerInterval()` method](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L545) so that further event executions can be cancelled if the *Shell commands* plugin gets disabled).

## History
- #TODO: Add date. [0.10.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).