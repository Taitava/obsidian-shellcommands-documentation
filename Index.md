---
cssclass: customiseTitle
---
# Shell commands - Documentation
*Shell commands* is a community plugin for [Obsidian.md Markdown editor](https://obsidian.md). Its purpose is to make it possible to execute system commands from within Obsidian (the same commands that you can execute in a [terminal](https://en.wikipedia.org/wiki/Terminal_emulator)).

The plugin's development can be followed in [Taitava/obsidian-shellcommands GitHub repository](https://github.com/Taitava/obsidian-shellcommands).

## Who is this plugin for, and the expected skill level
This plugin is aimed for people who **want to**:
- Launch external applications - with a possibility to make them use Obsidian vault's files and folders.
- Create commands for automatic creation, modification and/or deletion of files and folders in the vault.
- Use certain content related information as part of their commands, e.g. the *name*, *title* or *tags* of the currently open file, or currently selected text, or text present in the clipboard. (These are called [[Variables - general principles|{{variables}}]]).

... and people who **know**:
- How to use some basic shell commands in a terminal.
- How to identify commands that are safe to execute. Or rather: do not use a command whose meaning is not completely recognized.
- Approximately that there are different *shells* (e.g. Bash, Dash, Zsh, CMD, PowerShell 5 and PowerShell Core). You don't need to know all of them, but at least get to know [[Shells|what is your own shell]].

## Installation
See [installation instructions in the plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands#installation--usage).

[[Upgrading (and downgrading)|Upgrading instructions - and downgrading, if necessary]]

## Basic usage

### Defining your shell commands
- [[How to define shell commands]]: Start from this.
- [[Example shell commands]]: Sources of ideas for what you can achieve with this plugin. Modify and make them fit your particular needs.
- [[Output channels]]: Where to put possible text outputted by your commands: in a notification balloon, status bar, in the currently open file, in the clipboard, or just ignore.
- [[Working directory]]: Defining in which folder your shell commands will operate.
- [[Monitoring execution]]: Turn on notifications that show all long-running shell commands.

### Variables
- [[Variables - general principles]]: How to pass vault related information to your commands.
- [[Escaping special characters in variable values]]: Using variables safely.

### Execution
There are a few different ways to execute your shell commands:
- All shell commands can be executed via [Obsidian's command palette](https://help.obsidian.md/Plugins/Command+palette) (unless they are [[Events - general principles#^exlude-from-command-palette|excluded]]).
- You can assign keyboard hotkeys to shell commands. #TODO: Add instructions.
- [[Shell commands URI]] can be used to create custom links that execute your shell commands - both inside Obsidian notes, and externally from other applications.
- [[Events - general principles|Events]] can execute your shell commands automatically when certain things happen, e.g. when Obsidian starts or quits.

### Problems
- [[Problems]]: A compilation of issues that many users have reported.

## Advanced features
You will probably not need to look at these features in the beginning. These might come in handy in some use-cases, though.

### Output
- [[Ignoring errors]]
- [[Output wrappers|Wrapping output with surrounding text]]
- [[Realtime output handling]]

### Preactions
Actions that are performed before executing a shell command, i.e. preparations.
- [[Prompts]]: Ask values from a user.

### Variables
- [[Custom variables]]
- [[Default values|Default values for variables]]
- [[Pass variables to stdin]]

### Environments: Operating systems and shells
- [[Operating system specific versions of shell commands]]
- [[Shells]]

### Hidden settings
- [[Hidden settings|There are some minor settings that do not have a visible field in the settings user interface]]

## Future development
- [[Roadmap]]

## Improving the documentation
- For ideas on how to improve the documentation: [Create a new discussion in the *Shell commands* plugin's GitHub repository's *Ideas* discussion category](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/ideas).
- For clear errors in the documentation (that are simple to fix): Change it yourself and [create a pull request in the documentation's GitHub repository](https://github.com/Taitava/obsidian-shellcommands-documentation/pulls). If you are unsure how to work with Git and how to make PRs, it's also okay to just create a new discussion.

All feedback and ideas are greatly appreciated! 🙂

## Screenshots in the documentation
The documentation is partly illustrated with screenshots. The screenshots may look different from how the plugin's user interface looks in your Obsidian, as you might use a different theme, a different color mode, a different version of Obsidian, and a different operating system.

The screenshots are taken in the following environment:
- Theme: [Red graphite](https://github.com/seanwcom/Red-Graphite-for-Obsidian)
- Color mode: Light (with dark contrast side panes, provided by *Red graphite*)
- Operating system: Windows

Also, some screenshots may be from older versions of SC, in case no significant changes have occurred, or if screenshots have been forgotten to update. You can see from which version of SC a particular screenshot has been taken from, by looking at which folder it resides in (e.g. `Assets/Images/SC 0.10.0 - Obsidian 0.13.23`).

![[Settings-main-shell-commands-tab.png]]
(An example screenshot from the main settings view of SC version `0.10.0`. You can tell it's taken on Windows, because the shell command previews show an escape character `` ` `` that is used by *PowerShell*, instead of `\`, that is used by e.g. *Bash* on Linux and macOS. Also, the hotkeys `Ctrl` + `G` and `Ctrl` + `Shift` + `G` indicate that the screenshot is not taken on macOS, which would have `Cmd` instead of `Ctrl`.)


# History


> [!page-edit-history]- Page edit history: 2021-10-03 &#10132; 2023-02-28
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2023-02-13</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ac067d75771cfb2b7aae3bd3e1788491fb9de37a): Index.md: Fix stdin link.
> - [<small>2022-12-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c9c81dbfada887011827c82b9c6dcf60b962e4a3): Pass variables to stdin.md
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b66e987b28739cf2875a1dd33349420c832ca6e2): Index: Add a link to 'Realtime output handling'.
> - [<small>2022-11-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/202411b0f08dacf29b0967f7e6e16ff3cde0aed3): Documentation for execution notification.
> - [<small>2022-09-01</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fd9edbf69c25863a39526cf3fe00077625f6a01d): Output wrappers.
> - [<small>2022-07-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/6c9df8e8d8769676d3c160c56c1ed26b4a415504): First version of Roadmap.
> - [<small>2022-07-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/54fe6f9cbcc46737650513163c0af638fcebc270): Index.md: Add Problems link.
> - [<small>2022-05-07</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1ea6e6dfc57d520e523cfde196bce955d7b1a06): Beta 0.12.0: Remove notices.
> - [<small>2022-04-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1435534a8ba1bc862237cd5c067b5c0ce07b35c4): Shell commands URI.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3a0deef66398b57fe209025e4761fe55b27e992a): Index.md: Add a link to Prompts.md.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ddb140ebf5f8abd8a3b0b68acb954a6aee9cdc69): Beta 0.12.0: Add notice to Prompts.md.
> - [<small>2022-04-15</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/201b79ea1a42ab903f947424990332f449a24ffc): Index: Add a link to Default values.
> - [<small>2022-04-11</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/91702a4b6edda4a90120067de22de23a26383240): Custom variables.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/61658656e301113c3139c1b1dfe1653d0e4a0063): 0.12.0: Instructions for Prompts.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fad0f25eae8bdfa9ecd82fda2d32fbbddbe3654f): Change 'Operating systems & shells' tab name to 'Environments'.
> - [<small>2022-02-27</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c29ca8761f2f05a8ed149b447447304becb0e3c9): Fix github repository link
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fabdd6cf143447380e2f28f92ee7752d169d2554): Create a page for Hidden settings.
> - [<small>2022-01-29</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1e61b410c2336cef01cda5321766bcba85cf60d7): Update some screenshots to contain "Events" main settings tab.
> - [<small>2022-01-02</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/13c1f6a730fafb892c14d6598b58592b3bdb5fc0): Typo fixes.
> - [<small>2021-12-04</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0c1282c0d04a2dc6bfd8b357ab2955ad856ce008): Index: Add information about creating a PR for correcting errors in the documentation.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3ff17d13c815a111e48ab5d2ced7a084fce0b280): Instructions to downgrade the plugin.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/9873c4587a2b97c6a61a5cbfc2bb7ce55834ffda): Basic usage instructions.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/c0604c80a2db202476658a3ac945d3e8ccbf56f1): Upgrading.md: About semver and how to upgrade.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/ef45ee2d438bd565ed11c39ab2b8e1557d24aa6b): Index.md: Add a todo comment.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a222616b109b84d621c8376c0a8c22365fe576f9): Image assets: Add Obsidian version to the folder name.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3d719ac9dce5421807fdddc4a3cbca6afdc6eb95): Index.md: Move the Installation section up.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/118aaeb67eed11873cbe54c98b0f74b152b1c210): Shells.md: Add 'Choosing a shell on a per shell command basis'.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3010cd79f48e79b997509b6a8a1b0bad5a23993b): Create Shells.md.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/99a2b8dffec8e307302c234755f255eda41c0317): Index.md: Mention that it's expected that users know their shell.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4f3c84cfe4f74062679a566ead734d03a5c97f5c): Index.md: Add notes about improving the documentation.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d86be45a35f3f26c1525de98d88dcc7c81a50b62): Index: Add information about screenshots.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/366f1cecd4709d2da639b76fd2269e0f6d4a11ba): Fix a couple of links.
> - [<small>2021-11-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/51879d0d421cfde702d2699a2209332b24836e3f): Index: Add a list of topics and some other stuff.
> - [<small>2021-10-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2dd3261379bc2817e7ea01b96872402ad7c3c4d1): Some quick plans for the documentation.
> - [<small>2021-10-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5693b00490180aded4d5da5f80cb1bcdafecba6c): Initial commit.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Index.md).
> ^page-edit-history