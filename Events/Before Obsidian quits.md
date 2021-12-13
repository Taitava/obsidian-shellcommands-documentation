## Executed when
- User has commanded Obsidian to quit or restart. Execution is not guaranteed, as Obsidian might close even before the shell command execution. Even more likely is that there is no time to do output handling. There's no way for a shell command to make Obsidian wait or cancel from quitting.
- Executed even when another vault is still left open.