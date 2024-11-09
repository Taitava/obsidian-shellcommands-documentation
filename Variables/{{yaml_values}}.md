---
cssclass: customiseTitle
---
# Variable: `{{yaml_values:property:separator}}`
> [!Quote] {{yaml_values}} described in the *Shell commands* plugin's settings
> Reads a list of values from the current file's frontmatter. Takes a property name and separator as arguments. You can access nested properties with dot notation: property1.property2

![[{{yaml_value}}#Using dot notation to access nested properties]]

![[{{yaml_value}}#Accessing list values with numeric indexes]]

## Examples

These examples use the following note file content:

```markdown
---
cssclass: some-class
book_details:
  title: "My life"
  authors:
    - "Me!"
    - "Willy Writer"
  chapters:
    - 
      - "Birth"
      - "Childhood"
      - "Teenage"
    - 
      - "Young adulthood"
      - "Middle age"
    - 
      - "Pension age"
      - "Slowing down the pace"
---
```

### Example: Get all the authors of the book

As the `authors` list is a sub-item in `book_details`, it's needed to use a dot notation to access it: `book_details.authors` . Here's a complete example of a [[Bash]] command:
```bash
echo "Book authors: "{{yaml_values:book_details.authors: and }}
```
Output:
```
Book authors: Me! and Willy Writer
```

### Example: Get all the parts and chapters of the book

The chapters of this book are dived into three parts: I, II and III (without actual numbering or labeling). To get the chapters of all the three parts, each part must be retrieved separately, and numeric indexes are needed to refer to specific parts:
```bash
echo "Part I   chapters: "{{yaml_values:book_details.chapters.0:, }} # List indexing starts from 0, not 1.
echo "Part II  chapters: "{{yaml_values:book_details.chapters.1:, }}
echo "Part III chapters: "{{yaml_values:book_details.chapters.2:, }}
```
Output:
```
Part I   chapters: Birth, Childhood, Teenage
Part II  chapters: Young adulthood, Middle age
Part III chapters: Pension age, Slowing down the pace
```

> [!INFO] Only flat lists can be read at once
> It's not possible to do a single reading of the variable to get all the parts and chapters at once. If you tried `{{yaml_values:book_details.chapters:,}}` without the index number, you would get the following error:
> > [!ERROR]
> > YAML property 'chapters' contains (at least) one value that is not a single scalar value or that is empty. E.g. nested lists are not supported.
> 
> So, the readable property needs to point to a list of texts/numbers, not a list of lists.

## Key-value pairs (map objects) are not supported yet

Consider the following example:

```
---
cssclass: some-class
book_details:
  title: "My life"
  authors:
    Interviewee: "Me!"
    Writer: "Willy Writer"
---
```

The `book_details.authors` property cannot be read, because it contains a key-value paired map instead of a list. (A list would only contain values without keys). So, using `{{yaml_values:book_details.authors: and }}` would cause the following error:

> [!ERROR] 
> YAML property 'authors' is a map object with key-value pairs. Reading multiple values from objects is not yet supported. Can the YAML be changed from "key: value" format to "- list format"?

[Key-value pairs might become supported later](https://github.com/Taitava/obsidian-shellcommands/discussions/415#discussioncomment-10101724).
## Special characters in _separator_ are escaped

As is the case with [[{{tags}}]] variable, also any special characters in the `separator` argument of this variable are prefixed with an escape character. The [[{{tags}}#Special characters in *separator* are escaped|{{tags}} variable explains how its separator argument is escaped]]. The same principles apply for the separator of this variable, too.

## Availability
> [!Warning] Only available:
> - When the active pane contains a file, not in graph view or other non-file view.
> - Also, the given YAML property must exist in the file's frontmatter, and it must be a list instead of a single value.

## See also
- [[{{yaml_value}}]]
- [[{{event_yaml_values}}]]
- [[{{event_yaml_value}}]]

# History
- #TODO: Add a date [0.23.0 - 2024--](https://github.com/Taitava/obsidian-shellcommands/blob/main/CHANGELOG.md#00---2024--): The variable was released. ([#424](https://github.com/Taitava/obsidian-shellcommands/issues/424)).
