# textClipExtract
A python script to resource different resources such as plain text, rtf or webarchives from Mac OS [textClippings](https://en.wikipedia.org/wiki/TextClipping).

## Usage
```
    $ textSnipExtract path/to/a.textClipping
```

In the current configuration, the script will extract all resources of types
`RTF `, `utf8`, `weba` (webarchive) and, if none of these were found, as a
fall-back `TEXT`.

This behavior can be easily modified for own purposes.

The return value of the script is non-zero in case neither any of the default
resource types nor the fall-back could be extracted or written to a file.

Therefore you can gather a list of failed resources like this
```
$ ./textSnipExtract "$myFile" || echo "$myFile" >> ~/failedClipExtractions.txt
```

## Motivation
While trying to become less platform dependent with my data, I stumbled over
many files that I created using an Mac OS X specific feature that I used quite
intensively during my early days. The data in these text clippings are stored
in the resource fork of Apples HFS+ file system, so it cannot be easily
accessed from the command line, and any migration of the data to another file
system might end up with losing the data from these snippets.

The solutions I found were _not applicable for my purpose_:
 * Using Apples `DeRez` to display the content of the resources, then use
   text-utilities (grep/sed) to extract the pure data.

   _Data contained characters that made the regex engine panic._

 * Use AppleScript to programmatically drop the files into text documents and
   store them.

   _I wanted to have all types of resources, including webarchives._

I decided to take this as an exercise to reverse engineer the file format of
the resource forks and to toy around with python.

## Technical background

The data structure that I came up with can be found (for now) in the leading
comment of the script file.
_Note: I specifically took this as an exercise to reverse engineering the
underlying file format. There might be full descriptions available on Apples
developer documentation, or other resources that have a more thorough view on
the file format._

Since macOS 10.12 Sierra, the data is stored in property lists. Being xml
files, they are more accessible to other platforms already.
Before that, the data is stored in the resource fork of the HFS+ file system.
On my current instance Mac OS X El Capitan (10.11), the data can be read using the path
`path/to/file.textClipping/..namedfork/rsrc`. This might be different on other version of the system.

## Disclaimer
Since the file format is reverse engineered only to the degree to make it work with all of my snippets, there is no guarantee that it will work for any textClipping thrown at it.
However, due to its non-destructive nature, giving it a try should not be an issue.
 * Opens the resource forks read-only.
 * Only writes the extracted resources, if there is no file with the same name that would be overwritten.

## Dependencies
 * python (>= 2.7)

## Alternatives
Most straight-forwardly, this can be done manually, by dragging the textClipping to a new text document.

As already mentioned, it is easy to find scripts that rely on 
 * `DeRez`, in combination with `sed`, `grep` or `tr`.
 * AppleScripts, that programmatically drag and drop textClippings to new text files and store them.

Alternatively, one could develop solutions based on Apples API
 * `FSOpenResrouceFile`
 * `Get1Resource`
(see https://stackoverflow.com/questions/6072779/how-to-programmatically-read-mac-textclipping-files?rq=1)

## License
This project is licensed under the MIT License - see the
[LICENSE.txt](../LICENSE.txt) file for details
