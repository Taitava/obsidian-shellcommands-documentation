---
cssclass: customiseTitle
---
# Roadmap: The horizon of SC `1.0`

This page sums up some far-future goals of the *Shell commands* project. There are some fundamental features on my radar that I want to address here, because even though they are important, implementing them needs a lot of time, and often the presence of other planned features (= prerequisites). Some of the features are originating from other people's ideas, and I want to be more open about how I'm going to place them on the path of the future of this plugin.

The list of features is not explicit: new ideas may be born along the way, and current ones may be refined.

> [!Info] Other places to look for incoming features
> - There is [an older roadmap in GitHub](https://github.com/Taitava/obsidian-shellcommands/projects/1), but I haven't really utilized it to its full potential, and it's also not quite the thing I'm looking for: I want a roadmap that shows a one glance overview of far-ahead cornerstone features without the noise of near-future small features. I'm currently considering to retire the roadmap in GitHub. 
> - For a complete list of all ideas/plans for features including both big and small, please see [this *Ideas* discussion section in GitHub](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas). In case you happen to have an idea, you can suggest it there 😉. Once ideas are implemented and released, they are moved to [*Ideas - done & released*](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas-done-released).

# Cornerstone features of SC `1.0`
These are not in any particular order, but some features are needed to be done before some other features can be done.
## [Migrations: Better support for complex, nested configuration properties](https://github.com/Taitava/obsidian-shellcommands/discussions/198)
 - A robust way is needed to upgrade old settings files to formats specified by newer versions of the *Shell commands* plugin. Version upgrades tend to bring changes to the format of the settings file constantly, there will never be a "final state".
 - A crucial prerequisite for importing/exporting shell commands, because the exporting format will be heavily based on the settings format.

## [Import / export shell commands (#151)](https://github.com/Taitava/obsidian-shellcommands/discussions/151)
- Allows users to share their shell commands with others easily by exporting them to a textual format that includes all settings related to the particular shell command.
- One user can share shell commands between their different vaults, or to different users.
- There will be a GitHub repository designated for sharing shell commands publicly with others, but shell commands could also be easily shared in Discord, forums or by other public or private means.

## [JavaScript API (#219)](https://github.com/Taitava/obsidian-shellcommands/discussions/219)
- The most basic level: support treating shell command output as JavaScript code that could be evaluated. Need to provide some basic public API, at least access to Obsidian's `app` (or maybe there's no need, as it [seems to be global nowadays](https://forum.obsidian.md/t/obsidian-release-v0-14-4-insider-build/35026)).
- Later: Define a public API that allows calling some of the *Shell commands* plugin's methods from user code (= either JavaScript that is received as output from shell commands, or JavaScript written in other community plugins).

## [Tighter integration with Templater plugin.](https://github.com/Taitava/obsidian-shellcommands/discussions/217)
- Allow executing [Templater](https://github.com/SilentVoid13/Templater) scripts after a shell command is executed.

## [PowerShell: Handle output encoding](https://github.com/Taitava/obsidian-shellcommands/discussions/157)
 - Currently, [[PowerShell]] only works well when used with text that has only English characters - even if Unicode is used. Combine that to the fact that [[Escaping special characters in variable values#Escaping depends on the shell|there is not variable value escaping for CMD]], Windows as a platform is not currently as well-supported by the *Shell commands* plugin, comparing to Linux and macOS.

## [Methods for variables (#147)](https://github.com/Taitava/obsidian-shellcommands/discussions/147)
 - A prerequisite for [#105](https://github.com/Taitava/obsidian-shellcommands/discussions/105).

## [Variables: Handling separator arguments without escaping (#105)](https://github.com/Taitava/obsidian-shellcommands/discussions/105)
 - I could add more variables that present listed content, but currently [[{{tags}}#Special characters in separator are escaped|there's no solid way to define item separators when joining list items together]]. [[{{tags}}]] is currently the only variable that provides a list of values, and I don't want to create more like it before I develop a proper way to define separators.

# Already implemented features

| SC version                                                                                           | Feature                                                             | Discussion                                                                | Completed  |
|:---------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------- |:------------------------------------------------------------------------- | ---------- |
| [0.19.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0190---2023-05-27) | Support custom shells                                               | [#108](https://github.com/Taitava/obsidian-shellcommands/discussions/108) | completely |
| [0.18.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06) | Pass variables to `stdin`                                           | [#89](https://github.com/Taitava/obsidian-shellcommands/discussions/89)   | completely |
| [0.17.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0170---2022-11-26) | Realtime output handling                                            | [#64](https://github.com/Taitava/obsidian-shellcommands/discussions/64)   | completely |
| [0.13.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28) | Execute shell commands via Obsidian URI                             | [#195](https://github.com/Taitava/obsidian-shellcommands/discussions/195) | completely |
| [0.12.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07) | A modal for asking values from user (Prompt)                        | [#17](https://github.com/Taitava/obsidian-shellcommands/discussions/17)   | partially  |
| [0.12.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07) | Preactions                                                          | [#183](https://github.com/Taitava/obsidian-shellcommands/discussions/183) | partially  |
| [0.12.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0120---2022-05-07) | Custom variables                                                    | [#146](https://github.com/Taitava/obsidian-shellcommands/discussions/146) | partially  |
| [0.10.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0100---2022-02-06) | Events: Execute shell commands automatically when something happens | [#60](https://github.com/Taitava/obsidian-shellcommands/discussions/60)   | partially  |
| [0.7.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25) | Escaping variable values                                            | [#11](https://github.com/Taitava/obsidian-shellcommands/issues/11)        | completely |
| [0.5.0](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02) | Output channels                                                     | [#16](https://github.com/Taitava/obsidian-shellcommands/discussions/16)   | partially  |



# History


> [!page-edit-history]- Page edit history: 2022-07-21 &#10132; 2023-05-28
> - [<small>2023-05-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ec4cb08d2ec909a4866415434569e1b55a47555d): Roadmap: Custom shells are now implemented.
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f2b125e40b6f6beafdec7abf9f53890137347040): Roadmap.md: `stdin` support is now implemented.
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1d2f69e560da073028233e767a0ea164023fb656): Roadmap: Mark that realtime output handling is implemented.
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/158eba2360a38dfcc4732d08e0373182e0c2a7e3): Roadmap: Mention `stdin` support.
> - [<small>2022-07-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6c9df8e8d8769676d3c160c56c1ed26b4a415504): First version of Roadmap.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Roadmap.md).
> ^page-edit-history