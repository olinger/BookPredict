from nltk.util import ngrams
import operator

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


input_file = open('test.txt', 'r')
input_text = input_file.read()
ngrams = ngrams(input_text.split(), 2)
word_freq = {}
total = 0
for gram in ngrams:
	print gram
	word1 = CleanWord(gram[0])
	word2 = CleanWord(gram[1])
	if word1 == None or word2 == None:
		continue
	total += 1
	word = word1 + " " + word2
	if word in word_freq:
		word_freq[word] += 1# / float(total)
	else:
		word_freq[word] = 1# / float(total)
#	print word_freq[word]


sorted_word_freq = sorted(word_freq.items(), key=operator.itemgetter(1))
for x in sorted_word_freq:
	print "%s\t%f" % (x[0], x[1])
print total

