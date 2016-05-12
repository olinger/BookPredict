#!/usr/bin/env python
 
import sys
 
def CleanWord(aword):
    """
    Function input: A string which is meant to be
       interpreted as a single word.
    Output: a clean, lower-case version of the word
    """
    # Make Lower Case
    aword = aword.lower()
    # Remvoe special characters from word
    for character in '.,;:\'?':
        aword = aword.replace(character,'')
    # No empty words
    if len(aword)==0:
        return None
    # Restrict word to the standard english alphabet
    for character in aword:
        if character not in 'abcdefghijklmnopqrstuvwxyz':
            return None
    # return the word
    return aword
# Now we loop over lines in the system input
textin = open('googlebooks-eng-all-2gram-20120701-en', 'r')
for line in sys.stdin:
    #sys.stderr.write("debug info: line: %s\n" % line)
    # Strip the line of whitespace and split into a list
    line = line.strip().split()
   # print line
    # Get the year and the number of occurrences from
    # the ngram line
    year = int(line[3])
    occurrences = int(line[4])
    #ignore years before 1800, not enough data
    if year < 1800:
        continue
    # Use CleanWord function to clean up the word
    word1 = CleanWord(line[1])
    word2 = CleanWord(line[2])
    #sys.stderr.write("debug info: word: %s\n" % word)
    # If CleanWord didn't return a string, move on
    if word1 == None:
        continue
    if word2 == None:
        continue
    ngram = word1 + " " + word2
    # Print the output: word, year, and number of occurrences
    print '%s\t%s\t%s' % (ngram, year,occurrences)
sys.stderr.write("debug info: mapper done\n")