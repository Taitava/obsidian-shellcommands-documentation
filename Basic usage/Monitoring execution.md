# Monitoring execution

Usually, shell commands are quick to run, and it's only interesting to get a notification about their output. However, some shell commands might take a longer time to process, in which case it can be nice to be able to see that a shell command is under execution. You can turn on a notification balloon for this in settings. It will look like this:

![[Execution-notification-balloon.png]]

> [!Tip] Terminate long-running shell commands
> If you need to terminate a shell command's process before it's finished, just click the stop icon in the notification balloon (marked with an arrow in the image). This sends a `SIGTERM` signal to the process.


## Enable notifications when executing shell commands

1. Open up the _Shell commands_ settings modal and click on the _Output_ tab:
![[Settings-main-output-tab.png]]
2. Click on the dropdown menu at _Show a notification when executing shell commands_. Choose from the following options:
> [!Summary] Execution notification options
> - _Do not show_ (default): No notification will be shown while a shell command is executing. However, a notification might be shown after the execution, if the shell command is defined to show its output in a [[Output channel - Notification balloon|notification balloon]].
> - _Show for n seconds_: Shows a notification every time. The duration is the same as defined in _Notification message duration_.
> - _Show until the process is finished_: Shows the notification every time, and keeps it visible for as long as the shell command runs. This is handy if you have long-running shell commands without any visible output, and you want to keep an eye out on if they are still running or not. If you execute quickly running shell commands, the notification will just show up and disappear immediately.
> - _Show only if executing takes long_: Same as _Show until the process is finished_, but waits for two seconds after starting the execution. If the shell command is still running after two seconds, the notification is displayed.

> [!info] The setting affects all shell commands
> [There is no ability for defining the setting on a per shell command basis, but such feature is planned for the future](https://github.com/Taitava/obsidian-shellcommands/discussions/260#discussioncomment-3926382).


# History
- #TODO: Add a date [0.17.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): Added an ability to terminate processes by clicking an icon. ([#289](https://github.com/Taitava/obsidian-shellcommands/issues/289)).
- [0.16.0 - 2022-09-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0160---2022-09-25): Created the ability to show notifications about a shell command being executed. ([#261](https://github.com/Taitava/obsidian-shellcommands/issues/261)).
	- This documentation page was created later, on 2022-11-26.