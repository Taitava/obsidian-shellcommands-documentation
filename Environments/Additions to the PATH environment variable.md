# Additions to the `PATH` environment variable
> [!Info] What is `PATH`?
> `PATH` is an [environment variable](https://en.wikipedia.org/wiki/Environment_variable) used in macOS, Linux and Windows (and some other operating systems) to specify directories where executable programs are located. Executable programs can be located also in other directories not specified in `PATH`, but then their execution requires to use either their full path (= directory + file name) or they need to be located in the current [[working directory]].
> 
> It's convenient to have all frequently executed programs' directories specified in the `PATH` environment variable, so that only the program's file name is needed to be able to execute it.

## The traditional way to add directories to `PATH`

For the sake of understanding how additions to `PATH` are done in a normal terminal session or in a script file (= outside the *Shell commands* plugin's context), I'll first discuss this traditional method, and after that I'll describe a more recommended and easier way to do it in the *Shell commands* plugin.

A basic way to add directories to `PATH` is to prefix shell commands with the following:
 - For Bash/Dash/Zsh in macOS/Linux: `export PATH=$PATH:/an/additional/directory:/another/additional/directory; your-command-here`
 - For CMD in Windows: `set PATH=%PATH%;C:\an\additional\directory;C:\another\additional\directory & your-command-here`
 - For PowerShell in Windows: `$env:Path += ";SomeRandomPath"; your-command-here`

This needs to be done in every shell command where you need to execute the programs located in the additional directories. The modifications to the `PATH` environment variable are only effective during the execution of a shell command, the modification is not active anymore when other shell commands are executed.

Adding this kind of prefixes in front of shell commands can be quite cumbersome, and they affect negatively the readability of shell commands. Also, repeating the same directory additions in multiple shell commands makes it harder to modify the additions later, because you need to remember to modify them in multiple places.

## An easier way to add directories to `PATH`

The *Shell commands* plugin allows you to define additional directories in the settings. The additions will apply to **all shell commands in the Obsidian vault**.
1. Open up the main settings view and go to the *Environments* tab:
	![[Settings-main-environments-tab.png]]
2. Scroll downwards to see the section *Add directories to the PATH environment variable*. You'll see three text fields where you can define directories that should be added to `PATH`.
> [!Tip] Different fields for each operating system
> - If you happen to synchronize your vault between multiple devices that use different operating systems, you can specify different additions for each operating system.
> - If you are using your Obsidian vault in only one device, you'll just use the field that corresponds to your current operating system, and leave the other two fields empty.
3. Define the directories you want to add to `PATH`.

### Adding multiple directories
There's two ways to separate multiple directories from each other:

> [!Example] Define each directory on a separate line
> *This is easy to read.*
> 
> ![[Settings-main-environments-PATH-additions-example-multi-lines.png]]

> [!Example] Separate directories by a colon `:` or a semicolon `;`
> *Easy e.g. when copying and pasting `PATH` additions from the internet.*
> 
> ![[Settings-main-environments-PATH-additions-example-single-line.png]]
> **Check which separator your operating system uses!**
> - Linux and macOS use colons `:`
> - Windows uses semicolons `;`

If you separate the directories by defining them on separate lines, the *Shell commands* plugin will internally transform the definition to use colon `:` or semicolon `;` separators, depending on your operating system. No newlines will be inserted to `PATH`.

### Deciding the insertion order
The `PATH` environment variable always contains some default directories. By default, the *Shell commands* plugin appends all the additional directories **after** the directories already existing in `PATH`.

> [!Example]
> 1. Assume that `PATH` contains `/usr/local/bin` by default. (In real life, it contains more directories, but let's keep it short here).
> 2. Assume you'll want to add `/an/additional/directory` to `PATH`.
> 3. The *Shell commands* plugin adds `/an/additional/directory` **after** `/usr/local/bin`.
> 4. Result: `PATH` will be `/usr/local/bin:/an/additional/directory`.

> [!Question] Does it matter whether the additions are appended before or after the default content of `PATH`?
> Usually there's no difference, but some special cases might require you to change the insertion order.
> - Appending to the end of `PATH` might be slightly better for performance, although the effect can be minuscule. Directories are evaluated in the order they are defined, so it's good to have standard system commands appear before any custom programs, to make standard commands work efficiently. This is the default behavior of the *Shell commands* plugin.
> - Appending to the beginning of `PATH` might be required if you need to **override standard system commands** with custom programs. Then again, to be on the safe side, avoid appending to the beginning, if you want to make sure that you never override standard commands accidentally.
> 
> More information on the insertion order: http://www.troubleshooters.com/linux/prepostpath.htm

#### Inserting directories to the beginning of `PATH`
If you really need to insert directories *before* the default directories in `PATH`, you can use the [[{{environment}}|{{!environment:PATH}}]] variable to denote where you want the **default content of `PATH`** to appear.

> [!Example]
> ```
> /an/additional/directory
> {{!environment:PATH}}
> ```
> This appends `/an/additional/directory` to the beginning of `PATH`.

> [!Example]
> ```
> /an/additional/directory
> {{!environment:PATH}}
> /another/additional/directory
> ```
> This appends `/an/additional/directory` to the beginning of `PATH` and `/another/additional/directory` to the end of it.

> [!Warning]
> Adding custom directories before the default directories in `PATH` may accidentally override some system commands/programs. If a directory you add contains e.g. an executable file named `python`, the custom executable file will be executed **instead of the default `python` executable installed by your operating system** if any of your shell commands execute any programs that execute `python` scripts. Sometimes this might be intentional and desirable, but other times it might be an accident!
> 
> Only change the insertion order if you know what you are doing!

> [!Info] Inserting directories to the beginning of `PATH` does not put them to the exact beginning
> At least when using Windows PowerShell, the PowerShell's directory will always precede everything else in `PATH`:
> > C:\Program Files\WindowsApps\Microsoft.PowerShell_7.2.3.0_x64__8wekyb3d8bbwe;
> 
> This seems to be inevitable. That being said, it should be enough that the additions go before **most** of the other directories.

## Problem: `PATH` doesn't contain all the directories that are available in terminal
If you open up a [terminal emulator window](https://en.wikipedia.org/wiki/Terminal_emulator), you might be able to execute programs that are available in the terminal, but not in shell commands that you execute via Obsidian using the *Shell commands* plugin.

Depending on which shell you use, the terminal window might load one of the following profile files when it starts up:
| Shell      | Profile file              |
| ---------- | ------------------------- |
| Bash       | `~/.bashrc`               |
| Zsh        | `~/.zshrc`                |
| Dash       | No standard profile file? |
| CMD        | No standard profile file? |
| PowerShell | No standard profile file? |

In case you experience a problem that some program/command that you try to execute is not found for some reason (you get an error message saying e.g. `Command not found`), you should check if the `PATH` environment variable has any differences when read from a terminal application versus when reading from Obsidian using the *Shell commands* plugin.

### How to check the content of `PATH` in Obsidian using the *Shell commands* plugin
1. Open up the main settings view and go to the *Environments* tab:
	![[Settings-main-environments-tab.png]]
2. Click the small *Show the current PATH content* icon:
	![[Settings-main-environments-show-PATH-content-icon.png]]
3. A modal will open up showing the default content of `PATH`:
	![[Settings-current-PATH-content-modal.png]]
	The modal is a bit hard to read, because long lines are not completely visible, but it can be scrolled.
	
### How to check the content of `PATH` in a terminal application
1. Open up a terminal application. There are multiple terminal applications available, and probably your computer has some installed by default. Example terminals, but you can use others, too:
	- Linux: E.g. `konsole` or `gnome-terminal`
	- macOS: *iTerm* / *iTerm2*
	- Windows: _Windows Terminal_, _PowerShell_ or _Command prompt_
2. Execute the following command in the terminal:
	- Linux / macOS: `echo $PATH`
	- Windows CMD: `echo %PATH%`
	- Windows PowerShell: `echo $Env:PATH`

Compare the result that you got from the command executed in terminal, versus the result that you saw in the *Current PATH content* modal above.
 - If the modal displays fewer directories than the command executed in terminal, it means that some programs/commands that you can execute via a normal terminal, are unavailable when using the *Shell commands* plugin. [[#An easier way to add directories to PATH|Add the missing directories to SC's *PATH additions* settings according to the instructions shown above]].
 - If the results contain all the same directories, then there should be no problems with the `PATH` environment variable.
 - If you still encounter any problems, you can always ask for help in the [*Q & A* discussion category in the *Shell commands* plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands/discussions/categories/q-a).

### Related discussions
The following discussions were had before the ability to define additions to `PATH` was implemented in SC version `0.13.0`:
- https://github.com/Taitava/obsidian-shellcommands/discussions/189
- https://github.com/Taitava/obsidian-shellcommands/discussions/191

## Use variables in `PATH` additions

In addition to the [[{{environment}}|{{!environment}}]] variable, all other [[Variables - general principles|{{!variables}}]] can also be used in the _PATH additions_ settings. I just haven't come up with a use case where it would be beneficial.

> [!Important] Use `{{!` instead of `{{`
> When using `{{variables}}` in the *PATH additions* settings, an exclamation mark `!` needs to be used in the curly brackets (e.g. `{{!environment:PATH}}` instead of `{{environment:PATH}}`). The exclamation mark `!` tells the *Shell commands* plugin **not to escape special characters** in the variable's value. Otherwise, special characters, such as slashes `/`, backslashes `\`, colons `:` and semicolons `;` will be escaped, so they'll become: `\/`, `\\`, `\:` and `\;` (in Bash/Dash/Zsh, i.e. Linux/macOS) or `` `/ ``, `` `\ ``, `` `: `` and `` `; `` (in PowerShell, i.e. Windows), just to list a few examples.
> 
> **This is an exception to the recommendation that most of the time special characters should be escaped.** The content of `PATH` should not be escaped. [[Escaping special characters in variable values|Read more about escaping special characters]].
> 
> ^no-escaping

# History
- #TODO: Add a date [0.13.0 - 2022--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The ability to define PATH additions was born. ([#204](https://github.com/Taitava/obsidian-shellcommands/issues/204)).