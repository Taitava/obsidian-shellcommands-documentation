---
aliases:
  - Assign custom variables
cssclasses:
  - customiseTitle
---
# Output channel: Assign custom variables

> [!Info]
> _Assign custom variables_ is an advanced output handler aimed for situations where output from one shell command needs to be stored into [[Custom variables|custom variable(s)]] so that it can be fed to another shell command in a later phase. Think of it like first copying and then pasting text - but this time with unlimited slots that do not occupy your beloved clipboard!
>

> [!TLDR] Workflow between two separately executed shell commands
> ```mermaid
> flowchart LR
>     S1[Step 1] ~~~ A[Execute Shell command A] --> |"`{&quot;_myVariable1&quot;: &quot;Value 1&quot;,<br>&quot;_myVariable2&quot;: &quot;Value 2&quot;}<br>(JSON output from A)`"| A2(Assign custom variables)
>     A2 --> A3["{{_myVariable1}} = Value 1,\n{{_myVariable2}} = Value 2"]
>     S2[Step 2] ~~~ D["{{_myVariable1}}\n {{_myVariable2}}"] --> |"Value 1\nValue 2\n(Output from A passed to B)"| B(Execute Shell command B)
> ```

## Output must be formatted in JSON

> [!Quote]- JSON described on [json.org](https://www.json.org/json-en.html)
> **JSON** (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language Standard ECMA-262 3rd Edition - December 1999
> <small>(Cited on 2024-01-19)</small>

The primitive idea of the variable assignment format is that the output consists of a single JSON object, and each of its properties represent a [[Custom variables|custom variable]]'s name and an assignable value.

> [!Example] Output examples
> One variable assignment:
> ```
> {"_link_to_file": "My folder/My note.md"}
> ```
> 
> Multiple variable assignments:
> ```
> {
>     "_link_to_file": "My folder/My note.md",
>     "_link_alias": "Meeting notes"
> }
> ```

> [!Example] Shell command example
> This [[Bash]] command reads the size of a note file currently open in Obsidian (see [[{{file_path}}]]) and outputs the size to `stdout`.
> ```bash
> echo '{"_file_size": "'$(du -k {{file_path:absolute}} | cut -f1)' kB"}'
> # | cut -f1 removes the file path outputted by du.
> ```
> 
> Output:
> ```
> {"_file_size": "4 kB"}
> ```
> 
> This will turn into the [[Custom variables|custom variable]] `{{_file_size}}` having the value of `4 kB`.

> [!Tip]- JSON can be single line or multiline
> Padding the output with whitespace characters (spaces, tabs, newlines) does not affect interpreting the output. It's up to you if you prefer tight single-liners or sparse, easy to read multiline presentations.
> 
> > [!Success] Single line
> > ```
> > {"_link_to_file": "My folder/My note.md", "_link_alias": "Meeting notes"}
> > ```
> 
> > [!Success] Multiline
> > ```
> > {
> >     "_link_to_file": "My folder/My note.md",
> >     "_link_alias": "Meeting notes"
> > }
> > ```
> 
> If you use an external program or library to produce the JSON, it may add spacing by default for readability. On the other hand, single line outputs are easy to handcraft in a shell command without special tools:
> ```bash
> echo '{"_link_to_file": "My folder/My note.md", "_link_alias": "Meeting notes"}'
> ```

### Rules for custom variable names

- In the JSON object, custom variable names are presented with a preceding underscore `_` , but without curly braces `{{` and `}}` - just like in [[Shell commands URI#Pass values to your shell command via the URI using Custom variables custom variables|Shell commands URI]]. The property name is wrapped in double quotes `"` for it to comply with the JSON specification. For example, if the assignable custom variable would normally be referenced as `{{_link_to_file}}` in a shell command, here it will be `"_link_to_file"` .
- The same custom variable name should only be present once in the JSON object. If the object contains multiple properties with the same name, only the last one will be effective, and no warnings will be emitted.

### Rules for assignable values

- Currently, the values always need to be wrapped in double quotes `"` . In other words, only string (text) values are supported for now. Other value types (such as numbers) might be supported in the future, if a type system will be built for [[custom variables]].
- Possible line breaks must be presented as `\n` in a value. If a literal backslash `\` is wanted, it needs to be doubled: `\\` 

## Displaying the received values

By default, the SC plugin displays a notification balloon every time a [[Custom variables|custom variable]]'s value is changed via the _Assign custom variables_ output channel. [[Custom variables#How to disable notifications about value changes|The notifications can be disabled in settings]].

![[Custom variables#^value-change-example-notification]]

# Differences in *realtime* mode

If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output is handled exactly the same way as in [[Realtime output handling#Wait until finished|wait until finished]] mode, but just quicker.

> [!attention] Outputting in multiple phases must provide coherent JSON every time
> In case your shell command outputs content in multiple phases in the [[Realtime output handling|realtime]] mode, each output batch must form a **complete** JSON object.
> 
> For example, if your aim is to output two variable assignments like `{"_variable1": "value 1", "_variable2": "value 2"}`, you can optionally split them into two batches:
> > [!Success] Correct
> >- First batch: `{"_variable1": "value 1"}` 
> >- Second batch in a later phase: `{"_variable2": "value 2"}`
> 
> You cannot split the JSON object in between:
> > [!Failure] Incorrect
> > - First batch: `{"_variable1": "value 1",`
> > - Second batch in a later phase: `"_variable2": "value 2"}`.
> > 
> > This would cause JSON syntax errors to be shown in a notification balloon.
> 
> Then again, if the [[Realtime output handling#Wait until finished|wait until finished]] mode is used, the shell command must output only a single JSON object. Of course, that object can contain multiple custom variable assignments.

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The output channel was released. ([#382](https://github.com/Taitava/obsidian-shellcommands/issues/382)).