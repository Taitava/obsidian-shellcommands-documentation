#! /usr/bin/python3
import os
import re
from updateTimestamp import updateTimestamp

excludeFolders = {"Assets"}
countUpdatedFiles = 0
for root, subdirectories, fileNames in os.walk(".", topdown=True):
    # Exclude all directories starting with a dot, i.e. .obsidian, .git, and .idea
    subdirectories[:] = [subdirectory for subdirectory in subdirectories if not re.search(r"^\.", subdirectory) and not subdirectory in excludeFolders]

    for fileName in fileNames:
        if re.search(r".md$", fileName, re.IGNORECASE):
            filePath = os.path.join(root, fileName)
            # print("Updating timestamp on file: " + filePath)
            if updateTimestamp(filePath):
                countUpdatedFiles += 1
print("Updated timestamps on " + str(countUpdatedFiles) + " files.")