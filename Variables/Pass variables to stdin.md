`stdin` can be used to pass text values to shell programs without including them in the command line used to call the program.

> [!Info] About `stdin` - an abbreviation for _standard input_
> - `stdin` is one of three [standard streams](https://en.wikipedia.org/wiki/Standard_streams): `stdin`, `stdout` and `stderr`.
> - Used for inputting values to programs, whereas `stdout` and `stderr` go the other direction: they output values.

## How to define `stdin` content
1. Go to the plugin's settings panel.
2. Look for the shell command whose `stdin` you want to define, and click the *Alias, Icon, Confirmation, Stdin* icon next to it:
  ![[Settings-main-click-general-icon.png]]
 3. An *extra options modal* opens up. In the modal, look for *Pass variables to standard input (stdin)*.
![[Settings-modal-general.png]]
4. Write the content (static text or [[Variables - general principles|{{variables}}]]) that should be passed to `stdin` to the text field. Multiline content is also supported, the field grows if you press enter.

> [!summary] Notes
> - When using [[Variables - general principles|{{variables}}]] in the `stdin` field, special characters in their values are not [[Escaping special characters in variable values|escaped]], unlike when passing variables to shell commands directly.
> - If the `stdin` settings field is empty, nothing will be passed to `stdin`, not even an empty string.
> - If there are multiple values that need to be inputted, put them on separate lines. Many shell programs interpret newlines as separators between different values.

# History
<small>This page was last modified on <strong>2023-01-06</strong> and created on 2022-12-05. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/Pass%20variables%20to%20stdin.md">See page edit history</a>.</small>
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): The ability to pass content to `stdin` was born. ([#283](https://github.com/Taitava/obsidian-shellcommands/issues/283)).