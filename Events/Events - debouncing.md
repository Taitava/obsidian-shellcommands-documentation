---
aliases:
  - Event debouncing
---

> [!Warning] This feature is only available in a beta test
> - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/391).
> %% #TODO: Remove this annotation when the final version is released. %%

> [!Info] About debouncing
> Certain events may trigger a shell command's execution so often that it's desirable to limit how often events can execute the shell command. This is called [_debouncing_](http://unscriptable.com/2009/03/20/debouncing-javascript-methods/).
> - Debouncing prevents certain events from starting a shell command's execution if the command is already executing, is about to be executed, or has finished executing a short time ago. A _cooldown_ time is used to define for how long subsequent executions are prevented before or after a shell command's execution.
> - Debouncing is configured on a shell command basis. Different shell commands have different timings and different debouncing modes, and they are executed independently of each other's debouncing. I.e. Executing one debounced shell command does not prevent a different shell command from being executed, only the same shell command's execution is limited by debouncing.
> ^about-debouncing

## Enable debouncing for a shell command

1. When you have [[How to define shell commands|created a shell command]] and are looking at it [[How to define shell commands#^shell-command-controls|in the settings]], click on the *Events* icon to open up an *extra options modal*:
    ![[Settings-modal-events-debouncing.png]]

2. Look for the _Debouncing_ setting near the top of the modal, and select whether to execute **before** and/or **after** a *cooldown* phase. [[#Different debouncing modes|Information about different modes]].
3. Define a _Cooldown duration_ in seconds.
    - One decimal is allowed, e.g. `0.1` would be `100` milliseconds, and `1.1` would be `1100` milliseconds. 

## Cooldown duration
> [!Info] _Cooldown duration_ prevents subsequent executions from happening too close to each other
> _Cooldown_ is a phase in the debouncing process, during which a shell command either:
> - has just finished executing, **or**
> - is waiting for a delayed execution,
> depending on the [[#Different debouncing modes|debouncing mode]].
> 
>During a cooldown phase, the shell command is **not** executing, and **events are guarded not to start executing** it.
>- One shell command's cooldown phase does not prevent other shell commands from being executed. 
>- Similarly to the cooldown phase, when a debounce-enabled shell command (triggered by any non-menu event) is **executing** and has not finished, further executions of the same shell command are prevented or postponed.

> [!Tldr] Total duration of a phase during which simultaneous executions are prevented
> $$
> Shell\;command\;execution\;duration + Cooldown\;duration = Debounce\;total\;duration\;
> $$

## Different debouncing modes

There are different modes for deciding in which order shell command _execution_ and _cooldown_ should happen, each having their own ideal use cases.

> [!Summary] Debouncing modes in a nutshell
>
> | Mode | 1. Before cooldown | 2. During cooldown | 3. After cooldown |
> | ---- | ---- | ---- | ---- |
> | [[#Mode Execute before cooldown\|Execute before cooldown]] | Execute the shell command.<br>Discard subsequent executions. | After execution:<br>Discard subsequent executions. | Allow execution again. |
> | [[#Mode Execute after cooldown\|Execute after cooldown]] | - | Delay execution.<br>Discard subsequent executions. | Execute the shell command.<br>Subsequent events during execution will be postponed to start another cooldown + execution process afterward. |
> | [[#Mode Execute before and after cooldown\|Execute before and after cooldown]] | Execute the shell command.<br>Postpone subsequent executions. | After execution:<br>Postpone subsequent executions. | If an event triggered again during phases 1 or 2, execute the shell command again.<br>Otherwise, second execution is not needed. If a second execution is performed, apply another cooldown phase after it, then execute again if needed, etc. |

### Mode: Execute before cooldown

> [!Quote] From the *Shell commands* plugin's settings:
> When executing <em>Before cooldown</em>, the shell command is executed right-away, and <strong>subsequent executions are prevented</strong> for as long as the execution is in progress, <strong>plus</strong> the <em>Cooldown duration</em> after the execution.

This mode is suitable in situations where something needs to be updated occasionally, but where it's not important to get the latest information.

> [!Success] Ideal use case for _Execute immediately, then cooldown_
> #TODO: Add a use case.

### Mode: Execute after cooldown

> [!Quote] From the *Shell commands* plugin's settings:
> When executing <em>After cooldown</em>, the shell command execution will be delayed by the <em>Cooldown duration</em>. <strong>Subsequent executions are prevented</strong> during the cooldown phase, or <strong>postponed</strong> during the execution phase.

> [!Success] Ideal use case for _Cooldown first, then execute_
> Committing changed files automatically to a version control system (such as [Git](https://git-scm.com)) is reasonable to be debounced so that the first occurrence of e.g. [[File content modified]] event does **not immediately** create a commit. Instead, it should start a waiting phase (cooldown) lasting for example 30 seconds. Otherwise, mass-editing multiple files (e.g. by renaming note files that have backlinks in other files), or editing a single file multiple times, could cause multiple commits to be made, if [[#Mode Execute before cooldown]] or [[#Mode Execute before and after cooldown]] were used instead. So, [[#Mode Execute after cooldown|Execute after cooldown]] is a better choice here.
> 
> [Real-life use case on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/319#discussion-4762076)

> [!Warning] Exiting Obsidian cancels delayed executions
> Please note that postponed executions will not be carried out, if Obsidian quits before they are launched. [If you wish the plugin to trigger pending executions when Obsidian quits, please start a new _Idea_ discussion on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas)

### Mode: Execute before and after cooldown

> [!Quote] From the *Shell commands* plugin's settings:
> When executing both <em>Before and After cooldown</em>, the shell command is executed right-away, and <strong>subsequent executions are postponed</strong> for as long as the execution is in progress, <strong>plus</strong> the <em>Cooldown duration</em> after the execution. After the cooldown period ends, the shell command is possibly re-executed, if any subsequent executions were postponed.

This mode is suitable for situations where no harm is caused by executing a shell command twice in a short time (with a pause in-between), but where it's still reasonable to debounce execution occurrences to as few as possible.

> [!Success] Ideal use case for _Execute, cooldown, execute again if needed_
> When implementing a [Git lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) like ability to see the latest change of the current line, one can use the (still under development) event [[Caret moved in editor]]. As the caret can move multiple times in a short period of time, debouncing is recommended, and this mode provides the best of both worlds for this use case:
> - it reacts immediately to the first occurrence of caret movement, and
> - it makes sure that if the caret keeps moving, the last occurrence (where caret moves the last time) will still get caught on and executed.
>  
> As this use case is about **reading** information, and **not writing** it, it does not cause any permanent side effects to perform the execution twice (if needed) instead of once.
> 
> [Real-life use case on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/284#discussioncomment-4221577)

## Debouncing only affects events, not other means of executing shell commands

> [!Success] Events affected by debouncing
> 
> | Event                                                                                                                                                                                                                 | Reason for debouncing |
> |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ----------------------- |
> | [[Every n seconds]]                                                                                                                                                                                                   | Having this event enabled together with an other event could otherwise cause simultaneous executing. |
> | [[File content modified]]                                                                                                                                                                                             | Content might be edited repeatedly in a short time. |
> | [[File created]] / [[File deleted]] / [[File moved]] / [[File renamed]]<br>[[Folder created]] / [[Folder deleted]] / [[Folder moved]] / [[Folder renamed]] | External programs can modify large amounts of files in a single batch. |
> | [[Obsidian starts]] / [[Obsidian quits]]                                                                                                                                                                              | Having this event enabled together with an other event could otherwise cause simultaneous executing. |
> | [[Switching the active pane]]                                                                                                                                                                                         | User might focus different panes rapidly. |

> [!Failure] Debouncing does not affect
> - executing shell commands manually via [Obsidian's command palette](https://help.obsidian.md/Plugins/Command+palette) or hotkeys,
> - executing shell commands via [[Shell commands URI]], nor
> - menu events: [[Editor menu]], [[File menu]], [[Folder menu]], because their execution is always expected.
> 
> Note that if a shell command is executed by any of the means listed above, those executions are not seen by the debouncing mechanism, and so they will not prevent any event from performing a simultaneous execution. [If you wish this to be changed, please start a new _Idea_ discussion on GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas).

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2024--): Support for debouncing was released. ([#380](https://github.com/Taitava/obsidian-shellcommands/issues/380)).


> [!page-edit-history]- Page edit history: 2024-01-14 &#10132; 2024-01-20
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1399ca5f52956bd6ba2b3202720d6422f270c088): Rename [[Caret moved in editor.md]] to [[Caret moves in editor.md]].
> - [<small>2024-01-14</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e854c7f77ae93e038265401a766595f870feac47): First version of [[Events - debouncing.md]].
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Events/Events%20-%20debouncing.md).
> ^page-edit-history