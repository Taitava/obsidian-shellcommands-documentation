---
aliases:
  - "Notification balloon"
  - "Error balloon"
---

# Output channel: Notification/Error balloon
 
  A temporary message balloon that pops up in the top right corner of the Obsidian window. This is the default for all commands' `stderr` output.
 
 ![[Output-notification-and-error-balloons.png]]
 You can identify an *error balloon* by the brackets `[` `]` preceding the output message. The brackets indicate the exit code (aka error number) that the shell command returned at the end, e.g. *0* in the image above. A *notification balloon* does not have the brackets nor an exit code.
 
 **Good for**: Short output that can be discarded after a short period of time. Suits for  a small amount of multi line output, too.
 
 You can customize for how long *notification balloons* and *error balloons* are visible in the plugin's settings panel (in *Output* tab):
 ![[Settings-main-output-tab.png]]