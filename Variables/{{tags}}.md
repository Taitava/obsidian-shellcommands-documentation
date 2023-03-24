---
cssclass: customiseTitle
---
# Variable: `{{tags:separator}}`
> [!Quote] {{tags}} described in the *Shell commands* plugin's settings
> Gives all tags defined in the current note. Replace the *separator* part with a comma, space or whatever characters you want to use as a separator between tags. A separator is always needed to be defined.

## No hash `#` prefix
Note that the returned tags are **not** prefixed with a hash `#`. If you want to have them prefixed with a hash `#`, use `#` as the *separator* and also include it before the variable, like this: `#{{tags:, #}}`. If you have tags `#tag1`, `#tag2` and `#tag3`, this would give you: `#tag1, #tag2, #tag3`.

## Special characters in *separator* are escaped
Starting from SC `0.7.x`, special characters in variable values are escaped (= prefixed with either `\` or `` ` ``). Escaping concerns everything a variable outputs, even the *separator*. So, if you want to use a separator that can e.g. split your tags to be separate parameters to a command, using e.g. a space as a separator will end up the space being escaped.

Example:
- Think that you would have the following tags in your file: `#tag1`, `#tag2` and `#tag3`.
- Think that you would use the variable like this: `{{tags: }}` (*separator* is a space ` `). The output would be: `tag1\ tag2\ tag3` or ``tag1` tag2` tag3``.
- Think that you would use the variable like this: `{{tags:,}}` (*separator* is a comma `,`). The output would be: `tag1\,tag2\,tag3` or ``tag1`,tag2`,tag3``.

A space ` ` that is prefixed with an escaping character (`\` or `` ` ``) does not separate your expression to different arguments.

If you wish to use special characters in the *separator*, currently the only way is to deny escaping by adding an exclamation mark `!` to the variable. Examples:
- Think that you would use the variable like this: `{{!tags: }}` (*separator* is a space ` `). The output would be: `tag1 tag2 tag3`.
- Think that you would use the variable like this: `{{!tags:,}}` (*separator* is a comma `,`). The output would be: `tag1,tag2,tag3`.
- **A problem with this solution is that in case your tag names contain special characters, they will appear unescaped, too.** It may make your command unsafe.

[A better solution for this *separator* problem is under planning on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/105).

## Availability
> [!Warning] Only available:
> When the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_tags}}]]

# History
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The variable does not include preceding hash (#) characters anymore. This is a backwards incompatible change (although a small one), and normally these kinds of changes would not be released in a _minor_ version update. But this plugin is still in its 0.x era, so breaking changes are tolerated more than in stable releases. If you want to have your tags prefixed with a hash again, use something like `#{{tags:,#}}` instead of `{{tags:,}}`.  ([#62](https://github.com/Taitava/obsidian-shellcommands/issues/62)).
- [0.5.1 - 2021-10-09](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#051---2021-10-09): The variable does not give duplicate tags anymore. ([#65](https://github.com/Taitava/obsidian-shellcommands/issues/65)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The variable was released. Idea by [Felipe Rearden](https://github.com/FelipeRearden). ([#51](https://github.com/Taitava/obsidian-shellcommands/issues/51)).

> [!page-edit-history]- Page edit history: 2021-11-19 &#10132; 2022-12-11
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10ffc392aaf12df9cc211fb05030d43bcb772aad): Change ## History to # History on all pages.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8610b6660a05e99d0cc0531db30ffde0bfc2fe8e): Variables: Add availability information.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62b9ff92e6c0ed82fb8d617b8644ba062cafa25a): Variables: add version history.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ac4edfc48ee1136dae272140bb639273d92264f2): {{tags}}: Tell how to get '#' prefix.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17cb062fae9850024325871b93694d81e5d67fa3): Documentation for each variable.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e5e64ba07d1979852b3f75f53ed3d1480ffdb09): Documentation for each variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Btags%7D%7D.md).
> ^page-edit-history