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
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): The variable is now only available when something is selected, otherwise it shows an error message. ([#303](https://github.com/Taitava/obsidian-shellcommands/issues/303)).
- [0.1.0 - 2021-08-29](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#010---2021-08-29): The variable was released.

> [!page-edit-history]- Page edit history: 2021-11-19 &#10132; 2023-01-06
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2022-12-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/64b4d473ddcac9653d1613b9823033d861c4cae8): {{selection}} now displays an error if nothing is selected.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/98766d51b7baefbc75e4c6911d79991a9ee294fb): {{selection}}: Add a note about wanting to support 'Reading' mode.
> - [<small>2022-08-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a1bc8cac4a5ba12608ef30eabfcbb616a69710bd): Variables: Use callouts for all Availability sections.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b3e7de3816f3d1b8675616f41e6fc4b8fe66e740): Variables: Updated description layouts.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e4c431cdcbfcff0c95963613c9466171a38e90dd): Variables: Add 'See also' sections with links to other variables.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8610b6660a05e99d0cc0531db30ffde0bfc2fe8e): Variables: Add availability information.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62b9ff92e6c0ed82fb8d617b8644ba062cafa25a): Variables: add version history.
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17cb062fae9850024325871b93694d81e5d67fa3): Documentation for each variable.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3e5e64ba07d1979852b3f75f53ed3d1480ffdb09): Documentation for each variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bselection%7D%7D.md).
> ^page-edit-history