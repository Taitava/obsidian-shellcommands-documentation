## What is Flatpak?

> [!Quote]  From [Wikipedia](https://en.wikipedia.org/wiki/Flatpak)
> **Flatpak**, formerly known as [xdg](https://en.wikipedia.org/wiki/Freedesktop.org "Freedesktop.org")-app, is a [utility](https://en.wikipedia.org/wiki/Software_utility "Software utility") for [software deployment](https://en.wikipedia.org/wiki/Software_deployment "Software deployment") and [package management](https://en.wikipedia.org/wiki/Package_management "Package management") for [Linux](https://en.wikipedia.org/wiki/Linux). It is advertised as offering a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security) "Sandbox (computer security)") environment in which users can run [application software](https://en.wikipedia.org/wiki/Application_software "Application software") in isolation from the rest of the system.
> 
> <small>Cited on 2023-12-23.</small>

On Linux, [one way to install Obsidian is by using Flatpak](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian#Install+Obsidian+using+Flatpak).

## Flatpak installation may cause execution failures

Flatpak creates an isolated environment for Obsidian, which can lead to situations where Obsidian (and the SC plugin) is not able to execute external programs (files are not found even though they are present in the filesystem), or the program versions are different from expected.

> [!Quote] From [docs.flatpak.org](https://docs.flatpak.org/en/latest/sandbox-permissions.html)
> One of Flatpak’s main goals is to increase the security of desktop systems by isolating applications from one another. This is achieved using sandboxing and means that, by default, applications that are run with Flatpak have extremely limited access to the host environment.
> 
> <small>Cited on 2023-12-23.</small>

Generally speaking, sandboxing makes a lot of sense as it increases application security. That said, it can often prevent shell command execution from Obsidian.

> [!Failure] Reported problems that have happened with Flatpak installations:
> - [Old Python version 3.9 is executed instead of 3.10](https://github.com/Taitava/obsidian-shellcommands/discussions/225) (reported on 2022-05-20).
> - [`gedit`, `drawio`, and `thunderbird` commands are not found](https://github.com/Taitava/obsidian-shellcommands/discussions/367) (reported on 2023-08-23).

## Solutions

> [!Success] Configure Flatpak's sandbox permissions
> I haven't tested this myself yet, but at least the "file not found" type of problems might be solvable by configuring Flatpak to give Obsidian more permissions to needed directories. [Sandbox Permissions on docs.flatpak.org](https://docs.flatpak.org/en/latest/sandbox-permissions.html).

> [!Success] Reinstall Obsidian using a different method
> If you are unable to configure Flatpak to allow access to external programs, you can reinstall Obsidian using the following alternative methods for Linux:
> - [Install Obsidian using Snap](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian#Install+Obsidian+using+Snap)
> - [Install Obsidian using AppImage](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian#Install+Obsidian+using+AppImage)

## A warning is shown if Obsidian has been installed using Flatpak
From SC version `0.21.0` onwards, the plugin can detect if Obsidian has been installed using Flatpak. If so, the following warning will be shown in the plugin's settings:
![[Settings-main-Flatpak-warning.png]]

(Under the hood, the detection happens by [checking whether an environment variable named `container` is defined](https://github.com/Taitava/obsidian-shellcommands/blob/baaf74c166bd4feb8c89e794d711a7a73ea847b6/src/Common.ts#L101-L117)).

> [!Tip] Disable the warning
> If you want to continue using Flatpak, you can disable the warning:
> 1. Quit Obsidian.
> 2. Open up the `.obsidian/plugins/obsidian-shellcommands/data.json` settings file in a text editor.
> 3. Find [[Hidden settings#^show-installation-warnings|a hidden setting named "show_installation_warnings"]] and change its value from `true` to `false`.
> 4. Save the file and reopen Obsidian. If you open up the SC plugin's settings panel, there should not be a warning anymore.

# History
- [0.21.0 - 2023-12-30](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0210---2023-12-30): Flatpak warning was added to the plugin's settings panel. ([#368](https://github.com/Taitava/obsidian-shellcommands/issues/368)).

> [!page-edit-history]- Page edit history: 2023-12-23 &#10132; 2023-12-23
> - [<small>2023-12-23</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/d586cb48e0b834224852c911bfda24b1d3168991): Create [[Flatpak installation.md]].
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Problems/Flatpak%20installation.md).
> ^page-edit-history