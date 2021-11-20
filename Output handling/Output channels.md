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
All output channels are available to both `stdout` and `stderr`.
1. Go to the plugin's settings panel.
2. Look for the shell command whose output channels you want to change, and click the *Stdout/stderr handling, Ignore errors* icon next to it:
  ![[Settings-main-click-output-channels-icon.png]]
  
3. An *extra options modal* opens up. In the modal, look for *Output channel for stdout* and *Output channel for stderr*. You'll find dropdown menus that allow you to change the channels:
  ![[Settings-modal-output.png]]

## All output channels
### Ignore
Simply hides the output, doing nothing with it. This is the default for all commands' `stdout` output, because for many commands, the normal output is not so important. E.g. when creating a folder, launching an application or modifying a file - in these cases, the lack of error messages is usually enough to tell that the command executed successfully.
 
 ### Notification/Error balloon
 
 A temporary message balloon that pops up in the top right corner of the Obsidian window. This is the default for all commands' `stderr` output.
 
 ![[Output-notification-and-error-balloons.png]]
 You can identify an *error balloon* by the brackets `[` `]` preceding the output message. The brackets indicate the exit code (aka error number) that the shell command returned at the end, e.g. *0* in the image above. A *notification balloon* does not have the brackets nor an exit code.
 
 **Good for**: Short output that can be discarded after a short period of time. Suits for  a small amount of multi line output, too.
 
 You can customize for how long *notification balloons* and *error balloons* are visible in the plugin's settings panel (in *Output* tab):
 ![[Settings-main-output-tab.png]]
 
  ### Status bar
 Outputs text to the bottom of the Obsidian window. The last line of the output is visible permanently. If the output contains multiple lines, you can hover the status bar with mouse to see all of the outputted lines.
 
 **Good for:** Output that is wanted to be easily visible for a longer time, and that usually needs just one line.
 
 The text is visible until another shell command execution outputs text to the status bar, replacing the old text. **Note that if the new execution produces empty text output, the old text will not be removed**, because empty text is considered to be "no output at all", so it's not processed. This might change in the future.
 
 ![[Output-status-bar.png]]
 
 The position and available space of the status bar output element depends on how many other things have inserted content in the status bar (e.g. other plugins). The *Shell commands* plugin will never replace or remove other content in the status bar.
 
 ### Current file: top/bottom/caret position
 Output will be inserted to the file that is currently open and active in Obsidian. If no file is active (e.g. you have Graph view active instead of a file), the output will be shown in a message balloon.
 
 If *caret position* is used, then the output can replace text if you have something selected. 
 
 ### Clipboard
Output will be copied to the clipboard as text.

In addition, the output will be shown in a notification balloon, so that you can see what was copied to the clipboard. This can be disabled in the plugin's settings panel (in *Output* tab):
![[Settings-main-output-tab.png]]