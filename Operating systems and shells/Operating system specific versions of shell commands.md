#TODO write about how to use the feature.

# Operating system specific versions of shell commands
Probably most users use their Obsidian vaults on a single operating system, be it Windows, Linux or Macintosh. For those, the feature of _operating system specific versions of shell commands_ is not needed.

But if you happen to have a vault that you synchronize between computers that have **different** operating systems (e.g. one computer is a Macintosh, and another has Windows), and if you also synchronize the *Shell commands* plugin's settings between the computers, you might end up in a situation where some of your commands only work on one of the operating systems, but not others.

*Operating system specific versions of shell commands* allows you to define a command so that on certain operating system, it executes a shell command that is specifically tailored for that particular operating system, and on another operating system, another shell command is executed.

**Note that mobile platforms are not supported by the plugin, so this feature only supports desktop operating systems Windows, Linux and Macintosh.** #mobile

## Instructions
1. Head over to the plugin's settings, and look for a shell command that you would like to customize to have different versions for different operating systems. In this example, I'm going to use a command aliased *Terminal in test suite folder*, which is supposed to open either [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) or [Xfce terminal on Linux](https://docs.xfce.org/apps/terminal/start):
	![[Settings-main-click-operating-systems-and-shells.png]]
2. Notice that in the picture above, the shell command field is empty. It's possible to leave this field empty, if operating system specific command fields are filled (that'll be done soon). This field is called an *operating system **agnostic** shell command* field, meaning that this field can contain a shell command that will be executed if there is **no** explicit shell command defined **for the current** operating system.
3. Click the *Shell selection, Operating system specific shell commands* icon button.
4. An *extra options modal* will pop up, showing shell command fields for all the three supported operating systems:
	![[Settings-modal-operating-systems-and-shells.png]]
5. In the picture above, there are different shell commands specified for Linux and Windows. Macintosh does not have a command, because I haven't planned to execute this particular command on Macintosh. If I execute it on Macintosh, SC would show an error *The shell command is empty*, because like was shown in the step *2*, also the operating system agnostic shell command field is empty.
6. When a shell command is executed, the *Shell commands* plugin will automatically pick a correct shell command version based on the current operating system.

## The *operating system agnostic* shell command field
![[Settings-main-a-shell-command.png]]
Prior to SC version `0.7.0`, each shell command had only one shell command field. In `0.7.0`, the field's purpose has been slightly redesigned: it works as a *fallback* shell command, meaning that it will be executed if no shell command version exists for the current operating system.

This has certain advantages:
- For vaults that are synchronized between all the three operating systems, it's possible to create an operating system agnostic shell command for two of the operating systems (e.g. Linux and Macintosh), while defining a special shell command for the third operating system (e.g. Windows). In practice, Linux and Macintosh tend to use very similar [[Shell|shells]], with some commands being the same in both operating systems, so sometimes they can share the exactly same shell command, while Windows with its very different shell ([[CMD]] or [[PowerShell]]) can have a different shell command.
- Shell commands defined in SC versions prior to `0.7.0` will work regardless of what the operating system is, just like they did before.

## Different ways to synchronize vaults and settings
Because this feature is only meaningful in situations where vaults and settings are synchronized between multiple computers, I'll also list a few different methods to synchronize your Obsidian vaults and settings. The *Shell commands* plugin itself does not need to be aware of what kind of synchronization system you use - you can use whatever.

- [Obsidian Sync](https://obsidian.md/sync): The official way to synchronize Obsidian vaults and settings. Probably the easiest to set up. **Paid**.
- [Git](https://git-scm.com) + [GitHub](https://github.com)/[GitLab](https://gitlab.com)/[BitBucket](https://bitbucket.org): A very good way to manually store versions of your files in a version control system. Allows you to annotate (= write notes about) each change that you make to your files. Git has a learning curve, but if you are willing to use time, it'll pay off in the end, and it's usable for other projects outside of Obsidian, too. If you'd like to automate this, you can take a look at a community plugin named [Obsidian Git](https://github.com/denolehov/obsidian-git). **Free** for most use cases. *(Git itself is always free, but the hosting providers do have both free and paid plans available, with the free plans offering enough space and features for most Obsidian vaults).*
- [Dropbox](https://dropbox.com), [iCloud](https://icloud.com), [OneDrive](https://onedrive.com), [Google Drive](https://google.com/drive): General file synchronization services. **Free** for most use cases.