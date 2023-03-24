---
cssclass: customiseTitle
---
# Upgrading the plugin
Upgrades can be installed easily from within Obsidian - [[#How to upgrade|see instructions]].

## Easy to predict change types from version numbers
The *Shell commands* plugin uses [Semantic Versioning](https://semver.org) when developing new releases. Shortly, it means that given a version number *major.minor.patch*:
- The *major* version number is increased when backwards incompatible changes are made\**, that will probably require a user to modify their shell commands or other settings to make them work like they did before.
- The *minor* version number is increased when new features as added, while maintaining backwards compatibility\**. Users should be able to upgrade these versions easily.
- The *patch* version number is increased when backwards compatible bug fixes are done.

\*) Exception: in the `0.x.y` era, _minor_ version upgrades may add backwards incompatible changes.

## How to upgrade
1. Open up Obsidian settings and go to the *Community plugins* tab:
	![[Settings-community-plugins.png]]
2. Click the *Check for updates* button.
3. If an upgrade is available, you should see an *Update* button next to *Shell commands*:
  ![[Settings-community-plugins-update-shell-commands.png]]
4. Click the button and Obsidian will do the rest.

### Automatic backups of settings after an upgrade
The *Shell commands* plugin creates a backup file of its setting after each upgrade from version `0.7.0` onward. To learn more, see [[Settings backups#Automatic backups after SC version upgrades]].

# Downgrading the plugin

There might be situations where you'd like to downgrade the *Shell commands* plugin to an older version. Usually it's because of some problem that has come with a new version of SC, that has not yet been fixed by a *patch* version.

## Check that you have an older version of `data.json` available
Obsidian does not provide a way to install older versions of plugins, but you can do it manually. But before starting the downgrading process, let's first discuss shortly about `data.json` settings file's version compatibility:
- The *Shell commands* plugin stores it's settings in the following file: `.obsidian/plugins/obsidian-shellcommands/data.json`.
- Many times, new versions of SC introduce changes to the structure of the settings file. New versions of SC can read old versions of the settings file and convert it to a new format, but an old version of SC can never know how to read a settings file whose format is newer.
- For this incompatibility reason, you need to make sure that you will have a backup of `data.json` that is of a version equal to the version you are downgrading to, or older it. For example, if you want to downgrade SC from version `0.9.0` to `0.8.0`, you'll need to have a `data.json` file whose `settings_version` field indicates version `0.8.0` or older. A `settings_version` of `0.7.0` is suitable too, because it's older than `0.9.0`, which means that `0.9.0` can read `0.7.0` settings files.
- You can look for [[Settings backups|backup files]] in your `.obsidian/plugins/obsidian-shellcommands` folder to see if there's a compatible backup of your `data.json` file, but keep in mind that it might be old and maybe does not contain your latest settings changes.
- If you do not have a compatible `data.json` settings file available, you need to skip the part where you would copy your current `data.json` over to the downgraded version of SC. In this case, you will need to define all your shell commands again from the scratch. However, you can open up an incompatible `data.json` file in a text editor and see if you are able to copy and paste shell commands from there manually.

Now that you are aware of the `data.json` incompatibility issue, you can start the actual downgrading process.

## Start downgrading
1. Quit Obsidian.
2. Go to folder `.obsidian/plugins`.
3. Rename the `obsidian-shellcommands` folder to `obsidian-shellcommands-disabled`. Do not remove the folder (at least yet), you'll need the `data.json` file from there later.
4. Create a new, empty folder named `obsidian-shellcommands`.
5. Old versions of SC need to be downloaded manually from GitHub using a web browser. Go to the following address: https://github.com/Taitava/obsidian-shellcommands/releases
6. Locate the version of SC you want to downgrade to on the above-mentioned page. In this example, we're going to use `0.8.0`, but you can use something else, too.
7. Click *Assets* below the version you've chosen.
8. Click and download each of the following files to the newly created `obsidian-shellcommands` folder:
	- `main.js`
	- `manifest.json`
	- `styles.css`
	- Do not download *Source code*! You will not need it, and it would only contain a ton of files that would just make you confused.
9. From the old `obsidian-shellcommands-disabled` folder, copy a settings file that you know to be compatible with the version of SC you have chosen to downgrade to, to the new `obsidian-shellcommands` folder next to the three other files.
10. Launch Obsidian. Check that everything works okay!

# History


> [!page-edit-history]- Page edit history: 2021-11-25 &#10132; 2021-11-25
> - [<small>2021-11-25</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/3ff17d13c815a111e48ab5d2ced7a084fce0b280): Instructions to downgrade the plugin.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/./Upgrading%20%28and%20downgrading%29.md).
> ^page-edit-history