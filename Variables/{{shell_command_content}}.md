---
cssclass: customiseTitle
---
 > [!Warning] This feature is only available in a beta test
 > - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/108#discussioncomment-5277523).
 > %% #TODO: Remove this annotation when the final version is released. %%

# Variable: `{{!shell_command_content}}`
> [!Quote] {{!shell_command_content}} described in the *Shell commands* plugin's settings
> Gives the executable shell command statements that should be passed to a shell.

This variable is used in [[custom shells]]' settings to pass the content of a shell command to a shell program. It's used in two places in the settings:
 - [[#Shell arguments]]
 - [[#Wrapper for shell command]]

> [!tip] Use `{{!shell_command_content}}` without escaping special characters.
>  Although [[Variables - general principles|{{variables}}]] are usually used **with** [[Escaping special characters in variable values|escaping possible special characters]] in their values, when using `{{!shell_command_content}}` in custom shell settings, it's usually used **without** escaping.
>  > [!Example] Example [[Bash]] command
>  > ```bash
>  > echo "Hello, world!"
>  > ```
>  > > [!Success] `{{!shell_command_content}}` = `echo "Hello, world!"`
>  > 
>  > > [!Warning] `{{shell_command_content}}` = `echo\ \"Hello\,\ world\!\"`
>  > > Although this is not necessarily wrong (as it can be used e.g. for logging purposes), it's not capable of executing the shell command, because there's no separating space anywhere after `echo`, so the execution fails with an error:
> > > ```
> > > echo "Hello, world!": command not found
> > > ```

## Shell arguments
> [!Info] Arguments for custom shells
> Each shell defines arguments that control their behavior when they execute commands. The most important argument is the executable command itself.

When used as a shell argument, `{{!shell_command_content}}` gives:
 - **a)** the content of a wrapper, if defined for the shell, **or**:
 - **b)** the shell command content defined in an executable shell command setting item.

Here's the [[Settings for custom shells#Shell arguments|Shell arguments]] setting field in [[Settings for custom shells|custom shell settings]] where `{{!shell_command_content}}` is used:

![[Settings-custom-shell-shell-arguments.png]]

## Wrapper for shell command
> [!Info] Wrappers in custom shells
> Each [[Custom shells|custom shell]] may optionally define a wrapper that consist of normal shell command expressions that prefix and/or postfix the actual shell command in order to perform some preparing and/or finishing tasks, such as:
>  - setting character encodings (prefix)
>  - adding directories to the `PATH` environment variable (prefix)
>  - storing executed shell commands in a log file (prefix/postfix)
>  - converting output from one format to another (postfix)

When used in a wrapper, `{{!shell_command_content}}` gives the shell command content defined in an executable shell command setting item.

Here's the [[Settings for custom shells#Wrapper for shell command|Wrapper for shell command]] setting field in [[Settings for custom shells|custom shell settings]] where `{{!shell_command_content}}` is used:

![[Settings-custom-shell-wrapper-for-shell-command.png]]

> [!tip]- Repeating `{{!shell_command_content}}`
> Like shown in the screenshot above, `{{!shell_command_content}}` and/or `{{shell_command_content}}` can appear multiple times in a wrapper. 

## Order of program flow
When a shell command is executed, both the [[#Shell arguments]] and [[#Wrapper for shell command]] get parsed for [[Variables - general principles|{{variables}}]], and they relate to each other very closely. The program flow for executing a shell command is quite complex and should actually have its own documentation page some day, but here's a simplified principle from the `{{!shell_command_content}}` variable's point of view:

> [!example]- Example shell command definition
> Imagine the following [[Bash]] command:
> ```bash
> echo {{date:YYYY}} >> {{file_path:absolute}}
> ```
> (The command writes the current year to the currently open file.)
> 
> A [[Custom shells|custom shell]] is used:
> - Shell binary path: `/bin/myshell`
> - Shell arguments (defined on separate lines in a settings form):
>  ```bash
>  --login
>  -c
>  {{!shell_command_content}}
>  ```
> - Wrapper for shell command:
>  ```bash
>  # 1. Write log: a shell command is being executed.
>  logFile=/tmp/shellCommandsExecutedFromObsidian.log
>  echo {{date:YYYY-MM-DD HH:mm:ss}}": Executing the following shell command:" >> logFile
>  echo {{shell_command_content}} >> logFile # {{shell_command_content}} without ! escapes special characters so they will not jail-break from the echo command context.
>  
>  # 2. Execute the shell command.
>  {{!shell_command_content}} # Using ! prevents special characters from being escaped, which is needed for the shell command to execute correctly.
>  
>  # 3. Write to log that the execution is now finished.
>  echo {{date:YYYY-MM-DD HH:mm:ss}}": Execution is completed." >> logFile
>  echo "" >> logFile # An empty line to separate future log entries.
>   ```

> [!todo]- Program flow
> 1. `{{variables}}` are first parsed in the actual _shell command_:
>    1. This:
>    ```bash
>    echo {{date:YYYY}} >> {{file_path:absolute}}`
>    ```
>    2. is parsed to:
>    ```bash
>    echo 2023 >> \/home\/my\-user\/obsidian\-vaults\/my\-vault\/my\-note\.md
>    ```
> 2. `{{variables}}` in _Wrapper for shell command_ are parsed to:
>    ```bash
>    # 1. Write log: a shell command is being executed.
>    logFile=/tmp/shellCommandsExecutedFromObsidian.log
>    echo 2023\-03\-19\ 17\:40\:43": Executing the following shell command:" >> logFile
>    echo echo\ 2023\ \>\>\ \\\/home\\\/my\\\-user\\\/obsidian\\\-vaults\\\/my\\\-vault\\\/my\\\-note\\\.md >> logFile # {{shell_command_content}} without ! escapes special characters so they will not jail-break from the echo command context.
> 
>    # 2. Execute the shell command.
>    echo 2023 >> \/home\/my\-user\/obsidian\-vaults\/my\-vault\/my\-note\.md # Using ! prevents special characters from being escaped, which is needed for the shell command to execute correctly.
> 
>    # 3. Write to log that the execution is now finished.
>    echo 2023\-03\-19\ 17\:40\:43": Execution is completed." >> logFile
>    echo "" >> logFile # An empty line to separate future log entries.
>    ```
>    > [!note] Notes: `{{shell_command_content}}` vs. `{{!shell_command_content}}`
>    > - <small>Point 2.1:</small> Backslash ` \ ` characters are **repeated**, as the whole content of `{{shell_command_content}}` is escaped, escaping also the backslashes ` \ ` that were already inserted at point 1.2. That's correct when the aim is to write a literal shell command to a log file. 
>    > - <small>Point 2.2:</small> Backslash ` \ ` characters are **not** repeated for content that came from `{{!shell_command_content}}` (note the exclamation mark `!`). There is the same amount of backslashes ` \ ` as there were at point 1.2. This is correct for executing a shell command.
> 3. `{{variables}}` in _Shell arguments_ are parsed to:
>    ```bash
>    --login -c # 1. Write log: a shell command is being executed.
>    logFile=/tmp/shellCommandsExecutedFromObsidian.log
>    echo 2023\-03\-19\ 17\:40\:43": Executing the following shell command:" >> logFile
>    echo echo\ 2023\ \>\>\ \\\/home\\\/my\\\-user\\\/obsidian\\\-vaults\\\/my\\\-vault\\\/my\\\-note\\\.md >> logFile # {{shell_command_content}} without ! escapes special characters so they will not jail-break from the echo command context.
> 
>    # 2. Execute the shell command.
>    echo 2023 >> \/home\/my\-user\/obsidian\-vaults\/my\-vault\/my\-note\.md # Using ! prevents special characters from being escaped, which is needed for the shell command to execute correctly.
> 
>    # 3. Write to log that the execution is now finished.
>    echo 2023\-03\-19\ 17\:40\:43": Execution is completed." >> logFile
>    echo "" >> logFile # An empty line to separate future log entries.
>     ```
> 4. Finally, the shell's binary file `/bin/myshell` is executed with the arguments shown in the above point 3.

# Availability
> [!Warning] Only available:
> - In [[Settings for custom shells|custom shell settings]] : for defining shell arguments, or a shell command wrapper.
> - Cannot be used as part of a shell command's content. If it were possible, it would cause an infinite recursion. 😅

# History
- #TODO: Add a date [0.19.0 - 2023--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was born. ([#297](https://github.com/Taitava/obsidian-shellcommands/issues/297)).