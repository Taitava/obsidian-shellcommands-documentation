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
- [[Output channel - Ask after execution|Ask after execution]]
- [[Output channel - Clipboard|Clipboard]]
- [[Output channel - Current file|Current file]]
- [[Output channel - Ignore|Ignore]]
- [[Output channel - Notification balloon|Notification/Error balloon]]
- [[Output channel - Open files|Open files]]
- [[Output channel - Status bar|Status bar]]

# History


> [!page-edit-history]- Page edit history: 2021-10-31 &#10132; 2022-12-11
> - [<small>2022-12-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/97879fc6f02642444d1a61eee52f83b35a0ef86d): Output channels: Mention that some output channels are only available on `stdout`.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2022-08-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c6f5146f8f90047f63fd90bfbe81f024d6513ea): Rename Output channel "Open a file" to "Open files".
> - [<small>2022-02-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/10927a104173795814a93a66febebdf536563faa): Output channels: 'Open a file defined in the output' renamed to 'Open a file'.
> - [<small>2022-02-17</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/de08ed9e9c01e8c184e498473dafc44cad9eb0e0): Output channel: Open a file defined in the output.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1a84fe59a57f760fa9773a70cf41693982d571ef): #134: Output channel - Modal: Change the title to "Output channel - Ask after execution".
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/88f88ce46a22a9a7ae4ce3f93727dca1ed8b97bd): Output channel: Modal.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e98d750bc24d867629c6de1fa5019c31b6e87f49): Exract output channels to separate files.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49f6a5aa991b118b0193538cb111300aca91dc96): Improve some links.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a0b2ca18f74c8ece9499165e26bda7750e6945cd): Output channels.
> - [<small>2021-10-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2dd3261379bc2817e7ea01b96872402ad7c3c4d1): Some quick plans for the documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channels.md).
> ^page-edit-history