# Settings backups
Heavy users of this plugin may end up defining over 50 shell commands in their settings. It's a ton to remember if it has to be redone due to a hardware failure, corrupted settings file, or other accident. This note will discuss about two ways to to backup - manual and automatic.

## Manual backups are important

The *Shell commands* plugin's settings are stored in a single file: `.obsidian/plugins/obsidian-shellcommands/data.json`. Make sure to include it in your backups every time you back up your vault (you are backing up your vault, are you??). Even if you are doing automatic backups, it's good to check occasionally that the settings file really is included in the backups.

## Automatic backups after SC version upgrades
Every time the *Shell commands* plugin notices that the `data.json` settings file format is for an older version of SC (e.g. after upgrading the plugin), the plugin will automatically create a backup copy of the file in the same folder, and migrate the actual `data.json` file to comply with a new settings file format needed for new features.

Backup file naming logic:
- _data-backup-version-**0.x**-before-upgrading-to-**0.7.0**.json_: Here **0.x** means that the original settings file is from SC version 0.0.0 - 0.6.0. It's marked 0.x because before `0.7.0` the settings files do not have version information available. And the later version number, **0.7.0** in this case, tells before which upgrade this backup file was created.
- _data-backup-version-**0.7.0**-before-upgrading-to-**0.8.0**.json_: This is how the versioning will be in future updates. Here **0.7.0** is the original settings file's version, and **0.8.0** tells before which upgrade this backup was taken.
- (If a backup file already exists with the same name, a new backup file will have `-2` (or `-3` etc.) added to its name.)

These backups are meant to help you in case the migrating process has a bug that corrupts the settings file, or removes data from it. SC's migrations should never affect other settings in Obsidian or other plugins, but you should naturally backup those, too.

**As these backups happen infrequently, it's recommended that you take regular manual backups, too.**

### Restoring settings from a backup after a problematic SC upgrade
If an upgrade caused problems to your SC settings, you should first [[Upgrading (and downgrading)#Downgrading the plugin|downgrade]] the plugin to a previous version that you knew worked correctly, before trying to restore a backup settings file. Otherwise you'll end up running the problematic upgrade migration again.

To restore a backup settings file, do:
1. Quit Obsidian and [[Upgrading (and downgrading)#Downgrading the plugin|downgrade]] the plugin.
2. Go to `.obsidian/plugins/obsidian-shellcommands` folder.
3. Rename `data.json` settings file to something like `problematic-data.json` or something else.
4. Pick a backup file that's named like `data-backup-version-x.x.x-before-upgrading-to-y.y.y.json`, and rename it to `data.json`.
6. Launch Obsidian again and check that everything works.

# History
<small>This page was last modified on <strong>2021-11-25</strong> and created on 2021-11-25. <a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Settings%20backups.md">See page edit history</a>.</small>
[0.7.0 - 2021-11-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#070---2021-11-25): Started making automatic backup of the settings file after upgrades. ([#83](https://github.com/Taitava/obsidian-shellcommands/issues/83)).