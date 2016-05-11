import csv

infile = open('testout', 'r')
line = infile.readline()

x_variables = line.strip().split(',')
for i,s in enumerate(x_variables):
	s = s[s.find("[")+1:s.find("]")]
	x_variables[i] = s
print len(x_variables)
row = [0] * len(x_variables)

with open('xdata.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Year"] + x_variables)
	year = infile.readline().strip().split('\t')[0]
	print year
	for line in infile:
		line = line.strip().split('\t')
		if len(line) == 1:
			writer.writerow([year] + row)
			print row
			year = line[0]
			row = [0] * len(x_variables)
		else:
			print line[0] + " line0"
			if line[0] in x_variables:
				row[x_variables.index(line[0])] = line[1]
