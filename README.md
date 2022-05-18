# Wordle Utility

This code shows my knowledge of file manipulation, tuples, sets, and dictionaries.

Task 1: Building a Wordle word list. 
My word file contains a very long sorted series of lowercase English words, one per line. I then read words from the file, filter them and return a list of words that pass the filter. For the case of this Wordle game, filtering means discarding any words that are not five letters long, have any repeating letters, or end in 's'. It is safe to assume that there are no non-letter or upper case characters in the file. You can also assume that the file exists; however the user can read in a word file of their choice. It would be beneficial to strip each word of extra whitespace. This portion of the utility also returns a pair consisting of the word list and its length.

Task 2: Querying the read in word list. 
As the player makes guesses in Wordle, they gain information about what letters are and are not in the solution and where some of those letters fall in the answer. I have written four functions using tuples, sets, and dictionaries that are very helpful when playing this version of Wordle.
