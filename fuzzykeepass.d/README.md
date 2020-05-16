# fuzzyKeepass
An experiment to implement fuzz matching logic with regular expressions,
motivated by the need to have access to my keepass password database from the
command-line.

## Features
 * (Reg-Ex powered) Fuzzy matching of entries in a keepass database.
 * A `paranoialauncher`, which disables networking for the python instance by
   unsharing kernel namespaces.

## Usage
```
    $ ./paranoialauncher [path/to/db]
    ... or ...
    $ python main.py path/to/db
```

The paranoia launcher is a bash wrapper that disables networking for python,
and provides a default database path of `~/passworddb.kkdbx`.

## Dependencies / Limitations
This script uses the following python libraries:
 * getpass
 * pykeepass

Limitations:
 * The script currently uses hard coded terminal escape codes for highlighting
   search results, which might interfere with different terminals, or when
   running on windows.
 * The script currently prints the password to the terminal, which is sufficient
   for my purposes, but might need adaption for others. 

## Motivation

When working remotely via ssh, I regularly encountered the need to access my
keepass password databases.

While searching for solutions, I noticed that there weren't any tools around
that allowed for the combination of
 * working on headless configurations
 * allow searching (fuzzy at best) entries in the database

So I took this as an opportunity for exploration and implement a fuzzy matching
logic.

The common way to implement this is to use the [Levenshtein Distance](
https://en.wikipedia.org/wiki/Levenshtein_distance), but I stumbled over a [regex based implementation]
(https://j11y.io/javascript/fuzzy-scoring-regex-mayhem/). However, I did not like the fact that a RegEx needed to be build up for each entry in my database, which sounded a bit to excessive.

I found a way to invert the matching logic, such that the regex is now build
for the search string, and all entries are matched against the search string
instead.

This simple scheme worked well enough for me, and this tool has been my regular
driver for accessing my passwords in headless scenarios since then.

> *NOTE*
> This tool was implemented in early 2018, the situation around tooling may have changed since then.

## Credits
 * The script is based on an idea for implementing [reg-ex based fuzzy-matching logic by James Padolsey](https://j11y.io/javascript/fuzzy-scoring-regex-mayhem/)

A transcript of his java script code can be found in [FuzzyScorePerElement.py](./FuzzyScorePerElement.py)
 * The script uses a Getch implementation from [ActiveCode, recipe 134892](https://github.com/ActiveState/code/tree/master/recipes/Python/134892_getchlike_unbuffered_character_reading_stdboth/)

## Alternatives
While there are some programs that allows for command-line access to passwords,
none of them worked for me well enough, especially in a headless configuration
such as my remote server.

[fzf](https://github.com/junegunn/fzf) is a very handy tool, it might be more
suitable to achieve fuzzy matching logic than using a RegEx based
implementation.  

## License
This project is licensed under the MIT License - see the
[LICENSE.txt](../LICENSE.txt) file for details
