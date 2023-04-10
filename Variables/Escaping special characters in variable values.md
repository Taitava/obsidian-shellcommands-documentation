Shells have special meanings for certain characters. If the variables that you use in your commands, return special characters in their values, the special characters need to be *escaped* so that they will not perform any special, unexpected and possibly dangerous actions.

> [!Tip] Escaping can be disabled
> If you don't want variable values to be escaped, please see the section [[#Prevent escaping - but only after a deep consideration]].

Some examples:
- `mycommand "{{clipboard}}"`, with clipboard happening to contain a double quote `"` character. Your command might end up looking like this: `mycommand "Text pasted from clipboard that contains a " character."`.
- `mycommand {{clipboard}}`, with clipboard happening to contain stuff like `some text > C:\path\to\some\important\file`. In this case, the command might end up accidentally overwriting some file without a conscious meaning from the user. ^dangerous-special-characters

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
- For [[PowerShell]], the escape character is `` ` ``. If you are on Windows, it's recommended that you [[Shells#How to know which shell is used|set SC to use PowerShell 5 or Core to be your default shell]] in order to enable special character escaping and make variables safer to use.
- **For Windows' [[CMD.EXE]], there is no escaping done**, because I don't know if there is a way to escape characters in CMD. [This might be improved later](https://github.com/Taitava/obsidian-shellcommands/discussions/106).

Most of the time, the escape characters works quite similarly. However, on [[Bash]] and the like, you should not have escaped characters wrapped in double quotes `"`  or single quotes `'`, because that will leave the escaping character `\` visible in the final result. On [[PowerShell]], however, this does not seem to happen.

## Prevent escaping - but only after deep consideration
I am not able to think about all the possibility use cases of this plugin. In theory, there might some situation, where there simply is no way to get things working if escaping is enabled - however, those cases should be very rare. If you are new to this plugin or new the shell commands in general, I highly recommend you to not think about preventing escaping as the first possible solution to whatever problem you might be facing - rather, it should be your last solution. Try to tweak your shell command in some other ways first, and [consider asking for help](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/q-a), and only after that, if nothing else helps, you can use `!`, e.g. `{{!file_name}}`, to prevent escaping.

> [!Info] Exceptions
> - If variables are used to define dynamic shell commands (e.g. [use URI links to assign shell commands to variables and execute them](https://github.com/Taitava/obsidian-shellcommands/discussions/333#discussioncomment-5408903) or [define shell commands in YAML frontmatter](https://github.com/Taitava/obsidian-shellcommands/discussions/337#discussion-5015061)), escaping should be disabled. It's safe, if it's made obvious to the vault's user, that their content is clearly used as an interpretable shell command, instead of just as a literal value for an argument.
> - Currently, preventing escaping might be temporarily needed with the `{{tags}}` variable. [[{{tags}}#Special characters in separator are escaped|More information]].
> - [[{{shell_command_content}}]] (used in [[Settings for custom shells|custom shell settings]]) is usually used with escaping turned off.
> - Escaping should be prevented when using {{variables}} in the *PATH additions* settings. [[Additions to the PATH environment variable#^no-escaping|More information]].
> - If you use variables in shell command *alias* fields, you can safely disable escaping there, as *alias* texts are never executed in shells.

# History
- [0.11.1 - 2022-03-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0111---2022-03-05): Fixed a bug that corrupted four-byte unicode characters, e.g. emojis. ([#171](https://github.com/Taitava/obsidian-shellcommands/issues/171)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): Escaping special characters in variable values started. ([#11](https://github.com/Taitava/obsidian-shellcommands/issues/11)).

> [!page-edit-history]- Page edit history: 2021-10-31 &#10132; 2023-03-29
> - [<small>2023-03-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/53e256a42e8f491f850a6807de3f97e9a22cb828): [[Escaping special characters in variable values.md]]: Mention that escaping can be disabled, if variables are used for defining dynamic shell commands.
> - [<small>2023-03-23</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/07644d90d4a01c20fd0a151a7fec543000df0a54): Documentation for {{shell_command_content}}.
> - [<small>2022-06-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a6d98af9f752d83d8546719680419c2bd6973987): Escaping special characters in variable values: Mention that it's feasible to disable escaping in alias texts.
> - [<small>2022-06-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3327495afa8b2202864b59e13246b29d4e4a3bc0): Escaping special characters in variable values: Make it more prominent that escaping can be disabled.
> - [<small>2022-05-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ec4c6a61c51fc5c5a9c2ddb78469e671cffae9d1): 'PATH additions' settings: {{environment}} should be {{!environment}}.
> - [<small>2022-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2cb5f2e7896619b6e8b026b7744282b98d605528): Escaping special characters in variable values.md: Mention that a 4-byte unicode corruption bug is fixed.
> - [<small>2022-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8fc69b0f06842d47adc8143b3815ce3a0cab482f): Escaping special characters in variable values.md: Add a history section.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/118aaeb67eed11873cbe54c98b0f74b152b1c210): Shells.md: Add 'Choosing a shell on a per shell command basis'.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3010cd79f48e79b997509b6a8a1b0bad5a23993b): Create Shells.md.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1f4d7bbadccbb367d8f75d5b9d7f045f5b9a2954): Escaping special characters in variable values.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6eaebca7665be014aa0c07fd9a91bad9356dc541): Escaping special characters in variable values.md: Add a note about the system not being developed by an expert.
> - [<small>2021-11-16</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/72deca128a6c88e6ed8afaa14700609cc3670655): More topics about escaping and how to check the default shell.
> - [<small>2021-10-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2dd3261379bc2817e7ea01b96872402ad7c3c4d1): Some quick plans for the documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/Escaping%20special%20characters%20in%20variable%20values.md).
> ^page-edit-history