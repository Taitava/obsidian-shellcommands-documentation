#! /usr/bin/python3
import re
import sys
import subprocess
import urllib.parse


class UpdateTimestampException(Exception):
    pass


def updateTimestamp(filePath: str):
    # Get the creation and modification dates from git (if possible)
    gitLogOutput = subprocess.run([
        "git",
        "log",
        "--grep=\\[IgnoreHistory\\]", # Exclude commits whose commit message contains [IgnoreHistory]
        "--invert-grep",              # Makes it exclusive instead of inclusive.
        "--regexp-ignore-case",       # No need to be careful with casing when writing [IgnoreHistory] to commit messages.
        "--follow",
        "--format=%ad",
        "--date",
        "format:%Y-%m-%d",
        filePath
    ], stdout=subprocess.PIPE).stdout.decode("utf-8").strip('\n')
    if re.match(r"^(\d{4}-\d{2}-\d{2})", gitLogOutput):
        # Git was able to find dates
        gitDates = gitLogOutput.split('\n')
        modificationDate = gitDates[0]
        creationDate = gitDates[-1]
    else:
        # Git did not find dates for the file, so the file is not in git yet.
        raise UpdateTimestampException("Unable to generate timestamp for file '" + filePath + "' because it doesn't seem to be committed to git.")

    # Read the file in memory
    try:
        with open(filePath, "r", newline="\n") as readFile:
            fileContent = readFile.read()
    except UnicodeDecodeError:
        # Something went wrong.
        # Cancel updating.
        raise UpdateTimestampException("Unicode decoding failed for file '" + filePath + "'. Does it contain emojis? :-)")

    # Generate timestamp message
    timestampMessage = "This page was last modified on <strong>" + modificationDate + "</strong> and created on " + creationDate + ". " # Use <strong> instead of ** because ** doesn't seem to work in Obsidian's markdown when it's contained in a <small> element.
    filePathUrlEncoded = urllib.parse.quote(filePath.replace("\\", "/"), safe="/")
    timestampMessage += '<a href="https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/' + filePathUrlEncoded + '">See page edit history</a>.'

    # Change or add a timestamp in the content
    newTimestamp = "<small>" + timestampMessage + "</small>\n"
    regexPattern = r"(?<=^# History)(?P<middleSpacing>\s+)(<small>.*?</small>)?\n?"
    regexModifiers = re.MULTILINE | re.DOTALL
    if re.search(regexPattern, fileContent, regexModifiers):
        # A History heading exists
        fileContent = re.sub(regexPattern, r"\g<middleSpacing>" + newTimestamp, fileContent, flags=regexModifiers)
    else:
        # No History heading exists yet - add one.
        fileContent = fileContent + "\n\n# History\n" + newTimestamp

    # Write the modified file
    with open(filePath, "w", newline="\n") as writeFile:
        writeFile.write(fileContent)


if __name__ == "__main__":
    countNeededArguments = 1
    if len(sys.argv) - 1 != countNeededArguments:
        sys.exit("This script requires " + str(countNeededArguments) + " arguments: a file path.")

    filePath = sys.argv[1]
    try:
        updateTimestamp(filePath)
        # All is done.
        print("Timestamp is updated.")
    except UpdateTimestampException as exception:
        # Something went wrong.
        # Show the error message.
        sys.exit(exception)
