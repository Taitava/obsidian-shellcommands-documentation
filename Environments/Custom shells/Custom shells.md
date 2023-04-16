---
aliases:
  - "custom shell"
---

 > [!Warning] This feature is only available in a beta test
 > - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/108#discussioncomment-5277523).
 > %% #TODO: Remove this annotation when the final version is released. %%

> [!Info] About _custom shells_
> As there are only a few [[Shells#Built-in shells|built-in shells]] in the _Shell commands_ plugin (by default, the plugin only supports shells that come pre-installed with certain operating systems), _custom shells_ is a feature that allows defining shells in a more freely manner. Below you'll find a non-exhaustive list of example shells that can be defined as _custom shells_.
> ^about-custom-shells

> [!Example]+ Tailored configuration guides for certain shells
> 
> | Shell | For macOS | For Linux | For Windows |
> | ------- | ---------------|-------------|--------------|
> | [[Windows Subsystem for Linux (WSL)]]<br>Execute Linux shell commands on Windows. | - | - | Yes |
> | [[Windows - MinGW-w64\|MinGW-w64]]<br>Support the GCC compiler on Windows systems, but can be used to execute many other Linux commands, too. | - | - | Yes |
> | [[MacOS or Linux - Wine\|Wine]]<br>A compatibility layer capable of running Windows applications. | Yes | Yes | - |
> | BusyBox (no SC documentation yet)<br> From [busybox.net](https://busybox.net/): _"BusyBox combines tiny versions of many common UNIX utilities into a single small executable."_ | Yes | Yes | Yes, through [frippery.org](https://frippery.org/busybox/index.html) |
> ^tailored-configuration-guides

# Configuring custom shells
You can find instructions for how to configure certain shells in the table above. However, in case you're about to configure a shell that does not have specific instructions, or you need more information about the different settings, you can read the generic instructions for custom shell settings.

> [!Info] Read: [[Settings for custom shells]]

# Path additions

![[Additions to the PATH environment variable#^what-is-path]]

Sometimes program directories need to be explicitly added to the `PATH` environment variable. For [[Shells#Built-in shells|built-in shells]], the _Shell commands_ plugin has a setting named [[Additions to the PATH environment variable#An easier way to add directories to `PATH`|Add directories to the PATH environment variable]]. However, that setting does **not** work for _custom shells_. For custom shells, you can use the following settings to add directories to `PATH`:
 - [[Settings for custom shells#Shell arguments|Shell arguments]]: If your custom shell is [[Bash]], you can try adding `--login` as an option to the _Shell arguments_ setting. `--login` makes [[Bash]] read and execute _profile_ files (e.g. `~/profile`, etc.)  before executing the actual shell command. The executed profile files may add some directories to `PATH`, making more programs available for you. Read more about [Bash startup files and `--login`](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html).
 - [[Settings for custom shells#Wrapper for shell command|Wrapper for shell command]]: If your custom shell is [[Bash]], you can write a preceding shell command that adds directories to the `PATH` environment variable:
  ```
  PATH=$PATH:/additional/directory1:/additional/directory2
  {{!shell_command_content}}
  ```
 - If your custom shell is not [[Bash]], you might still be able to adapt similar techniques to it.

# History
- #TODO: Add a date [0.19.0 - 2023--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2023--): The ability to define custom shells was created. ([#297](https://github.com/Taitava/obsidian-shellcommands/issues/297)).

> [!page-edit-history]- Page edit history: 2023-02-28 &#10132; 2023-04-10
> - [<small>2023-04-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e1a5ac0a0a8b9a3a1532bbad7bb377e2d602dbf3): Custom shells.md: Split `^custom-shells-summary` in half so that the list of shell guides can be linked separately.
> - [<small>2023-03-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/cda9585a23ecbb64bccb380c75fa5df5ae32bc33): Custom shells.md: Put custom shell examples in a table.
> - [<small>2023-03-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/4f304a3cafb96df717a589d73194c3998e45f997): Custom shells.md: Begin writing documentation.
> - [<small>2023-03-05</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/561754f6cbe89180f451508e3cfd4d271240301a): Move the Custom shells.md draft to a new subfolder.
> - [<small>2023-02-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d24ace5fdd47a710b6d7355ec9acf94926ecd64d): Temporary Custom shells.md page.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Environments/Custom%20shells/Custom%20shells.md).
> ^page-edit-history