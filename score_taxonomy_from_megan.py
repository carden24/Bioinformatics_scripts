#!/usr/bin/python
# score_taxonomy_from_megan.py

import sys

score_dictionary = {}
filein = open(sys.argv[1], 'rb')
fileout = open(sys.argv[1] + '.score', 'w')

for line in filein:
     line0 = line.split(';')
     phyla = line[8]
     phyla = phyla.lstrip()
     phyla_score = score_dictionary.get(phyla, 0)
     phyla_score = phyla_score + 1
     score_dictionary[phyla] = phyla_score

#write score_dictionary
for key1, value1 in score_dictionary.iteritems():
   fileout.write("%s\t%s\t%d\n" %(sys.argv[1], key1, value1))

filein.close()
fileout.close()

     
