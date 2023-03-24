---
cssclass: customiseTitle
---
# Variable: `{{output}}`
> [!Quote] {{output}} described in the *Shell commands* plugin's settings
> Gives text outputted by a shell command after it's executed.

This is used in [[Output wrappers|output wrappers]] when you want to surround output with some container text, e.g. code block. The variable is used to denote the place where a shell command's output text is wanted to be placed in a wrapper. Example of an output wrapper:
````
Shell command output, put into a code block:
```
{{output}}
```
````

# Availability
> [!Warning] Only available:
> In [[Output wrappers|output wrappers]], cannot be used as input for shell commands.

This variable can only be used for the *Content* field of [[Output wrappers|output wrappers]], and that field is the only place where the variable appears in [[Autocomplete|autocomplete menu]].

# History
- [0.16.0 - 2022-09-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0160---2022-09-25): The variable was born. ([#262](https://github.com/Taitava/obsidian-shellcommands/issues/262)).

> [!page-edit-history]- Page edit history: 2022-09-01 &#10132; 2022-09-25
> - [<small>2022-09-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1a6b6b5d9d7153a45d308923056a67a8737a2e6): 0.16.0 is released.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fd9edbf69c25863a39526cf3fe00077625f6a01d): Output wrappers.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Boutput%7D%7D.md).
> ^page-edit-history