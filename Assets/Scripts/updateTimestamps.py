#! /usr/bin/python3
import os
import re
import sys

from updateTimestamp import updateTimestamp, UpdateTimestampException

excludeFolders = {"Assets"}
excludeFiles = ["Donate.md"]
countUpdatedFiles = 0
countFailedFiles = 0
for root, subdirectories, fileNames in os.walk(".", topdown=True):
    # Exclude all directories starting with a dot, i.e. .obsidian, .git, and .idea
    subdirectories[:] = [subdirectory for subdirectory in subdirectories if not re.search(r"^\.", subdirectory) and not subdirectory in excludeFolders]

    for fileName in fileNames:
        if fileName not in excludeFiles and re.search(r".md$", fileName, re.IGNORECASE):
            filePath = os.path.join(root, fileName)
            filePath = re.sub(r"^.[\\/]", "", filePath) # Remove an unnecessary .\ from the beginning of the path.
            try:
                print("Updating footer: " + filePath + "... ", end="", flush=True)
                updateTimestamp(filePath)
                print("ok.", flush=True)
                countUpdatedFiles += 1
            except UpdateTimestampException as exception:
                # Something went wrong
                # Output the error message, but continue updating other files.
                print("FAILED!", flush=True)
                print(exception, file=sys.stderr, flush=True)
                countFailedFiles += 1
print("Updated timestamps on " + str(countUpdatedFiles) + " files.")
if countFailedFiles > 0:
    sys.exit("Updating failed on " + str(countFailedFiles) + " files.")
