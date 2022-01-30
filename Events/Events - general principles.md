# Events - general principles
==This feature is currently only available in [0.10.0 BETA TEST](https://github.com/Taitava/obsidian-shellcommands/discussions/138)! #TODO: Remove this text when the beta is over.==

An obvious feature of the *Shell commands* plugin is the ability to execute shell commands from Obsidian's command palette, and via hotkeys. In addition to this, shell commands can also be executed automatically under certain circumstances - by using events.

For example, you can launch a set of applications [[After Obsidian starts|every time you open Obsidian]], so you will have all the needed tool programs open when you start your day by working on a project. And when you are done for the day, you can [[watch cat videos on YouTube after closing Obsidian]].

## Enabling events
When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click the *Events* icon to open up an *extra options modal*:

![[Settings-modal-events.png]]

Here you'll find all the event's that you can enable for a shell command - pretty simple.

A couple of tips:
- Multiple events can be enabled for a single shell command, but note that if you use event related variables, you can only use them when the shell command is executed by an event that supports the variables. E.g. `{{event_folder_name}}` can only be used when a shell command is executed by [[Folder menu]] or [[File menu]] events. Otherwise an error message is shown and execution prevented.
- If you have a shell command that you don't need to execute manually - only via events - you can switch the *Availability in Obsidian's command palette* setting to *Excluded* to make your command palette a little bit less polluted. 😉

# All events
You can also access the event documentation pages via question mark icons in the event settings view.
- [[After Obsidian starts]]
- [[After switching the active pane]]
- [[Before Obsidian quits]]
- [[Editor menu]]
- [[Every n seconds]]
- [[File menu]]
- [[Folder menu]]

## See which events are currently enabled
If you have forgotten which events you have enabled and for which shell commands, open up the settings modal and click the *Events* tab. You'll see a simple list of events and shell commands that use them:

![[Settings-main-events-tab.png]]

# History
- #TODO: Add date. [0.10.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): First events became supported. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).