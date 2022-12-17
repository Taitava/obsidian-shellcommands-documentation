---
cssclass: customiseTitle
---
# Variable: `{{selection}}`
> [!Quote] {{selection}} described in the *Shell commands* plugin's settings
> Gives the currently selected text.

## Availability
> [!Warning] Only available:
> When something is selected in <em>Editing</em>/<em>Live preview</em> mode, <strong>not</strong> in <em>Reading</em> mode.

I'd like to make this variable available in *Reading* view too, but I don't know how. In case you are familiar with Obsidian API or know other plugins that are able to access the selected text in *Reading* view, [please let me know in this GitHub issue](https://github.com/Taitava/obsidian-shellcommands/issues/2).

## If nothing is selected

`{{selection}}` will show an error message and prevent execution (as of SC `0.18.0`), if nothing is selected. This is to allow users to better customise what to do when nothing is selected:
 - Show an error message and cancel. Good to prevent accidental execution in cases where it's necessary to ensure that some text is selected.
 - Cancel silently. Good if you want to define automatic [[Events - general principles|events]] and only need them to execute when something is selected, and cancel otherwise without showing errors.
 - Restore the old behavior by defining the variable to use an empty value as its default value. [[Default values|How to define default values]].
 - Freely define an alternative text. E.g. `NO-SELECTION` can be defined as a default value.

(In SC `0.17.0` and below, the variable gave an empty text when nothing was selected.)

## See also
- [[{{caret_position}}]]

# History
<small>This page was last modified on <strong>2022-12-10</strong> and created on 2021-11-19. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bselection%7D%7D.md">See page edit history</a>.</small>
- #TODO: Add a date [0.18.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable is now only available when something is selected, otherwise it shows an error message. ([#303](https://github.com/Taitava/obsidian-shellcommands/issues/303)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was created.