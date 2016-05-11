#!/usr/bin/env python
import sys
import operator

ngram_map = {}
year_map = {}
end_map = {}
year_totals = {}

X = 50
index = 0
#textin = open("googlebooks-eng-all-1gram-20120701-x",'r')
for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line)!= 3:
        continue
    current_ngram, year, occurrences = line
    try:
        year = int(year)
    except ValueError:
        continue
    try:
        occurrences = int(occurrences)
    except ValueError:
        continue

    #map of each ngram in dataset to how many times it has ever occurred
    #use this to get the top X ngrams for regression model
    if current_ngram in ngram_map:
        ngram_map[current_ngram] += int(occurrences)
    else:
        ngram_map[current_ngram] = int(occurrences)

    #map of each year to how many ngrams have occurred that year. 
    #use this to create ratio for each ngram in a given year
    if year >= 1800: #filter out years before 1800 because there is not as much data
        if year in year_totals:
            year_totals[year] += occurrences
        else:
            year_totals[year] = occurrences
    else:
        continue

    #map each ngram occurrence within each year
    if year in year_map:
        if current_ngram in year_map[year]:
            year_map[year][current_ngram] += occurrences
        else:
            year_map[year][current_ngram] = occurrences
    else:
        this_year_ngram = {current_ngram : occurrences}
        year_map[year] = this_year_ngram


try:
    storei = 0
    sys.stderr.write("debug info: ngram_map size: %i\n" % len(ngram_map))
    top_X_ngrams_map = sorted(ngram_map.items(), key=operator.itemgetter(1), reverse = True)[0:X]
    top_X_ngrams = [tup[0] for tup in top_X_ngrams_map]
    sys.stderr.write("debug info: top_X_ngrams size: %i\n" % len(top_X_ngrams))
    if len(top_X_ngrams) > 0:
        for i in range(0, len(top_X_ngrams) - 1):
            storei = i
            print "[%s:%i]," % (top_X_ngrams_map[i][0], top_X_ngrams_map[i][1]),
        print "[%s:%i]" % (top_X_ngrams_map[-1][0], top_X_ngrams_map[i][1])
except IndexError, e:
    sys.stderr.write("NGRAMERROR: Index error at top_X_ngrams printing\n")
    sys.stderr.write("Length of top_X_ngrams is %i, i is %i\n" % (len(top_X_ngrams), storei))
    sys.stderr.write(e)
    sys.exit(0)

try:
    for year, ngrams in year_map.iteritems():
        for ngram, occ in ngrams.iteritems():
            if ngram in top_X_ngrams:
                ratio = float(occ) / float(year_totals[year])
                if year in end_map:
                    end_map[year][ngram] = ratio
                else:
                    end_map[year] = {ngram : ratio}
except IndexError, e:
    sys.stderr.write("NGRAMERROR: Index error at end map creation")
    sys.stderr.write(e)

try:
    for year, ngrams in end_map.iteritems():
        print year
        for ngram, ratio in end_map[year].iteritems():
            print "%s\t%f" % (ngram, ratio)
except IndexError, e:
    sys.stderr.write("NGRAMERROR: Index error at final print")
    sys.stderr.write(e)

sys.stderr.write("debug info: reducer complete")