Shells have special meanings for certain characters. If the variables that you use in your commands, return special characters in their values, the special characters need to be *escaped* so that they will not perform any special, unexpected and possibly dangerous actions.

> [!Tip] Escaping can be disabled
> If you don't want variable values to be escaped, please see the section [[#Prevent escaping - but only after a deep consideration]].

Some examples:
- `mycommand "{{clipboard}}"`, with clipboard happening to contain a double quote `"` character. Your command might end up looking like this: `mycommand "Text pasted from clipboard that contains a " character."`.
- `mycommand {{clipboard}}`, with clipboard happening to contain stuff like `some text > C:\path\to\some\important\file`. In this case, the command might end up accidentally overwriting some file without a conscious meaning from the user.

In other words, special characters may cause your commands to execute completely different commands and actions than what you meant. To overcome this, **the *Shell commands* plugin automatically escapes special characters in variable values** ([[#Escaping depends on the shell|except for Windows CMD no escaping is done]]).

==**The escaping system is developed by ME, not by a shell expert, so it can have bugs and leaks. Safety cannot be 100% guaranteed.**==

# What are considered to be special characters?
Different shells have a slightly different set of special characters. However, some special characters are quite common across different shells, such as:
- a space ` `: used for separating arguments from commands and each other.
- a double quote `"`: used to wrap long text and mark that (almost) all special characters in it should be used literally. \*
- a single quote `'`: same as double quote, but insists all special characters to be used literally. \*

\*) Concerns Bash, but is quite similar in other shells, too. Source: https://www.gnu.org/software/bash/manual/html_node/Quoting.html (read on 2021-11-20).

The *Shell commands* plugin uses a quite precise definition for deciding if a character is special in a way that it should be escaped:

==A character is considered *special* by SC if it's **not** an alphabet in ASCII character set `a`-`z`/`A`-`Z`, not a number `0`-`9`, and not an underscore `_`.==
*(This definition is based on the following blog post: https://qntm.org/bash, read on 2021-10-16).*

All of these *special characters* - when occurring in an output of a [[Variables - general principles|variable]] - are escaped by adding an escape character - either `\` or `` ` `` - in front of the special character. A shell interprets the escape character so that it removes the special meaning of the special character. The shell will then remove the escape character, so that the final result will only be a literal, not-anymore-special character. Examples of escaped special characters:
- `\ ` or `` `  ``: will become a literal space ` `, that will not terminate an argument.
- `\"` or `` `"``: will become a literal double quote `"`, that will not mark a beginning/end of a text sequence.
- `\\` or ``` `` ```: will become a literal `\` or `` ` `` that will not escape the next character.

## Escaping depends on the shell
The escape character that SC will use - `\` or `` ` `` - is dependent on the current shell that is used. [[Shells#How to know which shell is used|How to know which shell is used]]?

- For [[Bash]], [[Dash]] and [[Zsh]], the escape character is `\`. If you are on Mac/Linux, you are probably using one of these shells.
- For [[PowerShell 5]] and [[PowerShell Core]], the escape character is `` ` ``. If you are on Windows, it's recommended that you [[Shells#How to know which shell is used|set SC to use PowerShell 5 or Core to be your default shell]] in order to enable special character escaping and make variables safer to use.
- **For Windows' [[CMD]], there is no escaping done**, because I don't know if there is a way to escape characters in CMD. [This might be improved later](https://github.com/Taitava/obsidian-shellcommands/discussions/106).

Most of the time, the escape characters works quite similarly. However, on [[Bash]] and the like, you should not have escaped characters wrapped in double quotes `"`  or single quotes `'`, because that will leave the escaping character `\` visible in the final result. On [[PowerShell]], however, this does not seem to happen.

## Prevent escaping - but only after deep consideration
I am not able to think about all the possibility use cases of this plugin. In theory, there might some situation, where there simply is no way to get things working if escaping is enabled - however, those cases should be very rare. If you are new to this plugin or new the shell commands in general, I highly recommend you to not think about preventing escaping as the first possible solution to whatever problem you might be facing - rather, it should be your last solution. Try to tweak your shell command in some other ways first, and [consider asking for help](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/q-a), and only after that, if nothing else helps, you can use `!`, e.g. `{{!file_name}}`, to prevent escaping.

> [!Info] Exceptions
> - Currently, preventing escaping might be temporarily needed with the `{{tags}}` variable. [[{{tags}}#Special characters in separator are escaped|More information]].
> - [[{{shell_command_content}}]] (used in [[Settings for custom shells|custom shell settings]]) is usually used with escaping turned off.
> - Escaping should be prevented when using {{variables}} in the *PATH additions* settings. [[Additions to the PATH environment variable#^no-escaping|More information]].
> - If you use variables in shell command *alias* fields, you can safely disable escaping there, as *alias* texts are never executed in shells.

# History
<small>This page was last modified on <strong>2022-06-09</strong> and created on 2021-10-31. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/Escaping%20special%20characters%20in%20variable%20values.md">See page edit history</a>.</small>
- [0.11.1 - 2022-03-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0111---2022-03-05): Fixed a bug that corrupted four-byte unicode characters, e.g. emojis. ([#171](https://github.com/Taitava/obsidian-shellcommands/issues/171)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): Escaping special characters in variable values started. ([#11](https://github.com/Taitava/obsidian-shellcommands/issues/11)).