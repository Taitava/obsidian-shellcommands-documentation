---
aliases:
 - autocomplete menu
 - autocomplete variable names
---
# Autocomplete variable names
[[Variables - general principles|{{Variables}}]] are handy, but what makes them even handier is a super easy way to access them. When you are [[How to define shell commands|defining a shell command]], just type `{{`, and a dropdown menu like the one below will open up, showing all available variables and instructions:

![[Autocomplete-all-variables.png]]

You can navigate the list by pressing the `Up`/`Down` keys, and insert the selected variable into the command field by pressing the `Enter` key. You can also click a suggestion to do the same thing. Only the bold part of the suggestion will be inserted, the cursive help text is always left out!

If you type a few characters after `{{`, the list of suggested variables is filtered to contain only variables that contain those characters. Filtering rules:
- A suggestion is shown, if it contains the typed characters in the order they are typed, but they do not need to appear next to each other. For example, typing `{{cboard` matches `{{clipboard}}`.
- The filtering is based on the current word at the caret, but excluding characters that appear on the right side of the caret. If the word contains `{{`, all characters before it will be excluded (= *variable search mode*). Examples:
	- (Consider `|` as the caret.)
	- Typing `echo {{ab|` searches suggestions for `{{ab`, so `echo ` is not included.
	- Typing `{{ab|c` searches suggestions for `{{ab`, so `c` is not included.
	- Typing `file-name-prefix{{finame` searches suggestions for `{{finame`, so `file-name-prefix` is excluded.
	- Typing `other-prefix{text-after-a-single-curly-bracket` will search suggestions for the whole text, because a single curly bracket `{` does not trigger *variable search mode*. By default, this will show no suggestions, because the plugin's standard list of suggestions only contains `{{variables}}`; but in case you have created a [[#Create a custom autocompletion file|custom autocompletion file]], some suggestions might be shown.
- To summarize: The following work as *search term boundaries*: a whitespace ` `, and a pair of curly brackets:`{{` / `}}`.

The autocomplete feature is powered by [kraaden/autocomplete](https://github.com/kraaden/autocomplete).

# Turn it off in the settings
Not everyone is a huge fan of suddenly popping up content-hiders and attention-beggars. I used to hate autocompletion menus maybe a bit over decade ago... But then I started loving them and will probably marry one someday :). But if it's not your cup of tea, here's how to get rid of it:
1. Open up the settings panel and select *Shell commands* from the left side menu.
2. Select the *Variables* tab:
![[Settings-main-variables-tab.png]]
3. Turn off the *Show autocomplete menu* toggle.


# Not just for variables - add custom suggestions
The *Shell commands* plugin provides a list of variables for autocompletion, but it doesn't have to end there. Technically, the feature is not limited to suggest only variables. You can make it to suggest for example:
- Commands, e.g.:
	- `echo`: Output text.
	- `mkdir`: Create a new folder.
	- `start`/`open`/`xdg-open`: Open external applications/URLs/whatever.
	- `tar -xvf`: Unpack a tar archive file.
- Arguments for commands, e.g.:
	- `"Hello, World!"`: The ultimate cornerstone of all software testing; the holy grail of programmer inspiration.
- Output streaming, e.g.:
	- `2> /dev/null`: Ignore errors, although there's also [[Ignoring errors|other ways for ignoring errors]].
- Variables with predefined arguments, e.g.:
	- `{{date:YYYY-MM-DD HH:mm:ss}}`: Easily use your favorite date format.
	- `#{{tags:#, }}`: Get a list of #tags, separated by commas + spaces `, `, and prefixed by hashes `#`.

## Create a custom autocompletion file
1. Close Obsidian.
2. Open `.obsidian/plugins/obsidian-shellcommands` folder.
3. Create a file named `autocomplete.yaml` in it (it does not exist by default).
4. Open the file in a regular text editor.
5. The contents of the file will be formatted using YAML syntax. If you are not familiar with them YAML syntax, you can read a bit about it on the [YAML website](https://yaml.org/), or on the [YAML's Wikipedia page](https://en.wikipedia.org/wiki/YAML). But YAML is simple, so there's no need to spend much time reading.
6. Write your custom autocompletion suggestions in the file using the following kind of structure:

	```yaml
	# Text that starts with # is regarded as a comment, and it will not affect the content in any way.
	# All suggestions are placed in groups. The name of a group can be freely decided, and it will appear in the autocompletion menu as a small heading.
	Commands: # Or you could write e.g. "My commands"
	  # IMPORTANT! Indentation MUST be made using two spaces - no more, no less, and no tabs!
	  # Write the actual suggestion before a colon, and a descriptive help text after it. The help text will be shown in the autocomplete menu, but it will NOT be inserted into a command field.
	  echo: Output text.
	  mkdir: Create a new folder.
	  start: Open external applications/URLs/whatever.
	  tar -xvf: Unpack a tar archive file.

	Arguments for commands:
	  # You can wrap texts in double quotes, but it's optional. If you want to use double quotes as literal characters in your text, write them like this: \"
	  "\"Hello, World!\"": "The ultimate cornerstone of all software testing; the holy grail of programmer inspiration."

	Output streaming:
	  "2> /dev/null": "Ignore errors."

	# Use Variables as a group name if you wish to add suggestions to the very same Variables suggestion group that the SC plugin uses.
	Variables:
	  "{{date:YYYY-MM-DD HH:mm:ss}}": "Easily use your favorite date format.""
	  "#{{tags:#, }}": "Get a list of #tags, separated by commas + spaces, and prefixed by hashes.""
	  
	# Notes:
	# - It's not possible to remove or modify the default, built-in variable suggestions, although you can add your own next to them.
	# - Formatting text with HTML, Markdown or anything else is not supported.
	```
	(You can copy the content and start editing it.)

7. Save the file and launch Obsidian again.
8. You should now be able to see your custom suggestions in the autocompletion menu.

## Example lists for autocompletion
The following pages contain ready made lists of commands for different shells and operating systems. You can include any of them (or many of them) in your `autocomplete.yaml` file. The lists contain (short) instructions for the commands, too, so this is a really good way to learn new shell commands!

- [[Custom - Ubuntu Bash commands]]
- [[Custom - Windows CMD commands|Windows CMD commands]]
- [[Custom - Windows PowerShell 5]]

# History
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Autocompletion was added to:
	- Shell command *Alias* field ([#182](https://github.com/Taitava/obsidian-shellcommands/issues/182)).
	- Different fields in [[Prompts|Prompt]] settings ([#37](https://github.com/Taitava/obsidian-shellcommands/issues/37)).
- [0.9.0 - 2021-12-18](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#090---2021-12-18): Fix: Autocomplete suggests variables when typing right after a closing }} pair ([#129](https://github.com/Taitava/obsidian-shellcommands/issues/129)).
- [0.8.0 - 2021-12-10](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#080---2021-12-10): Autocompletion was added. Uses [kraaden/autocomplete](https://github.com/kraaden/autocomplete) ([a development version](https://github.com/kraaden/autocomplete/commit/1590fe09d347f7b6cb1466add5d8e5652bf9d1fb) after 6.1.2, adding support for regenerating the list also when a user presses left/right keys). ([#33](https://github.com/Taitava/obsidian-shellcommands/issues/33)).