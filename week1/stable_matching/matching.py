import string
from sys import stdin
from collections import defaultdict

n, p = map(int, next(stdin).split())
proposers = []
aPrefs = {}
bPrefs = defaultdict(lambda: defaultdict(int))
matches = {}

half = int(n/2)

for _ in range(half):
    personPref = list(next(stdin).split())
    person = personPref[0]
    proposers.append(person)
    aPrefs[person] = personPref[1:]
    aPrefs[person].reverse()

for _ in range(half):
    personPref = list(next(stdin).split())
    bPrefs[personPref[0]] = {b: count for count,b in enumerate(personPref) if count != 0}

while len(proposers) != 0:
    proposer = proposers.pop()

    # Pop the top preference of the proposer
    prefs = aPrefs[proposer]
    rejector = prefs.pop()

    if rejector not in matches: 
        # The rejector has not yet been matched with anybody
        matches[rejector] = proposer
    else:
        # Rejector has already been matched...
        currentMatch = matches[rejector]
        currMatchRank = bPrefs[rejector][currentMatch]
        proMatchRank = bPrefs[rejector][proposer]

        if currMatchRank > proMatchRank:
            # The proposer is the new match 
            matches[rejector] = proposer
            proposers.append(currentMatch) # Add back the rejected match
        else:
            proposers.append(proposer) # The proposer has been rejected

for match, value in matches.items():
    print(match + " " + value)
            