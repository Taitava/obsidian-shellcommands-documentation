#! /usr/bin/python3
import re
import sys
import subprocess
import urllib.parse


class UpdateFooterException(Exception):
    pass


def updateFooter(filePath: str):
    # Get the creation and modification dates from git (if possible)
    gitLogOutput = subprocess.run([
        "git",
        "log",
        "--grep=\\[IgnoreHistory\\]", # Exclude commits whose commit message contains [IgnoreHistory]
        "--invert-grep",              # Makes it exclusive instead of inclusive.
        "--regexp-ignore-case",       # No need to be careful with casing when writing [IgnoreHistory] to commit messages.
        "--follow",
        "--format=%ad|%H|%s",
        "--date",
        "format:%Y-%m-%d",
        filePath
    ], stdout=subprocess.PIPE).stdout.decode("utf-8").strip('\n')
    if re.match(r"^(\d{4}-\d{2}-\d{2})", gitLogOutput):
        # Git was able to find dates
        gitCommits = gitLogOutput.split('\n')
        modificationDate = gitCommits[0].split("|")[0]
        creationDate = gitCommits[-1].split("|")[0]
        gitCommitsMarkdown = parseCommitList(gitCommits)
    else:
        # Git did not find dates for the file, so the file is not in git yet.
        raise UpdateFooterException(filePath + ":\n    - Unable to generate a footer because the file doesn't seem to be committed to git.")

    # Read the file in memory
    try:
        with open(filePath, "r", newline="\n") as readFile:
            fileContent = readFile.read()
    except UnicodeDecodeError:
        # Something went wrong.
        # Cancel updating.
        raise UpdateFooterException(filePath + ":\n    - Unicode decoding failed. Does the file contain emojis? :-)")

    # Generate footer message
    filePathUrlEncoded = urllib.parse.quote(filePath.replace("\\", "/"), safe="/")
    historyContent = f"""> [!page-edit-history]- Page edit history: {creationDate} &#10132; {modificationDate}
{gitCommitsMarkdown}
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/{filePathUrlEncoded}).
> ^page-edit-history"""

    # Change or add a footer in the content
    regexPattern = r"^\> \[\!page\-edit\-history\].*?\> \^page\-edit\-history"
    regexModifiers = re.MULTILINE | re.DOTALL
    if re.search(regexPattern, fileContent, regexModifiers):
        # A previous block exists.
        fileContent = re.sub(regexPattern, historyContent, fileContent, flags=regexModifiers)
    else:
        # No previous block exists yet - add one.
        # Check should "History" heading be added, too.
        if re.search(r"^# History", fileContent, regexModifiers):
            # "History" heading exists already.
            historyHeading = ""
        else:
            # "History" heading needs to be added.
            historyHeading = "# History\n"

        fileContent = fileContent + "\n\n" + historyHeading + historyContent

    # Write the modified file
    with open(filePath, "w", newline="\n") as writeFile:
        writeFile.write(fileContent)

def parseCommitList(gitCommits):
    list = ""
    for gitCommit in gitCommits:
        if list != "":
            list += "\n"
        [date, hash, comment] = gitCommit.split("|")
        list += f"> - [<small>{date}</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/{hash}): {comment}"
    return list

if __name__ == "__main__":
    countNeededArguments = 1
    if len(sys.argv) - 1 != countNeededArguments:
        sys.exit("This script requires " + str(countNeededArguments) + " arguments: a file path.")

    filePath = sys.argv[1]
    try:
        updateFooter(filePath)
        # All is done.
        print("Footer is updated.")
    except UpdateFooterException as exception:
        # Something went wrong.
        # Show the error message.
        sys.exit(exception)
