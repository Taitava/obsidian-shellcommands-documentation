A *working directory* is a folder where your shell commands are executed in. This means, that all shell commands that *read*, *create*, *modify*, *move*, *delete* or otherwise access *files* or *folders*, will perform these actions in the *working directory*. By default, the *working directory* is your vault's root directory, but you can change it.

## Changing the working directory for all shell commands
1. Open up the plugin's settings panel, and open the *Environments* tab:
	![[Settings-main-environments-tab.png]]
2. You'll see the *Working directory* text field. When it's empty, it shows the default directory that will be used as a *working directory*.

The following values are possible:
- Empty: Use the vault's root directory.
- A relative path to a directory (does not begin with a `/`, `\` or `C:\`): Use a folder in the vault.
- An absolute path to a directory (does not begin with a `/`, `\` or `C:\`): Use a folder outside of the vault.

The specified *working directory* must exist and be a directory, not a file. Otherwise, the plugin will not allow executing any shell commands.

## Changing the working directory for a specific shell command
There is no explicit setting for defining a *working directory* on a per shell command basis, but you can achieve the same effect by preceding your shell command with: `cd "Your desired working directory" && `. The `&&` operator is used to execute two shell commands sequentially: your actual shell command will be executed only if the `cd` command succeeded to change the *working directory*.

An example: `cd "C:\Windows\Temp" && mkdir "My temporary directory"`

# History


> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2022-04-08
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/b5c6aabefb69afcf387fb2a4fd20e9c223f080bc): 0.12.0: Updated old screenshots to contain 'Environments', 'Preactions' and 'Variables' tabs.
> - [<small>2022-04-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fad0f25eae8bdfa9ecd82fda2d32fbbddbe3654f): Change 'Operating systems & shells' tab name to 'Environments'.
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/9873c4587a2b97c6a61a5cbfc2bb7ce55834ffda): Basic usage instructions.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Basic%20usage/Working%20directory.md).
> ^page-edit-history