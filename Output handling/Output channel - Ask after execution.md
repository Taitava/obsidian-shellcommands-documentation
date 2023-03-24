---
aliases:
 - "Ask after execution"
cssclass: customiseTitle
---

---
# Output channel: Ask after execution
This channel creates a modal window that displays output from a shell command.
- Output can be manually redirected (=applied) to [[Output channels|other output channels]], even to multiple channels at once. Output can be discarded just by closing the modal.
- Output can be manually edited before the redirection, to do cleanup etc. The field is resizable.
- If you select text before clicking any of the redirection buttons, you can only use the selected part of the output text.
- If both `stdout` and `stderr` streams are channeled to the modal, it will display two output fields and two redirection control rows.
- If output is empty, no modal is shown.
- Displays the executed shell command's [[exit code]]. It's usually zero if the command succeeded.

**Good for:** Long output that takes time to read through.

![[Output-modal.png]]

## Hotkeys
- Each redirection button has a keyboard hotkey: `Ctrl`/`Cmd` + a letter. 
- Hitting `Ctrl`/`Cmd` + `Shift` + a letter closes the modal in addition to redirecting.
- `Ctrl`/`Cmd` + clicking a button does the same, redirects output and closes the modal.
- Hover over each redirection button with mouse to see its hotkey letter.

# Differences in *realtime* mode

If you define your shell command's [[Realtime output handling|output to be handled in realtime mode]], the output might show up a bit differently than in [[Realtime output handling#Wait until finished|wait until finished]] mode.

> [!tldr] _Ask after execution_ - realtime mode differences:
> - You can edit early outputted text even when not all the output has been received. New output will go automatically to the bottom of the output textarea, regardless of your caret position.
> - *Exit code* will only show up after the shell command finishes execution. Before that, an *Executing...* text indicates that the process is still running. 
> - A stop icon can be clicked to terminate execution before it's finished:
>   ![[Icon-Terminate-execution-Ask-after-execution.png]]
>   (Sends a `SIGTERM` signal to the process.)
> ^differences-in-realtime

# History
- [0.17.0 - 2022-11-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26):
	- The output channel can now handle output in [[Realtime output handling|realtime mode]], too. ([#275](https://github.com/Taitava/obsidian-shellcommands/issues/275)).
	- Added a button for terminating long-running shell commands - only appears in realtime mode. ([#289](https://github.com/Taitava/obsidian-shellcommands/issues/289)).
	- Fixed: Redirecting output content repeated possible output wrapping ([#278](https://github.com/Taitava/obsidian-shellcommands/issues/278)).
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): Hitting the `Enter` key in the modal now closes it, although it won't probably be used much, because it requires that the output text field is not focused. Also `Esc` key can be used for closing, which has always been possible. ([#216](https://github.com/Taitava/obsidian-shellcommands/issues/216)).
- [0.12.0 - 2022-05-07](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07): Added hotkeys for redirecting the output. Also, `Ctrl`/`Cmd` + clicking a button closes the modal. ([#145](https://github.com/Taitava/obsidian-shellcommands/issues/145)).
- [0.11.1 - 2022-03-05](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0111---2022-03-05): Fixed line splitting glitches: ([#172](https://github.com/Taitava/obsidian-shellcommands/issues/172))
	- Long shell commands were not splitted to multiple lines.
	- When the window is narrow, redirection buttons were not splitted to multiple lines. This fix also made the buttons wider, but smaller in height.
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26): If some text is selected, only the selected text will be used instead of the whole text. ([#158](https://github.com/Taitava/obsidian-shellcommands/issues/158)).
- [0.10.0 - 2022-02-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06): The output channel was released. ([#134](https://github.com/Taitava/obsidian-shellcommands/issues/134)).

> [!page-edit-history]- Page edit history: 2022-01-02 &#10132; 2022-11-26
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c96937ed11df76038408f3b8e89529e6732878fc): 0.17.0 is released.
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/51befca61156a26873f502966d42de2d98b382fe): 'Ask after execution' and 'Notification balloon': Mention an icon that can be used to terminate processes.
> - [<small>2022-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cfdba5f85d4f92207a8fb81b14c9116b8e1f465f): Output channel - Ask after execution: Add a history record for a wrapping bug fix.
> - [<small>2022-11-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ba41cfb111b3cfd904f82df2746ef4689d9abba3): Realtime output handling.
> - [<small>2022-11-04</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d1672477a14a81a5fc168b1a7dce329a909fd969): Output channel - Ask after execution: Add an alias.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/946bdf5546a1580a4332cce169aa03a65ca9f0b9): Modals: Mention in history records that modals can be closed by hitting the 'Enter' key.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/002bf3b92e8f50bd1deb304dab946a3b8f981c8e): 0.12.0 is released.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/df021e7305cee4944a440c4c16bf7b3a283dcd1f): Beta 0.12.0: Add notices.
> - [<small>2022-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f0032fa9e63d09daab9d1709605d3373f1883a7a): Output channel - Ask after execution: Added hotkey information.
> - [<small>2022-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/622ea4065627bb6ee6104b3366421981a23675c8): Ouput channel Ask after execution: Wrapping gliches are fixed.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d6e852c88fb1ba221140841ea599189a27864a19): 0.11.0 is released.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e5463e54d3424913624f9ebc61fcc7f5dee829cb): 0.11.0 is released.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7537045e3408a0fa0a1f3b47a62907fc6e4f8ca3): Add annotations regarding 0.11.0-beta.1 test.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8c44ea0dd0bdbc370ff4b0ad1469373333f1ca4d): Output channel Ask after execution: Fixed the heading.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e355e9dc73c311afb913088c7076f495e977dcc4): Output channel Ask after execution: Add information about selecting text.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3cc94c373e6fdff6712511de5cb0482c2c7ba5e9): 0.10.0 is released.
> - [<small>2022-02-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1a84fe59a57f760fa9773a70cf41693982d571ef): #134: Output channel - Modal: Change the title to "Output channel - Ask after execution".
> - [<small>2022-01-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/db74fd2ed107c70fc30a73fa4f23fea2e5957eae): Mark certain features to be only available in the 0.10.0 beta test.
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/88f88ce46a22a9a7ae4ce3f93727dca1ed8b97bd): Output channel: Modal.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Output%20handling/Output%20channel%20-%20Ask%20after%20execution.md).
> ^page-edit-history