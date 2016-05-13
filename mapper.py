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
textin = open("googlebooks-eng-all-1gram-20120701-t", 'r')
for line in textin:
    #sys.stderr.write("debug info: line: %s\n" % line)
    # Strip the line of whitespace and split into a list
    line = line.strip().split()
    # Get the year and the number of occurrences from
    # the ngram line
    year = int(line[1])
    occurrences = int(line[2])
    #ignore years before 1800, not enough data
    if year < 1800:
        continue
    # Use CleanWord function to clean up the word
    word = CleanWord(line[0])
    #sys.stderr.write("debug info: word: %s\n" % word)
    # If CleanWord didn't return a string, move on
    if word == None:
     #   sys.stderr.write("debug info: word == None \n")
        continue
    # Print the output: word, year, and number of occurrences
    print '%s\t%s\t%s' % (word, year,occurrences)
#sys.stderr.write("debug info: mapper done\n")