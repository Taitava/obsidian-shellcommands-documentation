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
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The event's name was shortened from *After switching the active pane* to *Switching the active pane*. ([#218](https://github.com/Taitava/obsidian-shellcommands/issues/218)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The event was released. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2021-12-13 &#10132; 2022-12-11
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bcc0e63a8382fdbe8c42242d3df28cbc4fe63d18): Shorten event names.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3b3db94cf15a6c0b1af609ff00e6289e565393e7): Events: Use callouts for the 'Executed when' sections.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/89c649149543fc253fb088b0a1c174138be9f1a1): Events: Add 'Examples' section.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> - [<small>2021-12-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b4138ec1d10021a77b034dca21a6c9d7cffd9574): Events: After switching the active pane: It's also triggered when 'go back'/'go forward' functions are used.
> - [<small>2021-12-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0366fb1d749f167979a66d9699ef1c7f1d5c0cf9): After switching the active pane: This event does not trigger anymore during start-up.
> - [<small>2021-12-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7bdf92617999418cd604db6fbbd79a1f9e638ebb): Events: Change 'After active leaf has changed' to 'After switching the active pane'.
> - [<small>2021-12-13</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62392cb2d52bcf909cd8a5f56933ff07c5496e3b): WIP: A draft of Events documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/Switching%20the%20active%20pane.md).
> ^page-edit-history