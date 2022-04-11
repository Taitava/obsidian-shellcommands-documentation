# Custom variables
Quote from [[Variables - general principles#^custom-variables|Variables - general principles]]:
> Custom variables can be created to store values inputted by a user via [[prompts]]. Later, custom variables will be able to receive values from many sources:
> - [Planned: Output channel: Custom variable](https://github.com/Taitava/obsidian-shellcommands/discussions/127)
> - [Planned: Execute shell commands via Obsidian URI](https://github.com/Taitava/obsidian-shellcommands/discussions/195)
> - Anything else? [Throw me ideas 😉](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas)

Custom variables are *"storage slots"* that can contain values. You will create all the custom variables you need, by default there is no custom variables, and not everybody will need them.

Custom variables are needed, if you use [[prompts]] to ask values from a user when a shell command is about to be executed. When a user inputs values into a prompt's fields and then submits the prompt, the inputted values are stored into custom variables. Each prompt field has a designated custom variable (decided by you) that will get the value from the field. Your shell command can then use the custom variable in the same way as any other variable, to retrieve the inputted value.

## Value preservation
- Custom variables hold their values even after the shell command using them is executed, so you can use them later in other shell commands, if needed.
- However, custom variables lose their values when Obsidian quits or the *Shell commands* plugin is disabled and re-enabled. So, the values are **not** stored on file system. Support for [persisting custom variable values on file system is under consideration](https://github.com/Taitava/obsidian-shellcommands/discussions/146#store-on-disk).

## No value at the beginning
When Obsidian starts, all custom variables are *unassigned*, i.e. they do not have a value.
- If a shell command tries to read a custom variable that has no value yet, it will fail with an error message: *This custom variable does not have a value yet, and no default value is defined.*
- If a shell command has been configured to open up a [[Prompts|prompt]] that sets the custom variable, then it's okay, no error message will be shown, as the custom variable will eventually get a value.
- You can also define a [[Default values|default value]] for your custom variable, in which case the default value will be used every time the custom variable does not have a value. Default values are shell command specific, and so they are configured in shell command settings, not in the custom variable's own settings.

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
1. Open up the *Variables* tab on the plugin's [[How to define shell commands#Main controls for shell commands shell-command-controls|main settings view]]:
	![[Settings-main-variables-tab.png]]
2. Click the small icon near the *Custom variables* heading that has a tool-tip: *Open a pane that displays all custom variables and their values*.
3. Close the settings modal, and you'll see a new side pane:
	![[Pane-custom-variables.png]]

The side pane can currently only be used to read values. It doesn't provide any other functions.

# History
- #TODO: Add a date [0.12.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The support for custom variables was born. ([#159](https://github.com/Taitava/obsidian-shellcommands/issues/159)).