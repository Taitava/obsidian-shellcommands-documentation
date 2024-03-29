---
cssclass: customiseTitle
aliases:
 - "default value"
---
# Default values for variables
From [[Variables - general principles#^default-values|Variables - general principles]]:
> Not all variables are always available. For example, [[{{file_name}}]] variable cannot be accessed, if the currently active pane does not contain a file. If [[{{file_name}}]] is tried to be used in such a situation, the *Shell commands* plugin will show the following error message: *{{file_name}}: No file is active at the moment. Open a file or click a pane that has a file open.* The shell command's execution is then cancelled.
> 
> - In situations like that, variables can have *default values* that will be used if the normal value is unavailable, and the execution can be continued.
> - Another situation might be, that execution should be cancelled when a variable is unavailable, but no visible error messages are wanted. This might be desirable when executing shell commands via [[Events - general principles|Events]], but the execution is only wanted when the needed variables are available.

> [!Summary] Two ways to define default values
> - [[#Define global default values for all shell commands]]
> - [[#Define shell command specific default values]]
> - In case a variable has a default value defined both globally and for a currently executable shell command, the default value defined specifically for the shell command will be used instead of the global one.

## Define global default values for all shell commands
To define global default values for variables, or to mark a variable to cancel shell command execution silently when it's not available, open up the settings view. In the main view, click the _Variables_ tab:
![[Settings-main-variables-tab.png]]

![[#Define a default value]]

## Define shell command specific default values
To define shell command specific default values for variables, or to mark a variable to cancel shell command execution silently when it's not available, open up the settings view. When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click the *Default values for variables* icon:

![[Settings-main-click-variables.png]]

An *extra options modal* opens up and shows a list of variables. The list excludes variables that are always available. E.g. [[{{date}}]] is not listed, because a date can always be retrieved.

![[Settings-modal-variables.png]]

If you want to know in which situations a certain variable can be inaccessible, hover over its name with the mouse cursor, and a popup box appears with a description of the variable's restrictions.

### Define a default value
If you want to set a default value that will be used when a variable is not available, look for the variable in the list and select *Execute with value:* from the dropdown menu next to it:
![[Settings-modal-variables-Execute-with-value.png]]
Now you can type a free-form default value in the small text area that appears. In the example screenshot above, the default value is defined to be *None*. It could be an empty text, too, in which case you'd just leave the text area empty.

## Use other variables in default values
A really powerful feature is that **you can refer to other `{{variables}}` in the default value field**:
 - For example, if [[{{event_file_name}}]] is unavailable, you can define its default value to be *{{file_name}}* in order to use the value of the [[{{file_name}}]] variable instead.
 - Then, for the possibility that [[{{file_name}}]] might be unavailable, too, you can set that variable's default value to be for example *None* or whatever you want. In other words, default values can be chained. Just make sure not to create circular references (= loops where the default values refer to each other endlessly). The *Shell commands* plugin does not fall into an endless loop in case you happen to do it, the plugin will just leave variables unparsed when they start looping.
 - Default values can also consist of a combination of variables and static text, for example: *No file was open on {{date:YYYY-MM-DD HH:mm:ss}}, but hey, let's see what happens to be in the clipboard: {{clipboard}}*

## Cancel execution without displaying error messages
If you want to cancel the execution without showing up any error messages when a certain variable is not available, look for the variable in the list and select *Cancel execution silently*:

![[Settings-modal-variables-Cancel-execution-silently.png]]

**Please note that selecting this option might make it hard to understand why the shell command is not executed**, if you later forget that you have configured it to cancel silently, because there are literally no visual signs telling why nothing happens. Sometimes error messages can provide valuable information, so choose wisely.

# Should I define default values globally or on a per shell command basis?

> [!Success] When defining default values on a per shell command basis is good
While this might feel a bit complicated to understand at first, it allows a lot of flexibility in a way that each shell command can have a different requirement on what to do when a certain variable is unavailable. For example, one shell command might require [[{{file_name}}]] to default to for example text *None*, while another shell command (a one that is executed very frequently via events), might require [[{{file_name}}]] to just cancel the execution silently when it's not available.

> [!Success] When defining global default values is good
> Defining default values globally is easiest. If different shell commands don't need different values, use global definitions, so you don't have to repeat yourself for each and every shell command.
# [[Custom variables]] do not have values when Obsidian starts

Before a custom variable gets a value (for now, in SC version `0.12.0`, the only way for a custom variable to get a value is via [[Prompts]]), the variable is unassigned, and trying to use it would lead to an error message showing up. You can use the same default value features described on this page to handle the situations when a custom variable is unassigned.

# History
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): Default values can now be defined globally for all shell commands. ([#298](https://github.com/Taitava/obsidian-shellcommands/issues/298)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): The ability to define default values and ignore errors silently was released. ([#190](https://github.com/Taitava/obsidian-shellcommands/issues/190)).

> [!page-edit-history]- Page edit history: 2022-04-09 &#10132; 2023-01-06
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/55c412a9bd41ea75906d1df675a3d5ddd8229ed1): Default values.md: Tell about global default values.
> - [<small>2023-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/9b624e215cde7227187a8a4b4760200a02565f31): Default values.md: Add an alias.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/df021e7305cee4944a440c4c16bf7b3a283dcd1f): Beta 0.12.0: Add notices.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2d3e8929249fc0817a92b10ffe04b8b735d2cb97): 0.12.0: Default values for variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/Default%20values.md).
> ^page-edit-history