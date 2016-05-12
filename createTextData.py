import sys
import csv
all_lines = []
years = []
with open(sys.argv[1]) as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		years.append(row[0])
		all_lines.append(row[1:])


p = len(all_lines[0])
n = len(all_lines)
l = 10

outfile = open(sys.argv[2], 'w')

outfile.write("param p:= %i;\n" % p)
outfile.write("param n:= %i;\n" % n)
outfile.write("param lambda:= %i;\n\n" % l)

outfile.write("param X: ")
for i in range(1, p + 1):
	outfile.write("%i " % i)
outfile.write("\n")
outfile.write(":=\n")

for i, ratiolist in enumerate(all_lines):
	outfile.write("%i\t" % (i + 1))
	for r in ratiolist:
		outfile.write("%s\t" % r)
	outfile.write("\n")

outfile.write(";\n\n")

outfile.write("param Y:=\n")
for i, year in enumerate(years):
	outfile.write("%i\t%s\n" % ((i + 1), year))
outfile.write(";")