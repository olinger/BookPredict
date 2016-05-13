#quick parser to write w from ampl to clean csv
import csv
import sys
import operator 
#usage input_text_file output_csv_file
infile = open(sys.argv[1], 'r')
outfile = open(sys.argv[2], 'w')
w = {}
for line in infile:
	line = line.strip().split('\t')[0].split()
	for i, s in enumerate(line):
		if i % 2 == 0:
			w[int(s)] = line[i + 1]

w = [tup[1] for tup in sorted(w.items(), key=operator.itemgetter(0))]

writer = csv.writer(outfile)
writer.writerow(w)