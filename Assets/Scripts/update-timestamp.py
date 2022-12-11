#! /usr/bin/python3
import re
import sys
import subprocess
from datetime import date

countNeededArguments = 1
if len(sys.argv)-1 != countNeededArguments:
    sys.exit("This script requires "+str(countNeededArguments)+" arguments: a file path.")

filePath = sys.argv[1]

# Get the current date
currentDate = date.today().isoformat()

# Get the creation date from git (if possible)
gitDates = str(subprocess.run(["git", "log", "--follow", "--format=%ad", "--date", "format:%Y-%m-%d", "--reverse", filePath], stdout=subprocess.PIPE).stdout).strip('\\n')
if re.match(r"^b'(\d{4}-\d{2}-\d{2})", gitDates):
    # Git was able to find dates
    creationDate = re.search(r"^b'(\d{4}-\d{2}-\d{2})", gitDates).group(1)
else:
    # Git did not find a creation date for the file, so the file is not in git yet.
    # Use the current date as the creation date.
    creationDate = currentDate

# Read the file in memory
with open(filePath, "r", newline="\n") as readFile:
    fileContent = readFile.read()

# Change or add a timestamp in the content
newTimestamp = "<small>This page was last modified on " + currentDate + " and created on " + creationDate + ".</small>\n"
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