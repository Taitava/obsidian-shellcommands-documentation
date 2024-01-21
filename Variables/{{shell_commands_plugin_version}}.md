---
cssclasses:
  - customiseTitle
---
# Variable: `{{shell_commands_plugin_version:plugin}}`, `{{shell_commands_plugin_version:plugin:major|minor|patch}}`, `{{shell_commands_plugin_version:settings}}`, or `{{shell_commands_plugin_version:settings:major|minor|patch}}`
> [!Quote] {{shell_commands_plugin_version}} described in the *Shell commands* plugin's settings
> Gives the plugin's version or settings structure version.

> [!Info] Two slightly deviating version numbers
> The _Shell command_ plugin uses two version numbers, _plugin version_ and _settings version_.
> - _Plugin version_ is the normal release version of the plugin.
> - _Settings version_ is stored in `.obsidian/plugin/obsidian-shellcommands/data.json` and it tells which settings **format** version was used to save the file.
>     - It does not, however, tell exactly which version of the plugin saved the file. It only tells the settings format.
>     - Often the _settings version_ is the same as the _plugin version_, but in case a new _plugin version_ does not introduce any changes to the settings file format, then the _settings version_ **is not** raised with the _plugin version_. For instance, _patch_ releases do not usually need to raise the _settings version_.
> - The first argument (`plugin` / `settings`) is used to select which one is wanted.

## Getting just one part of the version

- `{{shell_commands_plugin_version:plugin}}` or `{{shell_commands_plugin_version:settings}}` gives you the whole version number, e.g. `0.22.1`.
- `{{shell_commands_plugin_version:plugin:major}}` gives you the first number of the version, e.g. `0` from `0.22.1`.
- `{{shell_commands_plugin_version:plugin:minor}}` gives you the second number of the version, e.g. `22` from `0.22.1`.
- `{{shell_commands_plugin_version:plugin:patch}}` gives you the third number of the version, e.g. `1` from `0.22.1`.
- The same applies for `{{shell_commands_plugin_version:settings}}`.

> [!Info] Terms _major_, _minor_, and _patch_
 The terms _major_, _minor_, and _patch_ come from [Semantic Versioning](https://semver.org).

## The _Shell commands_ plugin uses Semantic Versioning

![[Upgrading (and downgrading)#Easy to predict change types from version numbers]]
# Availability

> [!Success] This variable is always available.
# See also
- [[{{obsidian_api_version}}]]

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was promoted, so it doesn't require debug mode anymore. ([#387](https://github.com/Taitava/obsidian-shellcommands/issues/387)).
    - It was also renamed from `{{shell_commands_plugin:plugin-version}}`/`{{shell_commands_plugin:settings-version}}` to `{{shell_commands_plugin_version:plugin}}`/`{{shell_commands_plugin_version:settings}}`.
    - It's now also possible to get just a part of the version by a new argument `:major` / `:minor` / `:patch`.
- [0.20.0 - 2023-06-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0200---2023-06-25): The variable became available in debug mode only by the name `{{shell_commands_plugin:plugin-version}}`/`{{shell_commands_plugin:settings-version}}` ([#341](https://github.com/Taitava/obsidian-shellcommands/issues/341)).
