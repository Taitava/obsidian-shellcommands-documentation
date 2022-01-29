# Variable: `{{tags:separator}}`

> Gives all tags defined in the current note. Replace the *separator* part with a comma, space or whatever characters you want to use as a separator between tags. A separator is always needed to be defined.

_(The above description can also be seen in the plugin's settings.)_

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
> <strong>Only available</strong> when the active pane contains a file, not in graph view or other non-file view.

## See also
- [[{{event_tags}}]]

## History
- [0.6.0 - 2021-10-12](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#060---2021-10-12): The variable does not include preceding hash (#) characters anymore. This is a backwards incompatible change (although a small one), and normally these kinds of changes would not be released in a _minor_ version update. But this plugin is still in its 0.x era, so breaking changes are tolerated more than in stable releases. If you want to have your tags prefixed with a hash again, use something like `#{{tags:,#}}` instead of `{{tags:,}}`.  ([#62](https://github.com/Taitava/obsidian-shellcommands/issues/62)).
- [0.5.1 - 2021-10-09](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#051---2021-10-09): The variable does not give duplicate tags anymore. ([#65](https://github.com/Taitava/obsidian-shellcommands/issues/65)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The variable was created. Idea by [Felipe Rearden](https://github.com/FelipeRearden). ([#51](https://github.com/Taitava/obsidian-shellcommands/issues/51)).