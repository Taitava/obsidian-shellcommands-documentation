# Delay when executing a shell command

If your shell command is slow to execute (= has a few seconds delay before the actions of the shell command are done), there can be different reasons for it. Different shells may have different reasons for delays, so please [[Shells#How to know which shell is used|check first what shell you are using]].

> [!info] PowerShell (Windows)
> As far as i know, PowerShell is always slow to start. I do not know a solution for this at this time.

> [!info] CMD (Windows)
> So far, I don't recall seeing reports about CMD being slow.

> [!info] Bash/Dash/Zsh (Linux and macOS)
> ## Things to try
> - [Reinstall Obsidian with the newest installer](https://github.com/Taitava/obsidian-shellcommands/discussions/227).
> - To narrow the problem down, [try to use Templater to execute your shell command](https://github.com/Taitava/obsidian-shellcommands/discussions/187#discussioncomment-2431781), just to see if the delay only happens with SC or not.
> ## Related discussions
> - https://github.com/Taitava/obsidian-shellcommands/discussions/187
> - https://github.com/Taitava/obsidian-shellcommands/discussions/227
> - https://github.com/Taitava/obsidian-shellcommands/discussions/234