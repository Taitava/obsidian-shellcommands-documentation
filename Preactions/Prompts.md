# Prompts
Prompts are a customisable way to ask a user to input a value - or multiple values - when a shell command is about to be executed.

Some examples on what can be asked:
- A name for a new file.
- A date, defaulting to the current date, which a user can customise. E.g. apply some process to your [Daily notes](https://help.obsidian.md/Plugins/Daily+notes) files.
- Additional flags/parameters for a shell command.

## An example prompt

![[Prompt-Example-Hi-I-am-a-Prompt.png]]

Prompts include the following elements, that all can be customised:
- A title: *Hi, I am a Prompt!*
- A description: *Nice to meet you. This is my description.*
- A preview text showing the shell command in the form it is about to be executed. The preview can be turned off in the prompt's settings.
- Fields:
	- Field name: *What is your name* / *How old are you?*
	- Field description: *Please type your name here.*
	- Default value: *Bond, James Bond* / *33*
	- You can have as many fields as you want.
	- Fields can be marked as required (= cannot be left empty) or optional (= can be empty).
- A button to finally execute the shell command: *I'm ready to submit my details to some program!*

### The example prompt's settings
This is how the example prompt's configuration looks like:
![[Settings-prompt-Example-Hi-I-am-a-Prompt.png]]

# Creating prompts
Prompts can be created in two ways:
- [[#^create-prompt-from-shell-command|From the *Preactions* tab in a shell command's settings modal]].
- [[#^create-prompt-from-main-settings|From the *Preactions* tab in the main settings view]].

The former is the simplest, if you already have a shell command where you'd like to use a prompt.

## Create a prompt from a shell command's settings modal ^create-prompt-from-shell-command
1. When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click the *Preactions* icon to open up an *extra options modal*:
	![[Settings-main-click-preactions-icon.png]]
2. In the modal, select *Create a new prompt*:
	![[Settings-modal-preactions.png]]
3. Another modal with a new prompt's settings opens up. Continue reading from [[#^configuring-prompt-settings|Configuring a prompt's settings]].

## Create a prompt from the main settings view ^create-prompt-from-main-settings
1. Open [[How to define shell commands#^shell-command-controls|the settings]] and the *Preactions* tab:
	![[Settings-main-preactions-tab.png]]
2. Click the *New prompt* button.
3. Another modal with a new prompt's settings opens up.

After you finish setting up the prompt, you'll need to go to some shell command's settings to and select the prompt you created in order to enable opening it when the shell command executes. Follow the instructions in [[#Create a prompt from a shell command's settings modal create-prompt-from-shell-command]] to see how to pick a prompt for a shell command.

## Configuring a prompt's settings ^configuring-prompt-settings
![[Settings-prompt-new-prompt.png]] ^prompt-settings-screenshot

Fill in the following information:
- *Prompt title*
- *Description* (optional): Longer text if you need to write some instructions on how the executable shell command works.
- Create new fields by clicking the *New field* button. Fill in the field details:
	- *Field label*: A question or other label.
	- *Default value*: What the field will contain at the beginning when the prompt is opened. Tip: if you want the prompt to remember the last used value, put here the same variable that you will used in the *Target variable* field, e.g. `{{_my_variable}}`.
	- *Description*: More detailed instructions on how to fill this field.
	- *Target variable*: You need to select a [[Custom variables|custom variable]] where the prompt will store the inputted value.
		- Custom variables are `{{variables}}` that you can create yourself in the settings, and here the dropdown menu also offers you an option to *Create a new custom variable*. By selecting that, you will be asked a name for a new custom variable. Custom variables always start with `{{_` and end with `}}`, e.g. `{{_my_variable}}`.
		- You can insert the custom variable's name into your shell command to access the inputted value there.
		- You cannot use a custom variable as a target if it's already used in another field in the **same** prompt. However, if you have multiple prompts, you may use the same custom variable as a field's target variable in different prompts.
	- *Is required*: If this is on, a user cannot accidentally submit the prompt and execute a shell command if the field is left empty.
- *Execute button text*: Make the button that executes a shell command to show more specifically, what will be done. Examples: *Create the file*, *Open the application*, *Delete the file*, *Do the custom search in the vault*.

### Variables
All of the abovementioned text elements **support `{{variables}}`** and [[Autocomplete|autocompletion]]!
 - You can customise your description texts with information from your vault.
 - You can define the default value of a field to consist of multiple variables, e.g. `Year {{date:YYYY}} and current file name {{file_name}}`.
 - Also, when you finally execute a shell command that opens up a prompt, all text fields support `{{variables}}` and [[Autocomplete|autocompletion]].

### Previewing the prompt
After you have filled in the prompt's information, click the small icon button next to the *Prompt title* field. You'll see a prompt modal opening up, showing how the prompt looks like.

This prompt cannot execute any shell commands, because it's just a preview. **However**, if you click the execution button in the prompt modal, the prompt **will store the field values into the specified target variables**.

# Accessing inputted values afterwards
After a custom variable is assigned with a value (by a prompt, or in some later version by other means), it stores its value even after the shell command is executed. You can use the same custom variable in another shell command, even if that shell command does not open up a prompt, and so the two shell commands can share the same custom value.

You can also [[Custom variables|display the current custom variable values in a side pane]]. Custom variable values are lost when Obsidian quits or the *Shell commands* plugin is reloaded.

# Styling prompts with CSS
Prompts are something that you create yourself, so you should also be able to customise how they look and feel, if you want. This is completely optional, and the default layout for prompts is tried to be designed in a way that suits most typical use cases.

> [!INFO] CSS
> CSS (*Cascading style sheets*) is a web technology used to define layouts for websites and applications. It's a wide, wide thing to explain here, and requires a lot of learning and effort to master well, but you can try to learn some simple things. [Here's one CSS tutorial for beginners](https://www.freecodecamp.org/news/get-started-with-css-in-5-minutes-e0804813fc3e/).
> 
> The Obsidian community has a lot of kind members who help each other to come up with small (and not so small) CSS snippets that can accomplish certain features, such as changing the position or width/height of an element, or changing colors. If you have specific CSS questions related to prompts, feel free to ask them in the [*Q & A* discussion category of the *Shell commands* plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/q-a).

Prompts offer you two simple CSS classes that you can build your customisations on. If you feel that you'd need something more from the CSS API, just ask in the GitHub discussion linked above, and I'll see if I can do some improvements to support custom CSS better!

Create a file in `.obsidian/snippets` folder. Name the file for example `prompts.css`. Add one (or both) of the following two CSS snippets as content to the file and enable the snippet in Obsidian's appearance settings. [More help on creating CSS snippet files](https://help.obsidian.md/How+to/Add+custom+styles#Use+Themes+and+or+CSS+snippets).

> [!EXAMPLE] Example: CSS for all prompts
> ```css
> div.SC-prompt-modal {
> 	background-color: red;
> }
> ```
> This CSS snippet changes the background color of all prompts to red. It's not so nice looking, but it works as a good starting point for your own customisations.
> 
> (The `div` keyword can be removed, it's just there to indicate that the modal element is an HTML `<div>` element.)

> [!EXAMPLE] Example: CSS for a specific prompt
> ```css
> div.SC-prompt-modal-w3ocyqvjxb {
> 	font-weight: bold;
> }
> ```
> This CSS snippet makes text bold in a prompt whose **id** is *w3ocyqvjxb*. It doesn't change anything in any other prompt. Each prompt has a unique id, and you need to check your prompt's id from it's settings. [[#^prompt-settings-screenshot|See the bottom of the prompt settings screenshot above]].
> 
> (The `div` keyword can be removed, it's just there to indicate that the modal element is an HTML `<div>` element.)

# History
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): Hitting the `Enter` key in the prompt modal now closes it and executes the shell command. ([#216](https://github.com/Taitava/obsidian-shellcommands/issues/216)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): The support for prompts was born. ([#37](https://github.com/Taitava/obsidian-shellcommands/issues/37)).