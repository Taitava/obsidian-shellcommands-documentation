There are a couple of settings that do not have a visible field in the settings view, due to the fact that the settings are usually not needed to be changed, or for me not being able to decide a good location for the settings in the user interface.

## How to access the hidden settings
1. Close Obsidian.
2. Go to the folder `.obsidian/plugins/obsidian-shellcommands`.
3. Open `data.json` file in a text editor application.
4. Do your edits, but be really careful not to break the format of the file. The *Shell commands* plugin is unable to load an incorrectly formatted settings file.
5. Close the text editor and then start Obsidian again.

## A list of hidden settings
- `approve_modals_by_pressing_enter_key`: Can be `true` (default) or `false`. If `true`, any modals (such as deletion/execution confirmations) can be accepted and closed by pressing the `Enter` key. If you want to avoid accidental approving, set this to `false`. 
- `command_palette` 
    - `re_execute_last_shell_command`
        - `enabled`: A `boolean`. Can be set to `false` to remove the _Re-execute:_ command from Obsidian's *command palette*.
        - `prefix`: A `string`. Defines a text that will be inserted in Obsidian's *command palette* before a re-executable shell command's [[alias]] or the actual command text.
- `debug`: Can be `true` or `false`. If true, the following features are enabled:
	- The *Shell commands* plugin will log debugging information into a console, which you can open up by pressing `Ctrl`/`Cmd` + `Shift` + `I`. This is good in case if you encounter some kind of crash or bug and want to report it. You can then report these debug log records.
	- A special variable named `{{passthrough:argument}}` becomes available. Although I said *special*, it's not actually so special: It just returns the same text that it received as `argument`. It's used for testing escaping special characters in variable values, and it doesn't probably have any benefit to be used in real world situations. It might also be modified or removed in future versions without prior notice.
	- A special variable named `{{newline}}` becomes available. It returns a newline character (`\n`). An optional argument can be defined to tell, how many newlines are needed.
- `max_visible_lines_in_shell_command_fields`: Can be `false` or a number. If it's a number, limit the max height of all shell commands fields in settings. Useful if you want to prevent long scripts from taking up too much screen space. It won't restrict adding more lines to a shell command, it just makes the field to have a scroll bar instead of stretching infinitely. If it's `false` (default), don't limit at all. ^max-visible-lines-in-shell-command-fields
- `obsidian_command_palette_prefix`: A `string`. Defines a text that will be inserted in Obsidian's *command palette* before each shell command's [[alias]] or the actual command text.
- `settings_version`: This is not really a setting, as **it should not be changed** manually! This value tells the *Shell commands* plugin what format was used to save the settings. Again, do not change this value yourself! 🙂
- `show_installation_warnings`: A `boolean`. If `true` (default), the plugin's settings pane can display warnings related to how Obsidian is installed, if the installation may cause known potential problems for shell commands execution. Currently, the only detected situation is if Obsidian is installed using [[Flatpak installation|Flatpak]], which can cause problems. The warnings can be turned off if you prefer not to change your Obsidian installation method and if you can cope with the possible limitations. ^show-installation-warnings

# History
- [0.20.0 - 2023-06-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0200---2023-06-25): _Re-execute_ command was released, with the related hidden settings. ([#354](https://github.com/Taitava/obsidian-shellcommands/issues/354)).
- [0.18.0 - 2023-01-06](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0180---2023-01-06): `{{newline}}` was released. ([#295](https://github.com/Taitava/obsidian-shellcommands/issues/295)).
- [0.13.0 - 2022-06-28](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0130---2022-06-28):
	- `max_visible_lines_in_shell_command_fields` was released. ([#203](https://github.com/Taitava/obsidian-shellcommands/issues/203)).
	- `approve_modals_by_pressing_enter_key` was released. ([#216](https://github.com/Taitava/obsidian-shellcommands/issues/216)).
- [0.11.0 - 2022-02-26](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0110---2022-02-26): `obsidian_command_palette_prefix` was released. ([#164](https://github.com/Taitava/obsidian-shellcommands/issues/164)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): `settings_version` was released. ([#90](https://github.com/Taitava/obsidian-shellcommands/issues/90)).
- [0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): `debug` was released. ([#69](https://github.com/Taitava/obsidian-shellcommands/issues/69)).


> [!page-edit-history]- Page edit history: 2022-02-22 &#10132; 2023-12-21
> - [<small>2023-12-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/71c7bad42976db5b21483e7c5cc45bd05228787c): [[Hidden settings.md]]: Information about `show_installation_warnings` setting.
> - [<small>2023-06-23</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f3ff1611a4c4a370f07fe70a18b7ceea01cba0bc): Hiden settings: Mention "Re-execute" command.
> - [<small>2023-01-06</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/65637e77d4b209f81b215d1f2222bb138b7cbf0c): 0.18.0 is released.
> - [<small>2022-12-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/5fd8e7237b33b273ae2174f19cf47ef8ef915e35): Hidden settings: Mention {{newline}}.
> - [<small>2022-06-28</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/49efe1a5a719cb695cc0a4a96d05c10548298804): 0.13.0 is released.
> - [<small>2022-05-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/bb37c1f8ee6630879a4d6578eae61c50730cda97): 0.13.0-beta.1 annotations.
> - [<small>2022-05-12</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/af84abadcd9066a857fe6c6c52da0a1f2555a9dc): Hidden settings.md: Add 'approve_modals_by_pressing_enter_key'.
> - [<small>2022-05-03</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/8e2b04d58bc91cd7d795b95217fd45c2fc11df2c): Multiline shell commands.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7769b1c47ae8c0709d7631fef285d82c82dcaca7): Hidden settings: Added a missing history record.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d6e852c88fb1ba221140841ea599189a27864a19): 0.11.0 is released.
> - [<small>2022-02-26</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/e5463e54d3424913624f9ebc61fcc7f5dee829cb): 0.11.0 is released.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/84083f0caed7e2a4f427685839ff6422b0901230): Hidden settings: Add information about 'settings_version'.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/7537045e3408a0fa0a1f3b47a62907fc6e4f8ca3): Add annotations regarding 0.11.0-beta.1 test.
> - [<small>2022-02-22</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/fabdd6cf143447380e2f28f92ee7752d169d2554): Create a page for Hidden settings.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Hidden%20settings.md).
> ^page-edit-history