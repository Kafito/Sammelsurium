# system modules
from pykeepass import PyKeePass
import string
import getpass
import sys

# own modules
import getch
import fuzzy

def clearScreen():
    print(chr(27) + "[2J" + chr(27) + "[H", end='')

def resetColor():
    print(chr(27) + "[0m", end='')

def grayScale(level):
    cmap = ["37;1", "37"]
    if level > 1:
        level = 1
    resetColor()
    print(chr(27) + "[" + str(cmap[level]) + ";40m", end='')

def highlight():
    print(chr(27) + "[37;1;4m", end='')


if len(sys.argv) != 2:
    print("Usage: main.py pass/to/password/db")
    sys.exit(-1)

password_db = sys.argv[1]
pw = getpass.getpass()
kp = PyKeePass(password_db, password=pw)


reqstring = ''
currentFavs = ()


clearScreen()

print("How to: Ctrl-C, Ctrl-D to abort, Enter to print password")
print("Input your fuzz:")

while True:
    char = getch.getch()
    if char == '\x03' or char == '\x04' or char == '\x1a':
        break
    elif char == '\r' and currentFavs:
        bestMatch = currentFavs[0][1]
        print("Password for '", bestMatch.title, "':\t", bestMatch.password)
        break
    elif char == '\x7f':
        if (reqstring):
            reqstring = reqstring[:-1]
    elif not char in string.printable:
        print("Unhandled unprintable char: ", repr(char))
    else:
        reqstring += char
    
    scores = [e for e in [(fuzzy.fuzzyScore(reqstring, str(entry)), entry) for entry in kp.entries]
                if e[0] != None]
    sortedScores = sorted(scores, key=lambda e: e[0], reverse=True)
    clearScreen()
    print("How to: Ctrl-C, Ctrl-D to abort, Enter to print password")
    print("Input your fuzz: ", end='')
    if reqstring :
        highlight()
        print(reqstring)
        resetColor()
    else:
        print('')

    currentFavs = sortedScores[:3]
    i = 0
    for e in currentFavs:
        # note: output may currently be 'mangled' to due a bug in pykeepass
        if len(currentFavs) == 1:
            highlight()
        else:
            grayScale(i)
        i = i+1
        print(e[1])
    resetColor()
resetColor()
