---
aliases: [variable]
---
# Variables - general principles
In each shell command, you can use `{{variables}}` to submit data to your commands. You can for example pass the currently open file's path to a command that echoes the current date to the end of that file: `echo {{date:YYYY-MM-DD}} >> {{file_path:absolute}}`.

- Variables are always enclosed within `{{` and `}}`.
- Other characters specific to variables are `:` and `!`. More about them below.
- If you need to use `{{`, `}}`, `:` or `!` to do other things not related to variables, you can use them quite freely, but make sure that you do not accidentally concatenate them with text that forms an existing variable's name. E.g. you can use a literal text `{{variable}}` and you'll have just `{{variable}}`, because there is **no** variable named *variable*. You can also use a literal text `{{date}}` because the [[{{date}}]] variable expects an argument with it, and does not parse without. But you cannot have a literal `{{date:}}`, because that would trigger parsing the [[{{date}}]] variable, resulting in an empty text, because the given argument (*format*) is empty.
- Variables are predefined by SC, you cannot define your own variables. If you have an idea for a new variable, you can [suggest it in the *Ideas* discussion category](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas).

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

# All variables
- [[{{caret_position}}]]
- [[{{clipboard}}]]
- [[{{date}}]]
- [[{{file_extension}}]]
- [[{{file_name}}]]
- [[{{file_path}}]]
- [[{{folder_name}}]]
- [[{{folder_path}}]]
- [[{{selection}}]]
- [[{{tags}}]]
- [[{{title}}]]
- [[{{vault_path}}]]
- [[{{workspace}}]]