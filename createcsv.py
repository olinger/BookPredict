import csv
import operator
import glob
import sys

#usage path_to_input_files csv_out_file_name text_out_file_name X
X = int(sys.argv[4])
path = sys.argv[1] + 'part-*'
#print path
files = glob.glob(path)   
row = [0] * X
x_variables = []
for name in files:
	with open(name) as f:
		line = f.readline()
		#print line
		xvarstring = line.split(',')
		for i,s in enumerate(xvarstring):
			#print s
			s = s[s.find("[")+1:s.find("]")]
			ngram = s.split(':')[0]
			#print s
			#print name
			occ = s.split(':')[1]
			x_variables.append((ngram, occ))
		#print len(x_variables)

top_X_variables = [tup[0] for tup in sorted(x_variables, key=operator.itemgetter(1), reverse = True)[0:X]]

#print top_X_variables

#infile = open('testout', 'r')
#line = infile.readline()
year_map = {}
with open(sys.argv[2], 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Year"] + top_X_variables)
	for name in files:
		with open(name) as f:
			f.readline()
			year = int(f.readline().strip().split('\t')[0])
			for line in f:
				line = line.strip().split('\t')
				if len(line) == 1:
#					writer.writerow([year] + row)
					#print row
					year = int(line[0])
#					row = [0] * X
				else:
					#print line[0]
					if line[0] in top_X_variables:
						if year in year_map:
							year_map[year][line[0]] = line[1]
						else:
							year_map[year] = {line[0] : line[1]}
						#row[top_X_variables.index(line[0])] = line[1]
	#print year_map
	#for y in range(1800, 2008):
	#	ys = "%i" % y
	#	if ys in year_map:
	#		for ngram, freq in year_map[ys].iteritems():
	#			if freq in top_X_variables:
	#				row[top_X_variables.index(ngram)] = freq
			#writer.writerow([year] + row)
	#	row = [0] * X

	all_years = [tup[0] for tup in sorted(year_map.items(), key=operator.itemgetter(0))]
	for y in all_years:
		if y in year_map:
			for ngram, freq in year_map[y].iteritems():
				row[top_X_variables.index(ngram)] = freq
			writer.writerow([str(y)] + row)
			row = [0] * X

with open(sys.argv[3], 'w') as f:
	for x in top_X_variables:
		f.write("%s\t" % x)