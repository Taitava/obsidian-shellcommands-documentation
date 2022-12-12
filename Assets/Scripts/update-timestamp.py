#! /usr/bin/python3
import re
import sys
import subprocess

countNeededArguments = 1
if len(sys.argv)-1 != countNeededArguments:
    sys.exit("This script requires "+str(countNeededArguments)+" arguments: a file path.")

filePath = sys.argv[1]

# Get the creation and modification dates from git (if possible)
gitLogOutput = subprocess.run(["git", "log", "--follow", "--format=%ad", "--date", "format:%Y-%m-%d", filePath], stdout=subprocess.PIPE).stdout.decode("utf-8").strip('\n')
if re.match(r"^(\d{4}-\d{2}-\d{2})", gitLogOutput):
    # Git was able to find dates
    gitDates = gitLogOutput.split('\n')
    modificationDate = gitDates[0]
    creationDate = gitDates[-1]
else:
    # Git did not find dates for the file, so the file is not in git yet.
    sys.exit("Unable to generate timestamp for file '"+filePath+"' because it doesn't seem to be committed to git.")

# Read the file in memory
with open(filePath, "r", newline="\n") as readFile:
    fileContent = readFile.read()

# Change or add a timestamp in the content
newTimestamp = "<small>This page was last modified on <strong>" + modificationDate + "</strong> and created on " + creationDate + ".</small>\n" # Use <strong> instead of ** because ** doesn't seem to work in Obsidian's markdown when it's contained in a <small> element.
regexPattern = r"(?<=^# History)(?P<middleSpacing>\s+)(<small>[^<]*</small>)?\n?"
regexModifiers = re.MULTILINE | re.DOTALL
if re.search(regexPattern, fileContent, regexModifiers):
    # A History heading exists
    print("Found a history record, updating it.")
    fileContent = re.sub(regexPattern, r"\g<middleSpacing>" + newTimestamp, fileContent, flags=regexModifiers)
else:
    # No History heading exists yet - add one.
    print("Did not find a history record, creating one.")
    fileContent = fileContent + "\n\n# History\n" + newTimestamp

# Write the modified file
with open(filePath, "w", newline="\n") as writeFile:
    writeFile.write(fileContent)