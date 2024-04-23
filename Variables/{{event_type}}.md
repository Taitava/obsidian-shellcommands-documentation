---
cssclasses:
  - customiseTitle
aliases:
  - "{{event_type:category}}"
---
> [!Warning] This feature is only available in a beta test
> - [Participate in the test](https://github.com/Taitava/obsidian-shellcommands/discussions/391).
> %% #TODO: Remove this annotation when the final version is released. %%

# Variable: `{{event_type}}` or `{{event_type:category}}`
> [!Quote] {{event_type}} described in the *Shell commands* plugin's settings
> Tells which event was triggered.

The variable has two modes:
- `{{event_type}}`: Gives an explicit name for the event that executed the shell command.
- `{{event_type:category}}`: Gives a name of the category under which the event belongs that executed the shell command.
## Possible values
| Event | `{{event_type}}` | `{{event_type:category}}` |
| ---- | ---- | ---- |
| [[Caret moved in editor]] | `caret-moved` | `editor` |
| [[Every n seconds]] | `every-n-seconds` | `time` |
| [[Obsidian quits]] | `application-quit` | `application` |
| [[Obsidian starts]] | `application-started` | `application` |
| [[Switching the active pane]] | `active-leaf-switched` | `workspace` |
| **Menu events** |  |  |
| [[Editor menu]] | `editor-menu-item` | `menu` |
| [[File menu]] | `file-menu-item` | `menu` |
| [[Folder menu]] | `folder-menu-item` | `menu` |
| **File system events** |  |  |
| [[File content modified]] | `file-content-modified` | `file` |
| [[File created]] | `file-created` | `file` |
| [[File deleted]] | `file-deleted` | `file` |
| [[File moved]] | `file-moved` | `file` |
| [[File renamed]] | `file-renamed` | `file` |
| [[Folder created]] | `folder-created` | `folder` |
| [[Folder deleted]] | `folder-deleted` | `folder` |
| [[Folder moved]] | `folder-moved` | `folder` |
| [[Folder renamed]] | `folder-renamed` | `folder` |

## When to use

`{{event_type}}` and `{{event_type:category}}` are handy if a shell command uses multiple [[Events - general principles|events]], and it's needed to know which event was actually triggered.

> [!Example]
> Consider that a shell command uses all the file system events:  [[File content modified]], [[File created]], [[File deleted]], [[File moved]], [[File renamed]], [[Folder created]], [[Folder deleted]], [[Folder moved]], [[Folder renamed]].
> With `{{event_type}}`, it's easy to check if the triggering change in file system was about a file **content** change, or about a path change.
> ```bash
> if [ {{event_type}} = "file-content-modified" ]
> then
>     echo "File content has changed."
> else
>     echo "Either a file or folder has been created, moved, renamed or deleted."
> fi
> ```
> 
> With `{{event_type:category}}`, it's possible to do sparse categorization of events, without a need to list each event type explicitly:
> ```bash
> if [ {{event_type:category}} = "file" ]
> then
>     echo "A file has been created, modified, moved, renamed or deleted."
> elif [ {{event_type:category}} = "folder" ]
> then
>     echo "A folder has been created, moved, renamed or deleted."
> fi
> ```
# Availability
> [!Warning] Only available:
> In all events.

# History
- #TODO: Add a date [0.22.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2022--): The variable was released. ([#394](https://github.com/Taitava/obsidian-shellcommands/issues/394)).

> [!page-edit-history]- Page edit history: 2024-02-10 &#10132; 2024-02-10
> - [<small>2024-02-10</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/0ef4d4c717223599d69d32a92845bef694925026): Documentation for [[{{event_type}}]] variable.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/%7B%7Bevent_type%7D%7D.md).
> ^page-edit-history