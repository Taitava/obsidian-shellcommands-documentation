import re
import sys

count_needed_arguments = 3
if len(sys.argv) < count_needed_arguments:
    sys.exit("This script requires "+str(count_needed_arguments)+" arguments: a file path, a version and a release date.")

file_path = sys.argv[1]
version = sys.argv[2]
release_date = sys.argv[3]
regex_pattern = r"#TODO:\s*Add a date\.?\s*\[" + re.escape(version) + "\s*-\s*\d{4}--\]\([^)]*\):"

print("Looking for #TODOs in "+file_path+" using regex "+regex_pattern)
todos_found = False
with open(file_path, "r") as read_file: # FIXME: This translates all newlines to \r\n on Windows, they should be \n. Not too bad, because Obsidian fixes the newlines when any manual edit is done on the file.
    file_content = read_file.read()
    todos = re.finditer(regex_pattern, file_content, re.MULTILINE & re.IGNORECASE)

    for todo in todos:
        todos_found = True
        replace = todo.group(0)
        substitute = "["+version+" - "+release_date+"](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#"+version.replace(".","")+"---"+release_date+"):"
        print("Occurrence:")
        print(" - Replace:", replace)
        print(" - Substitute:", substitute)
        file_content = file_content.replace(replace, substitute)


if todos_found:
    # Write all changes to the file.
    # This overwrites the whole file.
    with open(file_path, "w") as write_file:
        write_file.write(file_content) # FIXME: See the other FIXME comment above, its result is written here.
else:
    # Nothing to do
    print("No #TODOs found.")