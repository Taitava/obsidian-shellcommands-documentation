From [[Variables - general principles#^arguments1|Variables - general principles]]:
![[Variables - general principles#^arguments1]]

## Empty value as an argument
If you want to pass an empty text as an argument to a variable, you can do it by simply writing nothing between a colon `:` and closing brackets `}}`. For example, [[{{tags}}]] variable can be used to list all tags of the current file without variables: `{{tags:}}`. If you have tags `#tag1`, `#tag2` and `#tag3`, that example would give you `tag1tag2tag3`. But maybe that example is not very useful.

## Multiple arguments to a variable, and optional arguments
In theory, there can be variables that accept multiple arguments (separated by multiple colons `:`, e.g. `{{variable:argument1:argument2:argument3}}`), but at the moment of writing this documentation (2021-11-20, for SC version `0.7.0`), there are only variables that take only one argument (and variables without any arguments).

In theory, some arguments can be optional, but at the moment all variables that use an argument, are defined so that the argument is mandatory.

## Including a literal colon `:` in an argument
The last argument of a variable can also contain a colon `:` as a literal character in the argument, e.g. `{{date:HH:mm}}` gives the current time with colon `:` as a separator, and `{{date::YYYY:}}` gives the current year surrounded by two colons, e.g. `:2021:`.

You cannot use a colon `:` in an argument that precedes the last argument, as in that situation the colon would act as a separator between two arguments. However, at the moment of writing this documentation (2021-11-20, for SC version `0.7.0`), there is no variables that can take multiple arguments. This notice is actually meant for future versions of SC that will have variables that use multiple arguments.

# History


> [!page-edit-history]- Page edit history: 2021-11-20 &#10132; 2021-11-24
> - [<small>2021-11-24</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/da2bc9e5eee499f12b6cc2c4952739652b999de1): Wrap variable note names between {{ and }}.
> - [<small>2021-11-21</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/f368a217fcc5484e3f078b598d6a2c3e2cbe35cb): Fix typos using WebStorm.
> - [<small>2021-11-20</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commit/2c3e9b2d8b625eb02dd1b6d8b709a5a4140c36f1): Arguments for variables.
> 
> [<small>See this list of commits on GitHub</small>](https://github.com/Taitava/obsidian-shellcommands-documentation/commits/main/Variables/Arguments%20for%20variables.md).
> ^page-edit-history