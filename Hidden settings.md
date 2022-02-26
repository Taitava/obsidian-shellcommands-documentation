# Hidden settings
There are a couple of settings that do not have a visible field in the settings view, due to the fact that the settings are usually not needed to be changed, or for me not being able to decide a good location for the settings in the user interface.

## How to access the hidden settings
1. Close Obsidian.
2. Go to the folder `.obsidian/plugins/obsidian-shellcommands`.
3. Open `data.json` file in a text editor application.
4. Do your edits, but be really careful not to break the format of the file. The *Shell commands* plugin is unable to load an incorrectly formatted settings file.
5. Close the text editor and then start Obsidian again.

## A list of hidden settings
- `debug`: Can be `true` or `false`. If true, the following features are enabled:
	- The *Shell commands* plugin will log debugging information into a console, which you can open up by pressing `Ctrl`/`Cmd` + `Shift` + `I`. This is good in case if you encounter some kind of crash or bug and want to report it. You can then report these debug loggins.
	- A special variable named `{{passthrough:argument}}` becomes available. Although I said *special*, it's not actually so special: It just returns the same text that it received as `argument`. It's used for testing escaping special characters in variable values, and it doesn't probably have any benefit to be used in real world situations. It might also be modified or removed in future versions without prior notice.
- `obsidian_command_palette_prefix`: A `string`. Defines a text that will be inserted in Obsidian's *command palette* before each shell command's [[alias]] or the actual command text.
- `settings_version`: This is not really a setting, as **it should not be changed** manually! This value tells the *Shell commands* plugin what format was used to save the settings. Again, do not change this value yourself! 🙂

# History
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26): `obsidian_command_palette_prefix` was created. ([#164](https://github.com/Taitava/obsidian-shellcommands/issues/164)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): `settings_version` was created. ([#90](https://github.com/Taitava/obsidian-shellcommands/issues/90)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): `debug` was created. ([#69](https://github.com/Taitava/obsidian-shellcommands/issues/69)).
