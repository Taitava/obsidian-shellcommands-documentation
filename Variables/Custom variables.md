---
aliases:
  - custom variable
---
![[Variables - general principles#^custom-variables-can-be-used-for]]

Custom variables are *"storage slots"* that can contain values. You will create all the custom variables you need, by default there is no custom variables, and not everybody will need them.

Custom variables are needed, if...
 - ...you use [[prompts]] to ask values from a user when a shell command is about to be executed. When a user inputs values into a prompt's fields and then submits the prompt, the inputted values are stored into custom variables. Each prompt field has a designated custom variable (decided by you) that will get the value from the field.
 - ...you use [[Shell commands URI]] to pass values to your shell commands
 - ...you need to do intermediate data storing by [[Output channel - Assign custom variables|assigning output from one shell command into custom variables]], and then inputting it to another shell command in a later phase of your workflow.

Your shell commands can use custom variables the same way as any other variables, to retrieve the inputted/passed value.

## Value preservation
- Custom variables hold their values even after the shell command using them is executed, so you can use them later in other shell commands, if needed.
- However, custom variables lose their values when Obsidian quits or the *Shell commands* plugin is disabled and re-enabled. So, the values are **not** stored on file system. Support for [persisting custom variable values on file system is under consideration](https://github.com/Taitava/obsidian-shellcommands/discussions/146#store-on-disk).

## No value at the beginning
When Obsidian starts, all custom variables are *unassigned*, i.e. they do not have a value.
- If a shell command tries to read a custom variable that has no value yet, it will fail with an error message: *This custom variable does not have a value yet, and no default value is defined.*
- If a shell command has been configured to open up a [[Prompts|prompt]] that sets the custom variable, then it's okay, no error message will be shown, as the custom variable will eventually get a value.
- You can also define a [[Default values|default value]] for your custom variable, in which case the default value will be used every time the custom variable does not have a value.

# How to create custom variables
Custom variables can be created from these places:
- The *Variables* tab on the plugin's [[How to define shell commands#Main controls for shell commands shell-command-controls|main settings view]]. Here you can also edit the variables after creation. This will be covered below.
- [[Prompts#Configuring a prompt's settings configuring-prompt-settings|Prompt field settings]]. Can only create new variables, editing existing ones cannot be done here.

## Creating custom variables in the main settings
1. Open up the *Variables* tab on the plugin's [[How to define shell commands#Main controls for shell commands shell-command-controls|main settings view]]:
	![[Settings-main-variables-tab.png]]
2. Click the *New custom variable* button. Fields for a new custom variables will appear:
	![[Settings-main-variables-new-custom-variable.png]]
3. Decide a name for the custom variable. By default, the *Shell commands* plugins defines a unique numeric name (starts from `{{_1}}`), but it's highly recommended to change the numeric name to something more meaningful so that you'll remember what the variable is used for.
4. After typing a name, check that the bold heading text shows the variable's name. If there's something wrong with the name, the bold heading will display an error message instead.
5. Optional: Type a description. This is just to help further remind yourself on how to use this variable, or what kind of content it will contain. Can be left empty, if the variable's name is very self-explanatory.

## Naming rules
- A custom variable's name starts with `{{_` and ends with `}}`, but you will not type these in the name field, you'll only type the inner part of the name. The underscore `_` is there to help dissociate custom variables from the plugin's own, built-in variables. This way future additions to the built-in variables will avoid colliding with the custom variables you define.
- The name can only contain the following characters:
	- Letters `a` - `z`. Case does not matter, you can define e.g. `{{_my_variable}}` and use it in a shell command like `{{_MY_VARIABLE}}` or `{{_My_VaRiAbLe}}`. However, a good common practise is to always write all variable names with lowercase letters.
	- Numbers `0` - `9`
	- An underscore `_`
	- Similar rules are very common in many programming languages.
- Minimum length for the internal part between `{{_` and `}}` is one character. E.g. `{{_x}}` meets the minimum length requirement.
- The name must be unique. You cannot make two custom variables with the same name.

## Renaming a custom variable
Custom variables can be renamed via the *Variables* tab in the main settings view, in the same way how new custom variables are created.

- If you rename a custom variable in the settings, **remember to change its name in your shell commands, too**!
- However, possible prompt field settings will not need any changes, as they can still use the same variable even after renaming.

# Monitor the custom variable values
To see what values your custom variables currently contain, you may open a *Custom variables pane*:

> [!TODO]- Open up the _Custom variables_ pane from settings
> 1. Open up the *Variables* tab on the plugin's [[How to define shell commands#Main controls for shell commands shell-command-controls|main settings view]]:
>   ![[Settings-main-variables-tab.png]]
> 2. Click the small icon near the *Custom variables* heading that has a tool-tip: *Open a pane that displays all custom variables and their values*.
> 3. Close the settings modal, and you'll see a new side pane:
>   ![[Pane-custom-variables.png]]

> [!TODO]- Open up the _Custom variables_ pane from the left side ribbon
> 1. The following icon should be visible in Obsidian's sidebar. Click on it:
>   ![[Ribbon-Custom-variables-icon.png]]
> 2. You should now see a new side pane:
>   ![[Pane-custom-variables.png]]

> [!TODO]- How to remove the icon from the left side ribbon - or add it back
> If you want to avoid icons cluttering your sidebar, you can remove the _Custom variables_ icon by [customizing the ribbon](https://help.obsidian.md/User+interface/Ribbon#Desktop).
> The same method allows you to add the icon back.

The side pane can currently only be used to read values. It doesn't provide any other functions.

## Show notifications when values change

From SC version `0.22.0` onwards, the plugin displays a notification balloon by default every time a custom variable's value is changed by any of the following methods:
- [[Shell commands URI]]
- [[Output channel - Assign custom variables|Assign custom variables]] output channel

(Note that notifications are not displayed when custom variable values are changed manually, i.e. via [[Prompts]].)

> [!Example] Example notification
> ![[Balloon-Custom-variable-change.png]]
> The first line contains the variable name, under which is the assigned value.
> ^value-change-example-notification

### How to disable notifications about value changes
1. Open up the main settings view and go to the *Variables* tab:
  ![[Settings-main-variables-tab.png]]
2. Look for the setting _Show notifications when values of custom variables change_ and select the desired options from the dropdowns:
  - _Via URI: Notify_ / _Via output assignment: Notify_
  - _Via URI: Don't notify_ / _Via output assignment: Don't notify_
# History
- [0.23.0 - 2024-11-09](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0230---2024-11-09): Fixed a bug that caused custom variables not to work in certain situations on Obsidian 1.7.2 and newer. ([#433](https://github.com/Taitava/obsidian-shellcommands/issues/433)).
- [0.22.0 - 2024-05-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0220---2024-05-05):
    -  A new output channel [[Output channel - Assign custom variables|Assign custom variables]] can now be used to set values to custom variables. ([#382](https://github.com/Taitava/obsidian-shellcommands/issues/382)).
    - [[#Monitor the custom variable values|Custom variables view]] can now be opened via a ribbon icon in the left sidebar of Obsidian. ([#386](https://github.com/Taitava/obsidian-shellcommands/issues/386)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): The support for custom variables was released. ([#159](https://github.com/Taitava/obsidian-shellcommands/issues/159)).

> [!page-edit-history]- Page edit history: 2022-04-11 &#10132; 2024-01-21
> - [<small>2024-01-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/233fb638fcc6bcdc5ce0a25a3fc461805df43f86): [[Custom variables.md]]: Information about a ribbon icon for the _Custom variables_ pane.
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b01077427009d4cf1d32f7556cd2f8343ac50a1e): [[Custom variables.md]]: Default values can nowadays be configured globally, too.
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3b15d62c0164dd1b8cc676a40a21e2aaf062704f): New output handler [[Output channel - Assign custom variables.md]].
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/14f72e02f10127df4aef4661a14386d91a1217a7): [[Custom variables]] now display a notification when their values change.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/26f2ed84d4663901ff516fbc140f9e82ffd2a392): Custom variables.md: Add information about Shell commands URI.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/df021e7305cee4944a440c4c16bf7b3a283dcd1f): Beta 0.12.0: Add notices.
> - [<small>2022-04-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/91702a4b6edda4a90120067de22de23a26383240): Custom variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/Custom%20variables.md).
> ^page-edit-history