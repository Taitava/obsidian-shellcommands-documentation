---
cssclass: customiseTitle
---
# Event: Every $n$ seconds
| [[{{event_type}}\|{{event_type:category}}]] | [[{{event_type}}]] |
| ---- | --- |
| `time` | `every-n-seconds` |
## Execution
> [!Success] Executed when
> - On a freely decidable frequency defined in seconds. One decimal is allowed, e.g. `0.1` would be `100` milliseconds, and `1.1` would be `1100` milliseconds. 
> 
> ![[Event-every-n-seconds.png]]

> [!Info] Debouncing can make the frequency longer
> Note that if [[Events - debouncing|event debouncing]] is enabled for the same shell command where the _Every $n$ seconds_ event is enabled, the debouncing can make the shell command to be executed **less often** than what the event's configured frequency ($n$) is. This happens, if `the execution duration + `[[Events - debouncing#Cooldown duration|cooldown duration]] is longer than the event's frequency ($n$).

## Variables
This event does not provide additional event specific variables, but all [[All variables#Normal variables|normal variables]] are available.

## Examples
- [[Display a clock]]

## Based on
This feature utilizes [JavaScript's `window.setInterval()` method](https://developer.mozilla.org/en-US/docs/Web/API/setInterval).

(The interval reference is also passed to [Obsidian API's `component.registerInterval()` method](https://github.com/obsidianmd/obsidian-api/blob/763a243b4ec295c9c460560e9b227c8f18d8199b/obsidian.d.ts#L545) so that further event executions can be cancelled if the *Shell commands* plugin gets disabled).

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2024--): The seconds can now have one decimal. ([#385](https://github.com/Taitava/obsidian-shellcommands/issues/385)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was released. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2022-01-01 &#10132; 2024-02-10
> - [<small>2024-02-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0ef4d4c717223599d69d32a92845bef694925026): Documentation for [[{{event_type}}]] variable.
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b242343b52174ecb98bd874d3655876980694aca): Event [[Every n seconds.md]]: The seconds can now have one decimal.
> - [<small>2024-01-14</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4cbddbedbc92fce6430240b1567b1f94e48e1d46): [[Every n seconds.md]]: Information about event debouncing.
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3b3db94cf15a6c0b1af609ff00e6289e565393e7): Events: Use callouts for the 'Executed when' sections.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e5b806c587863e196b130ee859c05d9ac9ff0fae): Examples: Display a clock.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/Every%20n%20seconds.md).
> ^page-edit-history