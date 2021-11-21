#TODO:
- data.json backups - the automatic backup + mention that a user should take their own backups.
- How to downgrade if problems occur.

# Upgrading
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
 