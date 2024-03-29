---
cssclass: customiseTitle
---
# Variable: `{{environment}}`
> [!Quote] {{environment}} described in the *Shell commands* plugin's settings
> Gives an environment variable's value. It's an original value received when Obsidian was started.

This variable can be used to read any environment variable in the state it was when Obsidian was started.

> [!Info] Environment variables
> [Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are "settings" that can be used to change how certain shells, commands and programs work. Each operating system defines their own set on environment variables, but custom programs can also use some environment variables.
> 
> The most common environment variables can be found from the following lists:
> - [Unix (Linux / macOS) environment variables](https://en.wikipedia.org/wiki/Environment_variable#Unix_2)
> - [Windows environment variables](https://en.wikipedia.org/wiki/Environment_variable#Windows)

## Retrieve the value of `PATH`
The actual reason for this variable to exist is that it can be used when [[Additions to the PATH environment variable#An easier way to add directories to PATH|adding new directories to the `PATH` environment variable]]. If `{{!environment:PATH}}` is present in a *PATH additions* setting, it's then possible to decide whether to add directories before or after the current content of `PATH`. Using the variable there is optional: if it's not present, all additions are added **after** the current content.

> [!Important]
> `{{environment}}` always gives the value the environment variable had *when Obsidian was started*. If you use `{{environment:PATH}}`, pay attention to the fact that it doesn't contain any of the [[Additions to the PATH environment variable#An easier way to add directories to PATH|additions you have possibly made to `PATH` in the settings]].

![[Additions to the PATH environment variable#^no-escaping]]

## Case sensitivity or insensitivity
- If you are using Linux or macOS, the environment variable names are case-sensitive. Usually they should be written with ALL CAPITAL LETTERS.
- However, if you are using Windows, the letter casing does not matter.

**Examples:**
> [!Fail] Linux/macOS
> Wrong: `{{environment:path}}`
> Wrong: `{{environment:Path}}`
> 
> These would lead to the following error message showing up: 
> > [!Fail] {{environment}}: Environment variable named 'path' does not exist.
> 
> Shell command execution would then be cancelled.

> [!Success] Linux/macOS
> Correct: `{{environment:PATH}}`

> [!Success] Windows
> Correct: `{{environment:path}}`
> Correct: `{{environment:Path}}`
> Correct: `{{environment:PATH}}`

## Alternative: Read environment variables using standard shell syntax
Apart from using the `{{environment}}` variable when [[Additions to the PATH environment variable#An easier way to add directories to PATH|adding new directories to the `PATH` environment variable]], the variable does not offer much benefit in the actual shell command context. If you want to use environment variables in your *shell commands*, it might be more natural to use the standard syntax your shell provides:
- For Bash/Dash/Zsh (Linux/macOS): `echo $VARIABLE`
- For CMD (Windows): `echo %VARIABLE%`
- For PowerShell (Windows): `echo $Env:VARIABLE`

Replace *`VARIABLE`* with the environment variable name you want to read. `echo` is just an example shell command, replace it with a command you want to use.

> [!Info] Difference: `$PATH`/`%PATH%`/`$Env:PATH` versus `{{environment:PATH}}`
> Even though `{{environment}}` usually gives the same value as the standard shell syntax for reading environment variables, there is a slight difference between `$PATH`/`%PATH%`/`$Env:PATH` vs. `{{environment:PATH}}`, like discussed [[#Retrieve the value of PATH|above]]:
> - `echo {{environment:PATH}}` gives the `PATH` value without any custom additions.
> - `echo $PATH`/`%PATH%`/`$Env:PATH` gives a `PATH` value that contains also custom additions. This only works in a *shell command*, not in a *PATH additions* setting field!

# Availability
> [!Warning] Only available:
> If the passed environment variable name exists.


# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The variable was released. ([#204](https://github.com/Taitava/obsidian-shellcommands/issues/#204)).

> [!page-edit-history]- Page edit history: 2022-05-01 &#10132; 2022-06-28
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-05-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ec4c6a61c51fc5c5a9c2ddb78469e671cffae9d1): 'PATH additions' settings: {{environment}} should be {{!environment}}.
> - [<small>2022-05-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/78d81b39be6c97aecac9c7229c5419e4dd0a81cd): {{environment}} variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Benvironment%7D%7D.md).
> ^page-edit-history