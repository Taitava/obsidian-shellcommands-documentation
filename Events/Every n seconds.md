# Event: Every *n* seconds

## Execution
> [!Success] Executed when
> - On a freely decidable frequency defined in seconds.
> 
> ![[Event-every-n-seconds.png]]

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[Display a clock]]

## Based on
This feature utilizes [JavaScript's `window.setInterval()` method](https://developer.mozilla.org/en-US/docs/Web/API/setInterval).

(The interval reference is also passed to [Obsidian API's `component.registerInterval()` method](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L545) so that further event executions can be cancelled if the *Shell commands* plugin gets disabled).

# History
<small>This page was last modified on <strong>2022-12-11</strong> and created on 2022-01-01. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Every%20n%20seconds.md">See page edit history</a>.</small>
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was created. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).