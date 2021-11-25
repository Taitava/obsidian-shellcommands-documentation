---
aliases:
  - Ignore
---
# Output channel: Ignore
Simply hides the output, doing nothing with it. This is the default for all commands' `stdout` output, because for many commands, the normal output is not so important. E.g. when creating a folder, launching an application or modifying a file - in these cases, the lack of error messages is usually enough to tell that the command executed successfully.

## History
- [0.5.0 - 2021-10-02](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#050---2021-10-02): The output channel was created. ([#34](https://github.com/Taitava/obsidian-shellcommands/issues/34)).