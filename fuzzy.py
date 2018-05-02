# taken from https://j11y.io/javascript/fuzzy-scoring-regex-mayhem/

import re
import math


def createFuzzyScorer(text):

    def makeFuzzyRegex(string):
        cleanedString = string #re.sub(r'\W', r'\\\1', string)
        regex = '^' + re.sub(r'(\\?.)', r'(?:(^.)?(\1)(.??))?', cleanedString) + "$"
        #print(regex)
        return regex

    regex = makeFuzzyRegex(text)

    def fuzzyScore(query):
        matchResult = re.match(regex, query, flags=re.IGNORECASE)

        if not matchResult:
            return 0

        groups = matchResult.groups()

        score = 0
        for i in range(0, len(groups), 3):
            relevancyWeight = math.pow(i+1, -2)
            if (groups[i]): score -= relevancyWeight * 0.1
            if (groups[i+1]): score += relevancyWeight * 1
            if (groups[i+2]): score -= relevancyWeight * 0.1

        return score

    return fuzzyScore


score = createFuzzyScorer('Germany')
#print(score('ger'))
#print(score('erman'))
#print(score('many'))
#print(score('blablabla'))

######
#GitHub
#Gillard.com


def fuzzify(query):
    regex = r'(?:.*?' + re.sub(r'(.)', r'(\1).*?', query) + ')'
    return regex

def fuzzyScore2(pattern, reference):
    result = re.match(fuzzify(pattern), reference, flags=re.IGNORECASE) 
    reflen = len(reference)
    lastindex = -1
    score = 0
    if not result:
        return None

    matchCount = result.lastindex and result.lastindex or 0
    for i in range(1, matchCount + 1):
        startindex = result.start(i)
        if startindex == None or startindex == -1:
            score = max(0, score - len(reference) / 2)
        else:
            score +=  1.0*(reflen - startindex)
            penalty = (startindex - lastindex - 1)
            assert(penalty >= 0)
            score -= 2.0*penalty*penalty
            lastindex = startindex
    return score

searchstring = ('Germany' , 'germany', 'Ge', 'ermy', 'Blablagerm', 'Gbermany', 'Germn')
name = 'Germany'
for search in searchstring:
    print(search, fuzzyScore2(search, name))

from pykeepass import PyKeePass
import getpass
if True:
    pw = getpass.getpass()

    kp = PyKeePass('/home/kafi/passworddb.kdbx', password=pw)

import readline
import time

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

string = ''

getch = _Getch()
currentFavs = ()
print("Input your fuzz:")
while True:
    char = getch()
    if char == '\x03' or char == '\x04' or char == '\x1a':
        break
    elif char == '\r' and currentFavs:
        bestMatch = currentFavs[0][1]
        print("Password for '",bestMatch.title, "':", bestMatch.password)
        break
    elif char == '\x7f' and string:
        string = string[:-1]
    elif len(char) == len(char.encode()):
        string+=char
    
    scores = [e for e in [(fuzzyScore2(string, str(entry)), entry) for entry in kp.entries] if e[0] != None]
    sortedScores = sorted(scores, key=lambda e: e[0], reverse=True)
    if string : print("SearchString: " + string)
    currentFavs = sortedScores[:3]
    for e in currentFavs:
            print(e[0], e[1])

    

