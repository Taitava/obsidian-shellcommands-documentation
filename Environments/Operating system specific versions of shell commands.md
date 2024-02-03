Probably most users use their Obsidian vaults on a single operating system, be it Windows, Linux or macOS. For those, the feature of _operating system specific versions of shell commands_ is not needed.

But if you happen to have a vault that you synchronize between computers that have **different** operating systems (e.g. one computer is a macOS, and another has Windows), and if you also synchronize the *Shell commands* plugin's settings between the computers, you might end up in a situation where some of your commands only work on one of the operating systems, but not others.

*Operating system specific versions of shell commands* allows you to define a command so that on certain operating system, it executes a shell command that is specifically tailored for that particular operating system, and on another operating system, another shell command is executed.

**Note that mobile platforms are not supported by the plugin, so this feature only supports desktop operating systems Windows, Linux and macOS.** #mobile

## Instructions
1. Head over to the plugin's settings, and look for a shell command that you would like to customize to have different versions for different operating systems. In this example, I'm going to use a command aliased *Terminal in test suite folder*, which is supposed to open either [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) or [Xfce terminal on Linux](https://docs.xfce.org/apps/terminal/start):
	![[Settings-main-click-environments-icon.png]]
2. Notice that in the picture above, the shell command field is empty. It's possible to leave this field empty, if operating system specific command fields are filled (that'll be done soon). This field is called an *operating system **agnostic** shell command* field, meaning that this field can contain a shell command that will be executed if there is **no** explicit shell command defined **for the current** operating system.
3. Click the *Shell selection, Operating system specific shell commands* icon button.
4. An *extra options modal* will pop up, showing shell command fields for all the three supported operating systems:
	![[Settings-modal-environments.png]]
5. In the picture above, there are different shell commands specified for Linux and Windows. macOS does not have a command, because I haven't planned to execute this particular command on macOS. If I execute it on macOS, SC would show an error *The shell command is empty*, because like was shown in the step *2*, also the operating system agnostic shell command field is empty.
6. When a shell command is executed, the *Shell commands* plugin will automatically pick a correct shell command version based on the current operating system.

## The *operating system agnostic* shell command field
![[Settings-main-a-shell-command.png]]
Prior to SC version `0.7.0`, each shell command had only one shell command field. In `0.7.0`, the field's purpose has been slightly redesigned: it works as a *fallback* shell command, meaning that it will be executed if no shell command version exists for the current operating system.

This has certain advantages:
- For vaults that are synchronized between all the three operating systems, it's possible to create an operating system agnostic shell command for two of the operating systems (e.g. Linux and macOS), while defining a special shell command for the third operating system (e.g. Windows). In practice, Linux and macOS tend to use very similar [[Shell|shells]], with some commands being the same in both operating systems, so sometimes they can share the exactly same shell command, while Windows with its very different shell ([[CMD.EXE]] or [[PowerShell]]) can have a different shell command.
- Shell commands defined in SC versions prior to `0.7.0` will work regardless of what the operating system is, just like they did before.

## Different ways to synchronize vaults and settings
Because this feature is only meaningful in situations where vaults and settings are synchronized between multiple computers, I'll also list a few different methods to synchronize your Obsidian vaults and settings. The *Shell commands* plugin itself does not need to be aware of what kind of synchronization system you use - you can use whatever.

- [Obsidian Sync](https://obsidian.md/sync): The official way to synchronize Obsidian vaults and settings. Probably the easiest to set up. **Paid**.
- [Git](https://git-scm.com) + [GitHub](https://github.com)/[GitLab](https://gitlab.com)/[BitBucket](https://bitbucket.org): A very good way to manually store versions of your files in a version control system. Allows you to annotate (= write notes about) each change that you make to your files. Git has a learning curve, but if you are willing to use time, it'll pay off in the end, and it's usable for other projects outside of Obsidian, too. If you'd like to automate this, you can take a look at a community plugin named [Obsidian Git](https://github.com/denolehov/obsidian-git). **Free** for most use cases. *(Git itself is always free, but the hosting providers do have both free and paid plans available, with the free plans offering enough space and features for most Obsidian vaults).*
- [Dropbox](https://dropbox.com), [iCloud](https://icloud.com), [OneDrive](https://onedrive.com), [Google Drive](https://google.com/drive): General file synchronization services. **Free** for most use cases.

# History


> [!page-edit-history]- Page edit history: 2021-10-03 &#10132; 2023-02-28
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7c25de016fcfca074a5743207377e6730e6a58f9): Change word "Macintosh" to "macOS".
> - [<small>2022-04-19</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/893a7098c3a22942bf115447418212a97c616dcb): Forgot to rename directory 'Operating systems and shells' to 'Environments'.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b5c6aabefb69afcf387fb2a4fd20e9c223f080bc): 0.12.0: Updated old screenshots to contain 'Environments', 'Preactions' and 'Variables' tabs.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/464f32b37f6ce9d2779b3fc5181b850cb2ad593c): Operating system specific versions of shell commands.md: Remove an unnecessary TODO comment.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/34848568584de5a45d67928d41221ed5cb7aa69e): Operating system specific versions of shell commands.
> - [<small>2021-11-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/aba3caead0248996d5fcf0f99799f8e5be271544): Some quick plans for topics related to operating systems and shells.
> - [<small>2021-10-31</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2dd3261379bc2817e7ea01b96872402ad7c3c4d1): Some quick plans for the documentation.
> - [<small>2021-10-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5693b00490180aded4d5da5f80cb1bcdafecba6c): Initial commit.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Environments/Operating%20system%20specific%20versions%20of%20shell%20commands.md).
> ^page-edit-history