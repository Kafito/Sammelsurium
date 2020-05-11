import re

# Fuzzy matching is commonly rather handled useing levenshtein-distance
# e.g. https://github.com/seatgeek/fuzzywuzzy

def fuzzify(query):
    regex = r'(?:.*?' + re.sub(r'(.)', r'(\1).*?', query) + ')'
    return regex

def fuzzyScore(pattern, reference):
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

if __name__ == '__main__':
    searchstrings = ('Germany' , 'germany', 'Ge', 'ermy', 'Blablagerm', 'Gbermany', 'Germn')
    name = 'Germany'
    for search in searchstrings:
        print(search, fuzzyScore(search, name))

