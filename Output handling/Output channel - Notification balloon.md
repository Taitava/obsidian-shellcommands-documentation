---
aliases:
  - "Notification balloon"
  - "Error balloon"
---

# Output channel: Notification/Error balloon
 
  A temporary message balloon that pops up in the top right corner of the Obsidian window. This is the default for all commands' `stderr` output.
 
 ![[Output-notification-and-error-balloons.png]]
 You can identify an *error balloon* by the brackets `[` `]` preceding the output message. The brackets indicate the exit code (aka error number) that the shell command returned at the end, e.g. *0* in the image above. A *notification balloon* does not have the brackets nor an exit code.
 
 **Good for**: Short output that can be discarded after a short period of time. Suits for  a small amount of multi line output, too.
 
 You can customize for how long *notification balloons* and *error balloons* are visible in the plugin's settings panel (in *Output* tab):
 ![[Settings-main-output-tab.png]]

# Differences in *realtime* mode  
  
If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.  
  
> [!tldr] _Notification balloon_ - realtime mode differences:
> - Output is tried to be inserted into a single notification balloon, meaning that when new output is received, it's added to an existing notification.
> - If a previous notification balloon was already closed, a new balloon is created, and it will contain **all** output content, not only new content.
> - If both `stdout` and `stderr` are directed to a notification/error balloon, they will share the same balloon in *realtime* mode. This is for trying to keep both of these outputs in the same order they have appeared in. It may cause confusion if you need to know explicitly if certain output came via `stdout` or `stderr`. As a comparison, when in *wait* mode, notification/error balloon will create separate balloons for `stdout` and `stderr`.
> - A stop icon can be clicked to terminate execution before it's finished:
>   ![[Icon-Terminate-execution-Notification-balloon.png]]
>   (Sends a `SIGTERM` signal to the process.)
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26):
	- The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
	- Added a button for terminating long-running shell commands - only appears in realtime mode. ([#289](https://github.com/Taitava/obsidian-shellcommands/issues/289)).
- [0.5.1 - 2021-10-09](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#051---2021-10-09): Error balloon: Fixed exit code being sometimes null. ([#67](https://github.com/Taitava/obsidian-shellcommands/issues/67)).
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel was created. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).