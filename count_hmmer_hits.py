#!/usr/bin/python

#usage
#python count_hmmer_hits.py <filein>

import sys

filein = open(sys.argv[1], 'r')
counter = 0

for line in filein:
   if line.ends.with('[number of targets reported over threshold]'):
   line2 = line.split(' ')
   print line2
else:
   continue

print '%s\t%s' %(sys.argv[1], str(counter))

