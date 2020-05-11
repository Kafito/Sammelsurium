# Code is a transcript from javascript based on what has been described 
# by James Padolsey on https://j11y.io/javascript/fuzzy-scoring-regex-mayhem/
#
# This code served as a reference or staring point for my experiment.
# 


import re
import math

def createFuzzyScorer(text):

    def makeFuzzyRegex(string):
        cleanedString = string #re.sub(r'\W', r'\\\1', string)
        regex = '^' + re.sub(r'(\\?.)', r'(?:(^.)?(\1)(.??))?', cleanedString) + "$"
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

if __name__ == '__main__':
    score = createFuzzyScorer('Germany')
    print(score('ger'))
    print(score('erman'))
    print(score('many'))
    print(score('blablabla'))
