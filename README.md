bin
===

A collection of useful scripts for your path

Clone this repository to your machine; I recommend the home directory. Add the repository to your path, and then you can use the scripts from anywhere!

Envy Examples
-------------

```bash
# show values of the PATH and JAVA_HOME environment variables
# varaible's value are split on delimeter ':' for unix systems and ';'
# on windows. You can control the delimeter with -d.
envy -s PATH JAVA_HOME
```

```bash
# show value of the PATH variable, and filter it's split values with a 
# regular expression
envy -s PATH -r "/usr"
```

```bash
# list all the environment variables
envy -ls 
```

```bash
# list the environment variables that have an underscore in them
# -ls takes a regular expression as a filter
envy -ls ".*_.*"
```

```bash
# append a path to the PATH environment variable
envy -a PATH "/path/to/append"
```

```bash
# put a value into a new or existing environment variable YOSHI
envy -p YOSHI "yoshi's value"
```

```bash
# delete (kill) an environment variable 
envy -k YOSHI
```

MdUtil Examples
----------------

```bash
# print a markdown table from a csv, tsv, or tab file.
mdutil --table data.csv
```