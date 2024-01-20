---
aliases:
 - variable
 - "{{variable}}"
 - "{{variables}}"
---
In each shell command, you can use `{{variables}}` to submit data to your commands. You can for example pass the currently open file's path to a command that echoes the current date to the end of that file: `echo {{date:YYYY-MM-DD}} >> {{file_path:absolute}}`.

- Variables are always enclosed within `{{` and `}}`.
- Other characters specific to variables are `:` and `!`. More about them below.
- If you need to use `{{`, `}}`, `:` or `!` to do other things not related to variables, you can use them quite freely, but make sure that you do not accidentally concatenate them with text that forms an existing variable's name. E.g. you can use a literal text `{{variable}}` and you'll have just `{{variable}}`, because there is **no** variable named *variable*. You can also use a literal text `{{date}}` because the [[{{date}}]] variable expects an argument with it, and does not parse without. But you cannot have a literal `{{date:}}`, because that would trigger parsing the [[{{date}}]] variable, resulting in an empty text, because the given argument (*format*) is empty.
- Variables are predefined by SC, you cannot define your own variables. If you have an idea for a new variable, you can [suggest it in the *Ideas* discussion category](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas).

> [!Info] All variables
> The list of all built-in variables has been moved on 2022-05-08 to a new page: [[All variables]]


## Escaping special characters in variable values

When a variable returns a value, all *special characters* in the value are escaped by prefixing them with an *escaping character*, e.g. `>` becomes either `\>` or `` `> ``, depending on [[Shells#How to know which shell is used|your shell]]. This is done to prevent the special characters from doing unexpected things. I'm not an expert in shells or command safety, and this feature may have leaks and bugs. I cannot guarantee the escaping to be 100% secure.

Due to escaping, it's recommended that you do not surround `{{variables}}` in double/single quotes (`"`/`'`). Escaped variable values do not need quotes around them. Having quotes around them can make `\` escaping characters accidentally visible in your command's output, if your shell is Bash or similar.

If your shell is CMD (the Windows legacy shell), **unfortunately no escaping is done**. This is because I do not know if there is a way to escape special characters in CMD. [Please contact me in GitHub if you know how to do it](https://github.com/Taitava/obsidian-shellcommands/discussions/106).

For information about what *special characters* are in this context, and what *escaping character* is used to make them safe, please read more about [[Escaping special characters in variable values]]. That same page also tells you how you can prevent the escaping completely in some rare situations, but first you need to read and understand why it's **not** a good idea to prevent escaping. The `!` character is explained there.

## Arguments for variables
Some variables accept arguments that are used to control how the variable works. Arguments are separated from the variable name by a colon `:`, e.g. [[{{date}}]] variable `{{date:YYYY}}` gives the current year. ^arguments1

Read more about [[arguments for variables]].

## Using a variable's value as a command
In theory, a variable value can also be used as a command name, too. E.g. `{{clipboard}} "Hi!"` would execute whatever command happens to be in the clipboard, and pass the text *Hi!* to it as an argument. But that's quite rare and can be unsafe, because there's no way to restrict what the command can be.

The point of this example is more to inform you, that if you don't pay special attention to how you use variables, you can accidentally create shell commands that do something else than what you mean. Misplacing a variable in a wrong location can lead to bad things. **This plugin is not the safest one on the Obsidian's community plugins list.** It comes with risks, especially when variables are used.

## Default values for variables ^default-values
Not all variables are always available. For example, [[{{file_name}}]] variable cannot be accessed, if the currently active pane does not contain a file. If [[{{file_name}}]] is tried to be used in such a situation, the *Shell commands* plugin will show the following error message: *{{file_name}}: No file is active at the moment. Open a file or click a pane that has a file open.* The shell command's execution is then cancelled.

- In situations like that, variables can have *default values* that will be used if the normal value is unavailable, and the execution can be continued.
- Another situation might be, that execution should be cancelled when a variable is unavailable, but no visible error messages are wanted. This might be desirable when executing shell commands via [[Events - general principles|Events]], but the execution is only wanted when the needed variables are available.

Read more about [[Default values|how to define default values for variables]].

# Custom variables ^custom-variables
> [!Summary] Custom variables can be used to:
> - store values inputted by user via [[prompts]].
> - [[Output channel - Assign custom variables|store values outputted by shell commands]].
> - pass their values as input to shell commands.
> - pass values when [[Shell commands URI|executing shell commands via Obsidian URI]].
> ^custom-variables-can-be-used-for

Read more about [[custom variables]].

# Passing `{{variable}}` values into external script files
`{{Variables}}` are only known by the *Shell commands* plugin, not by any [[shells]]. The *Shell commands* plugin interprets the `{{variables}}`, meaning that it **translates** them into literal values before a shell command is passed to a shell for execution. This means, that **no shells are aware of the `{{variables}}`** that you use when you use the *Shell commands* plugin. The plugin can only translate `{{variables}}` that it sees, so, when executing external script files, the contents of those files are **not read** by the *Shell commands* plugin, and so no `{{variables}}` can work there.

> [!Success] Bash example: No script file
> A working shell command that creates a folder that gets its name from selected text and then creates an empty file in that folder:
> ```bash
> mkdir {{selection}} && cd {{selection}} && touch {{date:YYYY-MM-DD}}".md"
> ```
> This simple shell command works, because the *Shell commands* plugin can read its `{{variables}}` and substitute them with a real values.

> [!Fail] Bash example: Incorrect script file
> A  shell command that calls an external script file to create a folder and a file in it:
> ```bash
> /bin/bash create-folder.sh
> ```
> Content of `create-folder.sh` :
> ```bash
> mkdir {{selection}}
> cd {{selection}}
> touch {{date:YYYY-MM-DD}}".md"
> ```
> The script would see just a literal `{{selection}}` instead of the actually selected text, because the *Shell commands* plugin does not parse `{{variables}}` in any files referred in the executed shell command.

> [!Success] Bash: Pass `{{variable}}` values into scripts correctly
> The shell command calling the script file must contain all the variables the script needs, and pass their values to the script **as command line arguments**:
> ```bash
> /bin/bash create-folder.sh {{selection}} {{date:YYYY-MM-DD}}
> ```
> A space ` ` is used to separate different arguments from each other. Note that the `{{variable}}` values can contain spaces freely - the *Shell commands* plugin [[Escaping special characters in variable values|escapes]] any spaces in `{{variable}}` values, so they will not cause values to accidentally split into multiple arguments (exception: the escaping does not work when using CMD as a shell).
>
> Content of `create-folder.sh` :
> ```bash
> mkdir $1 # $1 is the first argument the script receives: {{selection}}
> cd $1 # Re-use {{selection}} here.
> touch $2".md" # $2 is the second argument the script receives: {{date:YYYY-MM-DD}}
> ```

#TODO: The examples above only work for Bash (and similar shells)! Create examples for PowerShell, too.

# History
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): Variables listed in _Variables_ tab in settings and in [[autocomplete]] menu, have now a link to their documentation pages. ([#302](https://github.com/Taitava/obsidian-shellcommands/issues/302)).
- #TODO: Add older history records regarding the variable system.

> [!page-edit-history]- Page edit history: 2021-10-31 &#10132; 2023-03-23
> - [<small>2023-03-23</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ff1855d010f20a905a0ab35a813f984c3f0cd02c): Variables - general principles.md: Shell commands URI is released already.
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2022-12-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cf21d0992315eb7e221e2522ac1a52c3c3413bb4): History records for adding documentation links to variable listings in the plugin.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b19d636b4887940a685f6a90089d036b53de908a): Variables - general principles.md: Add more aliases.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/22bbc6f273f83619ad206784d8e1d451dc1a4f06): Variables: How to pass variable values to script files.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f47632e512e5549216f844d42703410de2dde0fc): Variables: Move built-in variable lists to a new file, All variables.md.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/df021e7305cee4944a440c4c16bf7b3a283dcd1f): Beta 0.12.0: Add notices.
> - [<small>2022-04-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/91702a4b6edda4a90120067de22de23a26383240): Custom variables.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2d3e8929249fc0817a92b10ffe04b8b735d2cb97): 0.12.0: Default values for variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3ca3ab49bb838e832ee435cb1427161cfa8c1444): Add event related variables.
> - [<small>2021-12-18</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/626eb9f280fa5298c9c19037783552fb0318042c): Cancel adding {{newline}} variable.
> - [<small>2021-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/24cbeaa5d55ef3f3c251af9bf3ecf33331af9b2b): {{newline}} variable.
> - [<small>2021-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/800c7e08d965a402888f523192571198fbeb029c): Variables - general principles: Forgot to add {{yaml_value}}.
> - [<small>2021-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/50aac17878dcdc8be628789f8c9fee1f566d3f3a): {{file_extension}} variable.
> - [<small>2021-12-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7bfb1a340d550b18e946b799907d8696bde818da): {{caret_position}} variable.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3010cd79f48e79b997509b6a8a1b0bad5a23993b): Create Shells.md.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f51105a249490dff82fc8f24753b1c975bcebb28): Variables - general principles.md: Add a link to CMD escaping discussion.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2c3e9b2d8b625eb02dd1b6d8b709a5a4140c36f1): Arguments for variables.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/00980a4ff0c56a5196b65efaa430b4e265d3a00c): Variables - general principles.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17cb062fae9850024325871b93694d81e5d67fa3): Documentation for each variable.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e5e64ba07d1979852b3f75f53ed3d1480ffdb09): Documentation for each variable.
> - [<small>2021-10-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2dd3261379bc2817e7ea01b96872402ad7c3c4d1): Some quick plans for the documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/Variables%20-%20general%20principles.md).
> ^page-edit-history