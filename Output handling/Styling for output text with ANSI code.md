
> [!INFO] 
> Shell programs may output ANSI code to apply <span style="color: magenta">colors</span>, <strong>font</strong> <em>styles</em> and other formatting (e.g. links) to the outputted text. If turned on, possible ANSI code occurrences are converted to HTML elements using <a href="https://github.com/drudru/ansi_up">ansi\_up.js</a> library (bundled in this plugin). Otherwise, possible ANSI code is displayed as-is, which may look ugly.
> <small>(From the _Shell commands_ plugin's settings)</small>


> [!QUOTE] From [Wikipedia: ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code):
> **ANSI escape sequences** are a standard for [in-band signaling](https://en.wikipedia.org/wiki/In-band_signaling "In-band signaling") to control cursor location, color, font styling, and other options on video [text terminals](https://en.wikipedia.org/wiki/Text_terminal "Text terminal") and [terminal emulators](https://en.wikipedia.org/wiki/Terminal_emulator "Terminal emulator"). Certain sequences of [bytes](https://en.wikipedia.org/wiki/Byte "Byte"), most starting with an [ASCII escape](https://en.wikipedia.org/wiki/Escape_character#ASCII_escape_character "Escape character") character and a [bracket](https://en.wikipedia.org/wiki/Bracket "Bracket") character, are embedded into text. The terminal interprets these sequences as commands, rather than text to display verbatim.

(The _Shell commands_ plugin does not support cursor location controlling.)

## Example of ANSI code

On Windows [[PowerShell]], the following (non-existing) command outputs an error message to _standard error_ (`stderr`):

```powershell
CommandThatDoesNotExist
```

> [!QUOTE] Output with text styling enabled:
> <span style="font-weight:bold;color:rgb(187,0,0)">CommandThatDoesNotExist: </span><span style="font-weight:bold;color:rgb(187,0,0)">The term 'CommandThatDoesNotExist' is not recognized as a name of a cmdlet, function, script file, or executable program.</span>
> <span style="font-weight:bold;color:rgb(187,0,0)">Check the spelling of the name, or if a path was included, verify that the path is correct and try again.</span>

In this particular example, the ANSI code handling changes the output text's color to red. While a red color might not be anything amazing, it fixes a problem that would occur if ANSI code was left completely unhandled:

> [!QUOTE] Output with text styling disabled:
> [31;1mCommandThatDoesNotExist: [31;1mThe term 'CommandThatDoesNotExist' is not recognized as a name of a cmdlet, function, script file, or executable program.[0m
> [31;1m[31;1mCheck the spelling of the name, or if a path was included, verify that the path is correct and try again.[0m

With text styling disabled, the error message is much harder to read.
# Configure text styling (aka ANSI code handling)
1. Go to the plugin's settings panel.
2. Look for the shell command that you want to configure, and click the *Stdout/stderr handling, Ignore errors* icon next to it:
  ![[Settings-main-click-output-channels-icon.png]]
  
3. A *modal* opens up. In the modal, look for *Detect colors, font styles etc. in output (ANSI code)*. You'll find dropdown menus that allow you to enable or disable the feature for _standard output_ and _standard error_ separately:
    ![[Settings-modal-output.png]]

# History
- [0.20.0 - 2023-06-25](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#0200---2023-06-25): Support for ANSI code handling was created ([#329](https://github.com/Taitava/obsidian-shellcommands/issues/329)).
