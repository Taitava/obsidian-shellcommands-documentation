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

After you finish setting up the prompt, you'll need to go to some shell command's settings and select the prompt you created in order to enable opening it when the shell command executes. Follow the instructions in [[#Create a prompt from a shell command's settings modal create-prompt-from-shell-command]] to see how to pick a prompt for a shell command.

## Configuring a prompt's settings ^configuring-prompt-settings
![[Settings-prompt-new-prompt.png]] ^prompt-settings-screenshot

Fill in the following information:
- *Prompt title*
- *Description* (optional): Longer text if you need to write some instructions on how the executable shell command works.
- Create new fields by clicking the *New field* button. Fill in the field details:
	-  Field type on the field's heading line: Choose either _Single line text_ , _Multiline text_, _Toggle_ or _Dropdown menu_.
	- *Field label*: A question or other label.
	- *Default value*: What the field will contain at the beginning when the prompt is opened. Tip: if you want the prompt to remember the last used value, put here the same variable that you will use in the *Target variable* field, e.g. `{{_my_variable}}`.
	- *Description*: More detailed instructions on how to fill this field.
	- *Target variable*: You need to select a [[Custom variables|custom variable]] where the prompt will store the inputted value.
		- Custom variables are `{{variables}}` that you can create yourself in the settings, and here the dropdown menu also offers you an option to *Create a new custom variable*. By selecting that, you will be asked a name for a new custom variable. Custom variables always start with `{{_` and end with `}}`, e.g. `{{_my_variable}}`.
		- You can insert the custom variable's name into your shell command to access the inputted value there.
		- You cannot use a custom variable as a target if it's already used in another field in the **same** prompt. However, if you have multiple prompts, you may use the same custom variable as a field's target variable in different prompts.
	- *Is required*: If this is on, a user cannot accidentally submit the prompt and execute a shell command if the field is left empty.
	- Other fields: Depending on which type of prompt field you selected, you might see additional settings. These are covered below.
- *Execute button text*: Make the button that executes a shell command to show more specifically, what will be done. Examples: *Create the file*, *Open the application*, *Delete the file*, *Do the custom search in the vault*.

### Different types of fields

> [!Info]- Single line text
> - A very basic type of input. Allows typing text on one line without line breaks.
> - Has no additional setting fields.
> - Uses the HTML `<input type="text">` element under the hood.
> - Before SC version `0.21.0`, this was the only supported prompt field type.

> [!Info]- Multiline text
> - Allows typing text on multiple rows. Lines will be separated by [newline characters (`\n`)](https://en.wikipedia.org/wiki/Newline) regardless of platform (Windows, Linux, or macOS).
> - First appears in single line height, but grows when the `Enter` key is pressed.
> - Has no additional setting fields.
> - Uses the HTML `<textarea>` element under the hood.
> - Available since SC version `0.21.0`.

> [!Info]- Toggle
> - A simple on/off switch field for choosing between two states.
> - As all field types must produce a textual value, _Toggle_ provides two additional settings for defining its textual value for both states:
>     - _Result when toggled on_
>     - _Result when toggled off_
>     - For example, the _on_ result can be a flag `--verbose` to a shell command, and the _off_ result can be an empty string for situations where the flag is not wanted. E.g. A complete shell command `git add {{!_verbosity}}` can become either `git add --verbose` or just `git add `.
>     - These settings are also used during Prompt opening, when interpreting a _Default value_ for the Toggle field. If _Default value_ matches _Result when toggled on_, the toggle will be turned on by default, otherwise off. The matching is not case-sensitive. (If _Default value_ happens to be something that matches neither the _on_ result, nor the _off_ result, the toggle's starting state will be off.)
>     - [[Variables - general principles|{{variables}}]] can be used to make the toggle provide dynamic values.
> - If _Is required_ is turned on, then a Prompt is only allowed to be submitted if the toggle is turned **on**. This can be used as an extra confirmation when executing a potentially dangerous shell command. Otherwise, having _Is required_ on for a toggle does not make much sense.
> - Uses the HTML `<input type="checkbox">` element under the hood, which Obsidian renders as a more modern looking toggle element: ![[Toggle.png]]
> - Available since SC version `0.21.0`.

> [!Info]- Dropdown menu
> - Allows choosing one value from a list of choices.
> - The available values are defined in _Choices_ setting, which takes multiline list:
>     - Each line defines one choice.
>     - If a line contains a pipe `|` then the left part of the line is used as a value for a target variable (not shown in the dropdown menu), and the right part is used as a visual label in the dropdown menu.
>     - If no pipe `|` is present on a line, then the whole line is used both as a value and a label.
>     - If a line contains multiple pipes `|` then only the first one works as a separator between a value and a label. Later pipes will be considered as part of the label.
>     - If you need to have a pipe `|` present in the value part, then I'm sorry, it's not possible via the user interface. But you can edit the settings file (`.obsidian/plugins/obsidian-shellcommands/data.json`) and add it there. Please [ask me on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/17) for instructions.
>     - [[Variables - general principles|{{variables}}]] can be used as choices. For example, you can provide the current [[{{file_name}}]] as a choice.
> - _Default value_ setting is used to pre-select a choice when a Prompt is opened. The _Default value_ is tried to be matched to one of the choice values (no case-sensitivity), but if there's no match, then the first choice will be selected.
> - If _Is required_ is turned on, then a Prompt is only allowed to be submitted if the selected value is not an empty string. So, if you want, you can define an empty line as a first choice, to make the Prompt not able to submit if the empty line is selected. Similarly, you can define `=Choose an option` to define a choice with an empty value.
> - (If you enter a value that only consists of number(s), it may appear out of its original position when the dropdown menu is shown. This is due to the nature of [how JavaScript's Object properties are ordered](https://stackoverflow.com/a/5525820/2754026).) <!-- I could improve this later, by preceding each value with e.g. an underscore, and then removing it from the value when reading it. -->
> - Uses the HTML `<select>` element under the hood.
> - Available since SC version `0.21.0`.

> [!Info]- Password
> - Similar to _Single line text_ (allows typing text on one line without line breaks), but shows a cloaked text &bullet;&bullet;&bullet; instead of the typed characters.
> - Variable values that came from a _Password_ field are also cloaked when shown in a prompt's shell command preview or _[[Custom variables#Monitor the custom variable values|Custom variables pane]]_.
> - Has no additional setting fields.
> - Uses the HTML `<input type="password">` element under the hood.
> - Available since SC version `0.21.0`.

### Variables
> [!Tip] Using `{{variables}}` diversely in Prompts
> All textual settings in Prompts **support [[Variables - general principles|{{variables}}]]** and [[Autocomplete|autocompletion]]!
>  - You can customise your description texts with information from your vault.
>  - You can define the default value of a field to consist of multiple variables, e.g. `Year {{date:YYYY}} and current file name {{file_name}}`.
>  - Also, when you finally execute a shell command that opens up a prompt, all text fields support [[Variables - general principles|{{variables}}]] and [[Autocomplete|autocompletion]].

### Previewing the prompt
After you have filled in the prompt's information, click the small icon button next to the *Prompt title* field. You'll see a prompt modal opening up, showing how the prompt looks like.

This prompt cannot execute any shell commands, because it's just a preview. **However**, if you click the execution button in the prompt modal, the prompt **will store the field values into the specified target variables**.

# Accessing inputted values afterward
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
> This CSS snippet makes text bold in a prompt whose **id** is *w3ocyqvjxb*. It doesn't change anything in any other prompt. Each prompt has a unique id, and you need to check your prompt's id from its settings. [[#^prompt-settings-screenshot|See the bottom of the prompt settings screenshot above]].
> 
> (The `div` keyword can be removed, it's just there to indicate that the modal element is an HTML `<div>` element.)

# History
- [0.21.0 - 2023-12-30](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0210---2023-12-30): New field types in addition to the original single line text: multiline text, toggle, dropdown menu and password. ([#365](https://github.com/Taitava/obsidian-shellcommands/issues/365)).
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): Hitting the `Enter` key in the prompt modal now closes it and executes the shell command. ([#216](https://github.com/Taitava/obsidian-shellcommands/issues/216)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): The support for prompts was released. ([#37](https://github.com/Taitava/obsidian-shellcommands/issues/37)).

> [!page-edit-history]- Page edit history: 2022-04-08 &#10132; 2023-12-10
> - [<small>2023-12-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f0e78b1a4c80d2a45e14b41a34addd11188a1d84): [[Prompts.md]]: Small changes to dropdown menu texts.
> - [<small>2023-12-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cc669e9f9b7830bdb91da48c40e31d9d135e0427): [[Prompts.md]]: Information about Password field type.
> - [<small>2023-08-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/90149bdd741c193d1a1c674b7a0b8b0b37717a0c): Prompts.md: Information about different prompt field types.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/02e98b52d70617d390d8b1dbfda581c9e03151bd): Prompts.md and {{event_old_folder_path}}.md: Typo fixes.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/946bdf5546a1580a4332cce169aa03a65ca9f0b9): Modals: Mention in history records that modals can be closed by hitting the 'Enter' key.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e8291571f084c53ecb9e7ed537ec4b6356a5008): Prompts: Add CSS instructions.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ddb140ebf5f8abd8a3b0b68acb954a6aee9cdc69): Beta 0.12.0: Add notice to Prompts.md.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/94015379ec1574b16f7ad2c60413b063792a1070): 0.12.0: Rename Settings-main-click-preactions.png image file.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/527ccff928a6af819d2237c7f98db8e18acf6cea): Prompts: Execute button text supports variables now.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7b150874ec1ec2620b683cc44075bd8205e4e518): Prompts: Restructure target variable instructions and mention that the same variable cannot be used in multiple fields.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/61658656e301113c3139c1b1dfe1653d0e4a0063): 0.12.0: Instructions for Prompts.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Preactions/Prompts.md).
> ^page-edit-history