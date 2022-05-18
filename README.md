# Wordle Utility

This code shows my knowledge of file manipulation, tuples, sets, and dictionaries.

Task 1: I built a Wordle wordlist. File words file contains a very long sorted series of lowercase English words, one per line. I then read words from the file, filter them and return a list of words that pass the filter. Filtering means discarding any words that are not five letters long, have any repeating letters, or end in 's'. It is safe to assume that there are no non-letter or upper case characters in the file. You can also assume that the file exists. It would be beneficial to strip each word of extra whitespace. Finally, return a pair consisting of the wordlist and its length.

Task 2: Querying my wordlist. As the player makes guesses in Wordle, they gain information about what letters are and are not in the solution and where some of those letters fall in the answer. Often, one of the hardest things about playing Wordle is thinking of new guesses that use that information strategically. But computers are great at that sort of thing. I have written four functions that would be very handy to have available when playing Wordle.
