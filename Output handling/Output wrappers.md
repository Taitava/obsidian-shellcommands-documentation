> [!summary]
> Output wrappers are text snippets that can be used to surround text outputted by shell commands. For example, when [[Output channel - Current file|inserting output to current note]], put it in a [code block](https://help.obsidian.md/How+to/Format+your+notes#Code+blocks). Benefits:
>  - Multiple shell commands can use the same output wrapper. No need to repeat the same wrapper text over and over again in the settings.
>  - Shell commands can be kept cleaner when they do not need to contain excessive `echo` commands in addition to their actual core logic.
>  - The same [[Variables - general principles|{{variables}}]] that are used in shell commands can also be used in output wrappers.

> [!info]
> Output wrappers are not always needed. If you are new to this plugin, you probably do not need to learn to use output wrappers now.

# Creating output wrappers
Output wrappers can be created in two ways:
- [[#Create an output wrapper from a shell command's settings modal|From the *Output* tab in a shell command's settings modal]].
- [[#Create an output wrapper from the main settings view|From the *Output* tab in the main settings view]].

## Create an output wrapper from a shell command's settings modal
1. When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click the *Output* icon to open up an *extra options modal*:
![[Settings-main-click-output-channels-icon.png]]
2. In the modal, select *Create a new output wrapper* for `stdout` or `stderr`:
![[Settings-modal-output-new-output-wrapper.png]]
3. Another modal with a new output wrapper's settings opens up. Continue reading from [[#Configuring an output wrapper's settings]].

## Create an output wrapper from the main settings view
1. Open [[How to define shell commands#^shell-command-controls|the settings]] and the *Output* tab:
![[Settings-main-output-tab.png]]
2. Click the *New output wrapper* button.
3. Another modal with a new output wrapper's settings opens up.

After you finish setting up the output wrapper, you'll need to go to some shell command's settings and select the output wrapper you created in order to use it. Follow the instructions in [[#Create an output wrapper from a shell command's settings modal]] to see how to pick a prompt for a shell command.

## Configuring an output wrapper
![[Settings-output-wrapper.png]]

Fill in the following information:
 - *Output wrapper title*: A name for the wrapper so that you will recognise it in the settings.
 - *Content*: This is the actual wrapper text that will be used as a "container" for text outputted from shell commands. Use the [[{{output}}]] variable to indicate where in the wrapper you will want shell command output to be placed. Other [[Variables - general principles|{{variables}}]] can be used, too.

# Examples

> [!Example] Fenced code block output wrapper
> This wrapper simply surrounds output with three backticks ` ``` ` :
> ````
> ```
> {{output}}
> ```
> ````

> [!Example] Add date and time of execution
> ```
> Executed on: {{date:YYYY-MM-DD HH:mm:ss}}
> Results:
> {{output}}
> ```

# Special cases

## Combining `stdout` and `stderr` wrapping
The *Shell commands* plugin allows to define output wrappers separately for `stdout` and `stderr`. If a shell command emits both `stdout` and `stderr` outputs, the outputs *might* be combined, based on the following rules:
- Does `stdout` and `stderr` have the same [[Output channels|output channel]]?
  - If the output **channels** are **the same**:
    - `stdout` and `stderr` outputs will be combined in an order specified by the *[[Output channels#How to select output channels for a shell command|Order of stdout/stderr output]]* setting.
    - Does `stdout` and `stderr` have the same output wrapper?
      - If the output **wrappers** are **the same**:
        - The combined `stdout` and `stderr` outputs will be wrapped in a **single output wrapper**.
      - If the output **wrappers** are **not the same**:
        - `stdout` and `stderr` outputs will be wrapped separately, and combined after the wrapping.
  - If the output **channels** are **not the same**:
    - `stdout` and `stderr` outputs will be handled separately, no combining will be done (regardless if they use the same wrapper or not).
> [!TLDR] TL;DR
> If the combining rules are not easy to understand, you can just skip the topic. Wrapper combining is a special case feature, and it's best learned when using output wrappers in practice.

## Duplicating output text
`{{output}}` can be presented multiple times in an output wrapper. This makes it possible to repeat output without executing a shell command multiple times.

## Discarding output
If `{{output}}` is not present in an output wrapper, then the wrapper text will completely replace the output, discarding it.

# History

- #TODO: Add a date [0.16.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The ability to define output wrappers was born. ([#262](https://github.com/Taitava/obsidian-shellcommands/issues/262)).