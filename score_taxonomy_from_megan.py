#!/usr/bin/python
# score_taxonomy_from_megan.py

import sys

score_dictionary = {}
filein = open(sys.argv[1], 'rb')
fileout = open(sys.argv[1] + '.score', 'w')
counter = 0

for line in filein:
    counter =  counter + 1
    line0 = line.split(';')
#     test_assign = line0[2]
#     print line0
#     if test_assign == ' Not assigned':
    if len(line0) <= 7:
        phyla = 'NA'
        phyla_score = score_dictionary.get(phyla, 0)
        phyla_score = phyla_score + 1
        score_dictionary[phyla] = phyla_score
    else:
        phyla = line0[8]
        phyla = phyla.lstrip()
        if phyla == 'Proteobacteria':
            phyla = line0[10]
            phyla = phyla.lstrip()
            phyla_score = score_dictionary.get(phyla, 0)
            phyla_score = phyla_score + 1
            score_dictionary[phyla] = phyla_score
        else:
            phyla_score = score_dictionary.get(phyla, 0)
            phyla_score = phyla_score + 1
            score_dictionary[phyla] = phyla_score

#write score_dictionary
for key1, value1 in score_dictionary.iteritems():
   fileout.write("%s\t%s\t%d\n" %(sys.argv[1], key1, value1))

fileout.write("%s\ttotal_reads\t%d\n" %(sys.argv[1], counter))

filein.close()
fileout.close()

     
