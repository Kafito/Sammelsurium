from pykeepass import PyKeePass
import getpass
import getch
import fuzzy

import readline
import time


import string

if True:
    pw = getpass.getpass()

    kp = PyKeePass('/home/kafi/passworddb.kdbx', password=pw)


reqstring = ''

currentFavs = ()
print("Input your fuzz:")
while True:
    char = getch.getch()
    if char == '\x03' or char == '\x04' or char == '\x1a':
        break
    elif char == '\r' and currentFavs:
        bestMatch = currentFavs[0][1]
        print("Password for '", bestMatch.title, "':\t", bestMatch.password)
        break
    elif char == '\x7f' and reqstring:
        reqstring = reqstring[:-1]
    elif not char in string.printable:
        print("Unhandled unprintable char: ", repr(char))
    else:
        reqstring += char
    
    scores = [e for e in [(fuzzy.fuzzyScore(reqstring, str(entry)), entry) for entry in kp.entries] if e[0] != None]
    sortedScores = sorted(scores, key=lambda e: e[0], reverse=True)
    if reqstring : print("SearchString: " + reqstring)
    currentFavs = sortedScores[:3]
    for e in currentFavs:
            print(e[0], e[1])

    

