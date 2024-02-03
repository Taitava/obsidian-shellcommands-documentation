*Shell commands URI* allows you to create links in your Obsidian note files (or in other applications outside of Obsidian) that execute your shell commands when they are clicked.

- Syntax for an example link: `[Execute my shell command](obsidian://shell-commands/?vault=VAULTNAMEHERE&execute=SHELLCOMMANDIDHERE)`
- A shorter example without an explicitly defined vault (will execute the shell command in the most recently opened Obsidian vault): `[Execute my shell command](obsidian://shell-commands/?execute=SHELLCOMMANDIDHERE)`

You can find the id by opening up the shell command's settings modal and going to the *General* tab. There you'll find a *Shell command id:* text.

> [!INFO]- Shell command id format has changed
> Depending on when you have first started using the _Shell commands_ plugin, you might notice a difference between ids of newer and older shell commands:
> - SC version `0.14.0` and below used sequential numbering when creating an id for a new shell command. I.e. shell commands created using version `0.14.0` or earlier, have ids that consist only of numbers.
> - SC version `0.15.0` (released on 2022-08-20) and onwards generate random text ids consisting of 10 characters for new shell commands. The characters are any of letters `a` - `z`  and numbers `0` - `9`.
> - Old shell commands that still have solely numeric ids will continue working like they used to do, and their ids are **not** changed in any way by newer plugin versions. This ensures that relations to existing URI links and hotkey configurations will keep working.
> - The longer format was taken into use because there's a plan to develop an [importing / exporting feature](https://github.com/Taitava/obsidian-shellcommands/discussions/151). Sequential numbering ids could easily cause collisions when trying to import a shell command to a vault that has another shell command that already uses that numeric id.

## Generate the URI easily with a correct id
Looking for the shell command id and writing the URI manually can be cumbersome. To do it easier, you can open up the plugin's main settings view, locate the shell command you want to create a URI for, and click the *Copy this shell command's URI to the clipboard* icon:
![[Settings-main-click-copy-URI-icon.png]]

> [!Tip] Copy a full link element
> You can hold the `Ctrl` / `Cmd` key down while clicking the icon to copy a full markdown link, containing the shell command's [[alias]] text as the link's label.

## Pass values to your shell command via the URI using [[Custom variables|custom variables]]
What makes the Shell command URI really powerful is its ability to customise shell commands by passing values to [[Custom variables|custom variables]]. For example, if you have a large PDF file that has tens or hundreds of pages, and you want to refer to different pages of that PDF document from multiple notes in your Obsidian vault, you can create a single shell command that opens up the PDF file. Each link that you create for executing the shell command can define a different page which to open up, to make it easier to refer to the correct part of the big PDF that is relevant for the clicked link.

To create a shell command and a link according to this example:
1. Create a new custom variable named `{{_pdf_page}}`. [[Custom variables#Creating custom variables in the main settings|Instructions on how to create a new custom variable]].
2. Create a new shell command: `okular -p {{_pdf_page}} /path/to/pdf_reference.pdf` (this assumes you have [Okular](https://okular.kde.org/) installed. You don't need it for custom variables or for the Shell commands URI, it's only mentioned here due to the PDF example). [[How to define shell commands|Instructions on how to create a shell command]].
3. Generate the URI for your shell command using the instructions in chapter [[#An easy way to generate the URI with a correct id]].
4. Pay attention that the copied URI should automatically contain the reference to the custom variable `{{_pdf_page}}` that was created. The reference should look like `&_pdf_page=`. It just contains the custom variable's name with an empty value. Paste the generated URI where you want and add the page number after the equal sign `=` in `&_pdf_page=` .
5. An example of a complete URI: `obsidian://shell-commands/?vault=VAULTNAMEHERE&execute=0&_pdf_page=77`
	
> [!TIP]
> The URI generator inspects the shell command for all custom variables it contains, and inserts them into the generated URI automatically (except that it excludes custom variables whose values come from [[Prompts]], as those do not usually need to be defined in URIs).

### Custom variable rules related to the Shell commands URI
- All URI argument names that start with an underscore `_` are considered to refer to custom variables. E.g. `&_pdf_page=77` assigns the value `77` to the custom variable `{{_pdf_page}}`.
- When you use custom variables in your shell commands, their names are wrapped in `{{` and `}}`. However, in Shell commands URI, the custom variable names must be simplified by leaving the curly brackets out. So, `{{_pdf_page}}` becomes `&_pdf_page=` instead of ~~`&{{_pdf_page}}=`~~. 
- If a custom variable with the given name does not exist, an error message will be shown and the shell command execution will be cancelled for safety reasons.
- You can assign values to multiple custom variables in one URI.
- In case a value happens to contain special characters, **it's good to always _URL encode_ values**. If a value contains e.g. a space ` `, it should be replaced by `%20`, so for example `My value` would become `My%20value` . A full URL could be: `obsidian://shell-commands/?vault=VAULTNAMEHERE&_my_custom_variable=My%20value` . URL encoding is needed, because special characters (such as a space) might otherwise cut the value text in half, ignoring the right side part, or causing other side effects. URL encoding is easy to do using an online service such as [urlencoder.io](https://www.urlencoder.io/). Just note that you must only to encode a _value_, **not** the custom variable *name* nor an equal sign `=` between the *name* and the *value*.
- After the shell command is executed, any assigned custom variables will **keep their assigned values** until Obsidian is closed (or new values are assigned to them). This means that you can pass values to custom variables via URIs, and reuse them later in the same shell command (by executing it e.g. via Obsidian's command palette) or in other shell commands.
- You can also create URIs that only assign values to custom variables, *but do not execute any shell command*. An example: `obsidian://shell-commands/?vault=VAULTNAMEHERE&_custom_variable1=first-value&_custom_variable2=second-value`. This makes it possible to first pass in some data to wait for processing, and then execute a shell command that utilizes the data later in a second step.

> [!INFO] Background
> The PDF example above is based on a real world use case described by [@hakonhagland](https://github.com/hakonhagland) in [this discussion in the *Shell commands* plugin's GitHub repository](https://github.com/Taitava/obsidian-shellcommands/discussions/193). The use case was the original trigger for me to create the Shell commands URI ability in the first place, and [[Custom variables|custom variables]] was a crucial feature to support in it.

# Alternative: [Obsidian Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri)
Shell commands can also be executed using the [Obsidian Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) community plugin for Obsidian. Before SC version `0.13.0`, this was the only way to execute shell commands via links, and so [some examples in the GitHub repository of SC](https://github.com/Taitava/obsidian-shellcommands/discussions/193#discussioncomment-2496001) still show how to use the Obsidian Advanced URI to execute shell commands.

I'm not going into huge details on how to use the Obsidian Advanced URI plugin here, but I'll cover shortly how you can create links that utilize it. There are two ways:
1. The easiest way is to use the [*Copy URI for command* helper provided by Obsidian Advanced URI](https://vinzent03.github.io/obsidian-advanced-uri/tips/helper_commands).
2. You can generate the URI manually using the following base structure:
	- `obsidian://advanced-uri?vault=VAULTNAMEHERE&commandid=obsidian-shellcommands%253Ashell-command-SHELLCOMMANDIDHERE`
	- Please replace `VAULTNAMEHERE` with your Obsidian vault folder's name. Note that you need to [URL encode any possible special characters](https://vinzent03.github.io/obsidian-advanced-uri/concepts/encoding), including spaces.
	- Please replace `SHELLCOMMANDIDHERE` with an id of the shell command you want. You can find the id by opening up the shell command's settings modal and going to the *General* tab. There you'll find a *Shell command id:* text.

> [!SUMMARY] Differences between *Shell commands URI* and *Obsidian Advanced URI*
> - Shell commands URI is a bit shorter than Obsidian Advanced URI, e.g.
> 	- `obsidian://shell-commands/?vault=Shell%20commands%20test&execute=0` vs.
> 	- `obsidian://advanced-uri?vault=Shell%20commands%20test&commandid=obsidian-shellcommands%253Ashell-command-0`
> - Obsidian Advanced URI cannot work if a shell command is [[Events - general principles#^exlude-from-command-palette|completely excluded from Obsidian's command palette]]. However, it can work if hotkeys are enabled. Shell commands URI works also for excluded shell commands.
> - Obsidian Advanced URI does not support passing custom data to shell commands, because this kind of general value arguments are not supported by Obsidian's command palette. Shell commands URI allows assigning values to [[Custom variables|custom variables]], which is a concept only present in the *Shell commands* plugin's scope, not in Obsidian in general.
> - **Shell commands URI does not support opening a specific file before executing a shell command**, which is [supported by Obsidian Advanced URI](https://vinzent03.github.io/obsidian-advanced-uri/actions/navigation). This support might be added to Shell commands URI later.

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2024--): Changing custom variable values via Shell commands URI now [[Custom variables#Show notifications when values change|displays a notification balloon (configurable)]]. ([#382](https://github.com/Taitava/obsidian-shellcommands/issues/382)).
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28): The support for shell command URI was released. ([#202](https://github.com/Taitava/obsidian-shellcommands/issues/202)).

> [!page-edit-history]- Page edit history: 2022-04-30 &#10132; 2024-01-20
> - [<small>2024-01-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/14f72e02f10127df4aef4661a14386d91a1217a7): [[Custom variables]] now display a notification when their values change.
> - [<small>2023-01-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/32c776f8ac8c22351a3e196870710c8ca28db06b): Shell commands URI.md: Mention that custom variable values should be URL encoded.
> - [<small>2023-01-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/17ef77d1c58167bab865a661e4809e7141c9838b): Shell commands URI.md: Update ID information.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-08</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/341e9f4cde907eafe165b724c28559df5f1ef68d): Shell commands URI: Mention Ctrl + clicking the copy button.
> - [<small>2022-04-30</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/1435534a8ba1bc862237cd5c067b5c0ce07b35c4): Shell commands URI.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Basic%20usage/Shell%20commands%20URI.md).
> ^page-edit-history