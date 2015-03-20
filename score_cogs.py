#!/usr/bin/python
# File created on 3 Mar 2014.

# author__ = "Erick Cardenas Poire"
# Usage python ./score_cogs.py <cogs.txt>

import sys
import re

# Expected input
# JGI12692J13336_10000011	COG0141	40.91	22	69	90	307	328	0.055	29.4

filein = open(sys.argv[1], 'r')
shortname = re.sub('[.](txt)', '', sys.argv[1], re.I)
output_file = shortname + "_summary.txt"
fileout = open(output_file, 'w')

# Created empty result dictionary
COG_dictionary = {}

for line in filein:
   # Split line from results
   line = line.split('\t')
   COG = line[1]
   # Get current COG count, if not found use zero
   COG_count = COG_dictionary.get(COG, 0)
   new_score = COG_count + 1
   COG_dictionary[COG] = new_score

for key, value in COG_dictionary.iteritems():
   fileout.write("%s\t%s\t%s\n" %(sys.argv[1], key, value))

filein.close()
fileout.close()

