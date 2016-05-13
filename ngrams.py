from nltk.util import ngrams
import operator
import csv
import sys
import glob

#usage books_file_path x_var_text csv_to_output N(gram)
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
if len(sys.argv) != 5:
    print "Error - Parameters: books_file_path x_var_text csv_to_output N(gram)"
    sys.exit(0)
    
n = int(sys.argv[4])
xvarfile = open(sys.argv[2], 'r')
x_variables = xvarfile.readline().strip().split('\t')
freq = [0] * len(x_variables)
with open(sys.argv[3], 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Year"] + x_variables + ["Title"])
    path = sys.argv[1] + '*.txt'
    files = glob.glob(path)
    for name in files:
        freq = [0] * len(x_variables)
        title, year = name.split(".txt")[0].split("/")[1].split("-")
        input_file = open(name, 'r')
        input_text = input_file.read()
        text_ngrams = ngrams(input_text.split(), n)
        word_freq = {}
        total = 0
        for gram in text_ngrams:
        #    print gram
            word = ""
            for i in range(0, n):
                newWord = CleanWord(gram[i])
                if newWord != None:
                    word += CleanWord(gram[i])
                    if i < n - 1:
                        word += " "
          #  print word
            total += 1
            #word = word1 + " " + word2
            if word in word_freq:
                word_freq[word] += 1# / float(total)
            else:
                word_freq[word] = 1# / float(total)
        sorted_word_freq = sorted(word_freq.items(), key=operator.itemgetter(1))
        for x in sorted_word_freq:
            if x[0] in x_variables:
                freq[x_variables.index(x[0])] = float(x[1]) / float(len(word_freq))
        writer.writerow([year] + freq + [title])

