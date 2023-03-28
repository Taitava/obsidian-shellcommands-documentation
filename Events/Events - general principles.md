---
aliases:
  - Events
---
An obvious feature of the *Shell commands* plugin is the ability to execute shell commands from Obsidian's command palette, and via hotkeys. In addition to this, shell commands can also be executed automatically under certain circumstances - by using events.

For example, you can launch a set of applications [[Obsidian starts|every time you open Obsidian]], so you will have all the needed tool programs open when you start your day by working on a project. And when you are done for the day, you can [[watch cat videos on YouTube after closing Obsidian]].

## Enabling events
When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click the *Events* icon to open up an *extra options modal*:

![[Settings-modal-events.png]]

Here you'll find all the event's that you can enable for a shell command - pretty simple.

A couple of tips:
- Multiple events can be enabled for a single shell command, but note that if you use event related variables, you can only use them when the shell command is executed by an event that supports the variables. E.g. `{{event_folder_name}}` can only be used when a shell command is executed by [[Folder menu]] or [[File menu]] events. Otherwise an error message is shown and execution prevented.
- If you have a shell command that you don't need to execute manually - only via events - you can switch the *Availability in Obsidian's command palette* setting to *Excluded* to make your command palette a little bit less polluted. 😉 Note that if you use [[Shell commands URI]], the exclusion does **not** prevent using the URI to execute shell commands. ^exclude-from-command-palette

# All events
You can also access the event documentation pages via question mark icons in the event settings view.

## Miscellaneous events
- [[Obsidian starts]]
- [[Obsidian quits]]
- [[Switching the active pane]]
- [[Every n seconds]]
- [[File menu]]
- [[Folder menu]]
- [[Editor menu]]

## File and folder events
- [[File content modified]]
- [[File created]]
- [[File deleted]]
- [[File moved]]
- [[File renamed]]
- [[Folder created]]
- [[Folder deleted]]
- [[Folder moved]]
- [[Folder renamed]]

> [!Important] File/folder moves/renames done by external applications are seen as *deletions* and *creations*
> - When a file/folder is moved from one folder to another **by an external application**, Obsidian notices it as two separate events: a [[File deleted|deletion]] and a [[File created|creation]]. This is true even when the moving is done completely inside the vault.
> - The same happens also when a file/folder is renamed **by an external application**.
> - [[File moved|Moves]] and [[File renamed|renames]] are **detected more precisely when they are done in Obsidian**. ^file-folder-events-detection

## See which events are currently enabled
If you have forgotten which events you have enabled and for which shell commands, open up the settings modal and click the *Events* tab. You'll see a simple list of events and shell commands that use them.

Here you can also quickly disable all events, if needed, by switching *Enable events* off. Or otherwise, if you wonder why your events are not doing anything, remember to check that the toggle is turned on. It's on by default.

![[Settings-main-events-tab.png]]

# History
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26):
	- All events can now be disabled using a single toggle setting. ([#163](https://github.com/Taitava/obsidian-shellcommands/issues/163)).
	- Fixed a bug: Ghost shell commands were executed by events even after removal ([#165](https://github.com/Taitava/obsidian-shellcommands/issues/165))
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): First events became supported. ([#123](https://github.com/Taitava/obsidian-shellcommands/issues/123)).

> [!page-edit-history]- Page edit history: 2021-12-13 &#10132; 2022-05-11
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bcc0e63a8382fdbe8c42242d3df28cbc4fe63d18): Shorten event names.
> - [<small>2022-05-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5bbc04d5721f6b3723fd5baade2975a596e799dc): Events, part 2.
> - [<small>2022-04-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1435534a8ba1bc862237cd5c067b5c0ce07b35c4): Shell commands URI.
> - [<small>2022-04-09</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2d3e8929249fc0817a92b10ffe04b8b735d2cb97): 0.12.0: Default values for variables.
> - [<small>2022-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da3fab304cf1ecd9f7134fa969e4e6b3f8a9fa11): Add an example: Remember caret position when reopening Obsidian
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d6e852c88fb1ba221140841ea599189a27864a19): 0.11.0 is released.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e5463e54d3424913624f9ebc61fcc7f5dee829cb): 0.11.0 is released.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7537045e3408a0fa0a1f3b47a62907fc6e4f8ca3): Add annotations regarding 0.11.0-beta.1 test.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ce76d80247575b3d194500b2c0f8ee65dd7ce56b): Events: Added information about being able to enable/disable all events.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6355e7e9635c5baa1824e77337b48ecba4647c79): Events: Add 'See which events are currently enabled' section.
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f82d4d857c0acf39c4ffac3af84633e843e71d31): Events: General information.
> - [<small>2022-01-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99dc8c4717fc8b85fd34ab2c632e61d1d08f28af): Events: Add more information about different events.
> - [<small>2021-12-13</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/62392cb2d52bcf909cd8a5f56933ff07c5496e3b): WIP: A draft of Events documentation.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Events/Events%20-%20general%20principles.md).
> ^page-edit-history