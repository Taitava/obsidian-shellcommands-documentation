# Output channels

Output channels specify what to do with text that your shell commands return to Obsidian after their execution. You can define specific output channels for each of your shell commands. For example, one shell command's output may be channeled to the file that is currently open in Obsidian, and another shell command's output may be channeled to the clipboard. Output can also be discarded (ignored).

## Two different *output streams*
In general, shells support multiple different [output streams](https://en.wikipedia.org/wiki/Standard_streams). The general idea is to be able to separate different kinds of outputs from each other. The *Shell commands* plugin supports the two most common output streams:
- `stdout`: *Standard output*; for normal, expected output text from a command.
- `stderr`: *Standard error*; for exceptional messages indicating that the command has failed (either completely or just partly).

The *Shell commands* plugin allows you to define different output channels for each of these output streams. This way you can specify e.g. that a shell command's normal, expected output will be channeled to the clipboard, but error messages - if any - will be shown in a notification balloon instead.

(Note that a shell command is able to produce both `stdout` and `stderr` type of outputs at the same time, for example in a situation where you use a single command to process multiple files, and one of the files fails to process and produces output to `stderr`, while others produce output to `stdout`.)

While shells do support also other output streams than the `stdout` and `stderr`, the *Shell commands* plugin does not support custom output streams at the moment. This kind of support might be added in the future, although no decisions have been made.

## How to select output channels for a shell command
1. Go to the plugin's settings panel.
2. Look for the shell command whose output channels you want to change, and click the *Stdout/stderr handling, Ignore errors* icon next to it:
  ![[Settings-main-click-output-channels-icon.png]]
  
3. An *extra options modal* opens up. In the modal, look for *Output channel for stdout* and *Output channel for stderr*. You'll find dropdown menus that allow you to change the channels:
  ![[Settings-modal-output.png]]
Some output channels are available to both `stdout` and `stderr`. There are some channels that are not available for `stderr`, such as [[Output channel - Open files|Open files]].

## Realtime output handling
> [!quote]
> By default, the *Shell commands* plugin **waits till the end of execution** before it reads any output. This is fine for many cases, but if you are executing something that takes a long time to finish, you may opt for [[realtime output handling]].

## All output channels
- [[Output channel - Ignore|Ignore]]
- [[Output channel - Status bar]]
- [[Output channel - Notification balloon|Notification/Error balloon]]
- [[Output channel - Current file]]
- [[Output channel - Clipboard]]
- [[Output channel - Ask after execution]]
- [[Output channel - Open files]]