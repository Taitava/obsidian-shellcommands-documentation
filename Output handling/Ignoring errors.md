# Ignoring errors
By default, the *Shell commands* plugin displays all error messages produced by shell commands in a notification balloon in the top right corner of the Obsidian window. Sometimes, however, error messages might be unimportant. SC provides you with two ways on how to ignore error messages on a per shell command basis.

## Ignore all error messages produced by a shell command
1. Read a guide about [[Output channels#How to select output channels for a shell command|how to select output channels for a shell command]].
2. Set the output channel of `stderr` to [[Output channel - Ignore|Ignore]].

**Note** that while this method is easy and simple to use, it might not be the best solution. If you encounter a regular error message that you want to suppress, this will do it, but it will also hide more infrequent error messages, that would be important to be seen. Consider using the below method instead, if possible.

## Ignore error messages based on a shell command's exit code

An exit code (aka error code) is used to identify error situations programmatically. It offers a simple way to ignore certain predefined failures, while letting unexpected failures still produce visible error messages. The exit code `0` usually means that there were no errors, but in practice you might still encounter some error messages raising up with exit code `0`.

1. Go to the plugin's settings panel.
2. Look for the shell command whose error messages you want to ignore, and click the *Stdout/stderr handling, Ignore errors* icon next to it:
  ![[Settings-main-click-output-channels-icon.png]]
  
3. An *extra options* modal opens up. In the modal, look for *Ignore error codes*. Type the exit code that you want to ignore. If you need to ignore multiple exit codes, you can separate them with commas `,`.
  ![[Settings-modal-output.png]]
	You can check which exit code you need to use by executing a shell command that fails and looking at the number in the brackets:
	![[Output-error-balloon.png]]
	
## History
- [0.8.0 - 2021-12-10](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#080---2021-12-10): Changed error code ignoring so that also error code 0 can be ignored. ([#107](https://github.com/Taitava/obsidian-shellcommands/issues/107)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): Added support for ignoring all error output regardless of error codes. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).
- [0.4.0 - 2021-09-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#040---2021-09-26): Added support for ignoring error codes that are greater than or equal to 1. ([#36](https://github.com/Taitava/obsidian-shellcommands/issues/36)).
