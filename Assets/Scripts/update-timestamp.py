#! /usr/bin/python3
import re
import sys
import subprocess
from datetime import date

count_needed_arguments = 1
if len(sys.argv)-1 != count_needed_arguments:
    sys.exit("This script requires "+str(count_needed_arguments)+" arguments: a file path.")

file_path = sys.argv[1]

# Get the current date
current_date = date.today().isoformat()

# Get the creation date from git (if possible)
git_dates = str(subprocess.run(["git", "log", "--follow", "--format=%ad", "--date", "format:%Y-%m-%d", "--reverse", file_path], stdout=subprocess.PIPE).stdout).strip('\\n')
if re.match(r"^b'(\d{4}-\d{2}-\d{2})", git_dates):
    # Git was able to find dates
    creation_date = re.search(r"^b'(\d{4}-\d{2}-\d{2})", git_dates).group(1)
else:
    # Git did not find a creation date for the file, so the file is not in git yet.
    # Use the current date as the creation date.
    creation_date = current_date

# Read the file in memory
with open(file_path, "r", newline="\n") as read_file:
    file_content = read_file.read()

# Change or add a timestamp in the content
new_timestamp = "<small>This page was last modified on " + current_date + " and created on " + creation_date + ".</small>"
regex_pattern = r"^<small>This page was last modified on \d{4}-\d{2}-\d{2} and created on \d{4}-\d{2}-\d{2}.</small>$"
if re.match(regex_pattern, file_content, re.MULTILINE):
    # An old timestamp exists - update it.
    re.sub(regex_pattern, new_timestamp, file_content)
else:
    # No timestamp exists yet - add one.
    file_content = new_timestamp + "\n" + file_content

# Write the modified file
with open(file_path, "w", newline="\n") as write_file:
    write_file.write(file_content)