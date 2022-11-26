---
aliases:
 - "Realtime mode"
---

# Realtime output handling

> [!info]
> By default, the *Shell commands* plugin **waits till the end of execution** before it reads any output. This is fine for many cases, but if you are executing something that takes a long time to finish, you may opt for realtime output handling. <!-- If you change this paragraph, change it in Output channels.md, too! -->

## Two *output handling modes*

For each shell command, you can choose between these modes:
 - *Wait until finished*: Output from a shell command is passed to the chosen [[Output channels|output channel]] **after** the shell command has finished its execution and all output text has been gathered. This has traditionally been the only way to handle output in SC until version `0.17.0`.
 - *Realtime*: Output is read actively as soon as a shell command starts emitting any. Output will likely appear one part at a time, and certain actions (e.g. [[Output wrappers|output wrapping]], if used) are done repeatedly for each outputted part.

Some output channels behave a bit differently in *realtime* mode than in *wait* mode.

## Which output handling mode should I choose?

### Wait until finished
> [!check] Good for:
> - Shell commands that execute quickly.
> 	- Or: Long-running shell commands, but you only want to see the output once it's all complete.
> - If you need to [[Ignoring errors#Ignore error messages based on a shell command's exit code|ignore certain errors by exit code]].
> - If you are using [[output wrappers]] and want to avoid **repeated** wrapping.
> - If you are using [[Output channel - Current file|Current file: top]] and want to avoid **reversed** output order.
> - If you are uncertain, try this first.

> [!fail] Not for:
>  - If you need to receive `stdout` **and** `stderr` output in their original order. *Wait until finished* will handle these different output streams in an order specified in a shell command's settings, but it cannot *mix* the two streams together, like can be done in *realtime* mode. That being said, [[#Order between `stdout` and `stderr` cannot be guaranteed.|realtime mode also has some problems maintaining order between the two streams]], but at least it's better at it.

### Realtime
> [!check] Good for:
> - Long-running commands if you want to see at which phase they are in.
> - If you want `stderr` output to mix naturally together with `stdout`.
> - If you are using [[Output channel - Ask after execution|Ask after execution]] and want to manually edit the output text **while part of the output is still incoming**.
> - Any kinds of [daemons](https://en.wikipedia.org/wiki/Daemon_(computing)) that are designed to execute constantly.

> [!fail] Not for:
>  - [[Ignoring errors#Ignore error messages based on a shell command's exit code|Ignoring certain errors by exit code]]. As an *exit code* is only received after a shell command finishes execution, it's unavailable at the time of `stderr` error message handling in *realtime* mode. But you can still [[Ignoring errors#Ignore all error messages produced by a shell command|ignore all stderr output completely]].

## How to change the output handling mode?

1. Go to the plugin's settings panel.
2. Look for the shell command whose output handling mode you want to change, and click the *Stdout/stderr handling, Ignore errors* icon next to it:
  ![[Settings-main-click-output-channels-icon.png]]
  
3. An *extra options modal* opens up. In the modal, look for *Output handling mode*:
	![[Settings-modal-output-handling-mode.png]]
 
4. Select the mode you want. It will be used the next time the shell command is executed, regardless of how the execution happens: manually from Obsidian's command palette (or hotkeys), via [[Events - general principles|events]], or via [[Shell commands URI]].


# Output channel specific differences when going realtime

![[Output channel - Ask after execution#^differences-in-realtime]]

![[Output channel - Clipboard#^differences-in-realtime]]

![[Output channel - Current file#^differences-in-realtime]]

![[Output channel - Ignore#^differences-in-realtime]]

![[Output channel - Notification balloon#^differences-in-realtime]]

![[Output channel - Open files#^differences-in-realtime]]

![[Output channel - Status bar#^differences-in-realtime]]


# Order between `stdout` and `stderr` cannot be guaranteed.

If your shell command outputs both `stdout` and `stderr` output, the order in which they are handled by the *Shell commands* plugin may vary.

> [!example] Example on Windows PowerShell
> Imagine that the following shell command would output both `stdout` and `stderr` into the current file at caret position:
> ```
> echo stdout line 1
> [Console]::Error.WriteLine("stderr line1")
> [Console]::Error.WriteLine("stderr line2")
> echo stdout line 2
> echo stdout line3
> echo stdout line4
> echo stdout line5
> ```
> You could expect that *stderr line1* and *stderr line2* would be inserted to the current note **after** *stdout line1* and **before** *stdout line2*. However, sometimes *stdout line2* is received before *stderr line1*, or even before *stderr line 2*.

The order in which `stdout` and `stderr` output messages are received may vary from time to time. You might often see the output coming just fine in the correct order, even if not every time. If your use case **requires** that `stdout` and `stderr` **must** always keep their original order, I recommend you to consider directing all `stderr` output to `stdout`, so you'll have all output in `stdout`. A single output stream's content should always arrive in the same order to this plugin.

> [!bug]- Probably cannot be fixed
> Unfortunately, according to the following sources, there seem to be no solutions to this problem:
>  - https://github.com/nodejs/node/issues/26516
>  - https://stackoverflow.com/questions/57046930/node-js-spawn-keep-stdout-and-stderr-in-the-original-order
> 
> In case you do have some tips about how a correct order could be achieved, please post your ideas in the following GitHub discussion: https://github.com/Taitava/obsidian-shellcommands/discussions/64#discussioncomment-4063498

# If you suspect bugs in output handling

Whether you are using the *realtime* mode or the traditional *wait* mode, if you encounter odd behavior in the way the *Shell commands* plugin handles **the output content**, you may try if the same problem occurs if you switch to use the other mode.

The shell command execution process is partly the same and partly different between the *wait* and *realtime* modes:
> [!info] Process parts
> > [!check] Same process parts:
> > 1. [[Variables - general principles|{{variable}}]] parsing and other actions that happen before the actual execution of a shell command happen similarly regardless of the output handling mode.
> > 2. The actual execution starting process is also the same.
> 
> > [!warning] Differing process parts
> > 3. When output is received, different modes *handle* the output via different routes.
> > 4. Even though output will be handled by the same [[output channels]], the channels themselves behave a bit differently in different modes.

If you are reporting suspected bugs in output handling, you can [create a new discussion in the *Debugging and testing* category in the *Shell commands* plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/debugging-and-testing). You can mention the following things:
- What is the actual problem?
- Are you using the *wait* mode or the *realtime* mode?
- If you tried both modes, did the problem occur on both of them, or only one of them?

# History

- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26): The possibility to handle output in _realtime_ mode was born. Before this, only the _Wait until finished_ mode was available. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).