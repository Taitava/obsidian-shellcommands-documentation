---
cssclasses:
  - customiseTitle
---

> [!Warning] This variable is only available in a beta test
> - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/391).
> %% #TODO: Remove this annotation when the final version is released. %%

# Variable: `{{obsidian_api_version}}` or `{{obsidian_api_version:major|minor|patch}}`
> [!Quote] {{obsidian_api_version}} described in the *Shell commands* plugin's settings
> Gives Obsidian's API version, which follows the release cycle of the desktop application.

> [!Question] What does it mean that it's the _API_ version?
> To my understanding, Obsidian's API version seems to be the same as Obsidian's desktop application's release version. The version information is retrieved from [the `apiVersion` variable in Obsidian's API](https://github.com/obsidianmd/obsidian-api/blob/da7309d0f22c073ca6eb0fe95c0eeee055a235a7/obsidian.d.ts#L369-L374), and I do not know if the API version can differ from the release version of Obsidian in any way. 

## Getting just one part of the version

- The base form of the variable (`{{obsidian_api_version}}`) gives you the whole version number, e.g. `1.5.3`.
- `{{obsidian_api_version:major}}` gives you the first number of the version, e.g. `1` from `1.5.3`.
- `{{obsidian_api_version:minor}}` gives you the second number of the version, e.g. `5` from `1.5.3`.
- `{{obsidian_api_version:patch}}` gives you the third number of the version, e.g. `3` from `1.5.3`.

> [!Info] Terms _major_, _minor_, and _patch_
 The terms _major_, _minor_, and _patch_ come from [Semantic Versioning](https://semver.org), even though I haven't seen Obsidian developers making a statement if they're using the Semantic Versioning scheme or not. I assume Obsidian is not using it, but as SemVer is familiar to many programmers, I decided to use those three terms here. Also, they are in line with the [[{{shell_commands_plugin_version}}]] variable.

# Availability

> [!Success] This variable is always available.
# See also
- [[{{shell_commands_plugin_version}}]]

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was promoted, so it doesn't require debug mode anymore. ([#387](https://github.com/Taitava/obsidian-shellcommands/issues/387)).
    - It was also renamed from `{{obsidian_api:version}}` to `{{obsidian_api_version}}`.
    - It's now also possible to get just a part of the version by a new argument `:major` / `:minor` / `:patch`.
- [0.20.0 - 2023-06-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0200---2023-06-25): The variable became available in debug mode only by the name `{{obsidian_api:version}}` ([#341](https://github.com/Taitava/obsidian-shellcommands/issues/341)).


> [!page-edit-history]- Page edit history: 2024-01-21 &#10132; 2024-01-21
> - [<small>2024-01-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/a94285bc786c5c827a89adb660162cb1f8f7bee0): Create [[{{obsidian_api_version}}.md]] and [[{{shell_commands_plugin_version}}.md]].
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Variables/%7B%7Bobsidian_api_version%7D%7D.md).
> ^page-edit-history