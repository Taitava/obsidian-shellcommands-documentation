# Example: Watch cat videos on YouTube after closing Obsidian

A long day behind and you need some relaxation after finally being able to stop working? This example will cheer you up by presenting a simple shell command that serves you lovely cat videos every time you close Obsidian. 😸👍

1. [[How to define shell commands|Create a new shell command]]. You will find a shell command you can use on your particular operating system below.
2. Go to [[Events - general principles|event settings]].
3. Enable the [[Obsidian quits]] event. 

## Windows
- `start https://www.youtube.com/results?search_query=cat+videos`

## Linux
- `xdg-open "https://www.youtube.com/results?search_query=cat+videos"`.

## Macintosh
- `open "https://www.youtube.com/results?search_query=cat+videos"`.