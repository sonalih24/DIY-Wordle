# This program implements simplified version of Wordle through file manipulation to build a Wordle wordlist and using tuples/sets/dictionaries to query the wordlist.

def createWordlist(filename): 
    # Read words from the provided file and store them in a list.
    # The file contains only lowercase ascii characters, are sorted
    # alphabetically, one word per line. Filter out any words that are
    # not 5 letters long, have duplicate letters, or end in 's'. Return
    # the list of words and the number of words as a pair.
    # Open files for input and output
    infile = open(filename, "r")
    # This will read the entire file into string
    string = infile.read()
    # Split string into words
    new_wordlist = [x for x in string.split()]
    # loop to remove any words not 5 characters in length
    for word in new_wordlist[:]:
        if len(word) != 5:
            new_wordlist.remove(word)
    # Nested for loop one loop going thru each character and then the nested loop goes thru the next character so it would be whatever is in the first for loop + 1
    for word in new_wordlist[:]:
        if len(set(word)) != len(word):
            new_wordlist.remove(word)
    # loop to remove any words in list that end with 's'
    for word in new_wordlist[:]:
        if word.endswith('s'):
            new_wordlist.remove(word)
    #print(new_wordlist)
    infile.close()
    # Counts lines in small word file
    count = 0
    for lines in new_wordlist[:]:
        count = count + 1
    return(new_wordlist ,count)

def containsAll(wordlist, include):
    # Given your wordlist, return a set of all words from the wordlist
    # that contain all of the letters in the string include.  
    # include = input("Enter a string to test for including: ")
    containsAllList = set()
    for word in wordlist:
        added = True
        for i in include:
            if i not in word:
                added = False
                break
        if added == True:
            containsAllList.add(word)
    return(containsAllList)

def containsNone(wordlist, exclude):
    # Given your wordlist, return a set of all words from the wordlist
    # that do not contain any of the letters in the string exclude.  
    containsNoneList = set()
    for word in wordlist:
        added = True
        for i in exclude:
            if i in word:
                added = False
                break
        if added == True:
            containsNoneList.add(word)
    return(containsNoneList)

def containsAtPositions(wordlist, posInfo):
    # posInfo is a dictionary that maps letters to positions.
    # You can assume that the positions are in [0..4].  Return a set of
    # all words from the wordlist that contain the letters from the
    # dictionary at the indicated positions. For example, given posInfo
    # {'a': 0, 'y': 4}.   This function might return the set:
    # {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}.
    containsPositionsList = set()
    for word in wordlist:
        added = True
        for key in posInfo:
            if word[posInfo[key]] != key:
                added = False
                break
        if added == True:
            containsPositionsList.add(word)
    return(containsPositionsList)

def getPossibleWords(wordlist, posInfo, include, exclude):
    # Finally, given a wordlist, dictionary posInfo, and
    # strings include and exclude, return the set of all words from 
    # the wordlist that contains the words that satisfy all of 
    # the following:
    # * has letters in positions indicated in posInfo
    # * contains all letters from string include
    # * contains none of the letters from string exclude.
    emptySet = set()
    # Calls "containsAtPositions" function to filter for letters in indicated positions
    filter1 = emptySet.union(containsAtPositions(wordlist,posInfo))
    positionFilter = set(filter1)
    # Calls "containsAll" function to filter for letters from string include AND intersects this with first filter
    filter2 = positionFilter.intersection(containsAll(wordlist, include))
    withIncludeFilter = set(filter2)
    # Calls "containsNone" function to filter for letters from string exclude AND intersects this with second filter
    filter3 = withIncludeFilter.intersection(containsNone(wordlist,exclude))
    possibleWordsList = set(filter3)
    return(possibleWordsList)




