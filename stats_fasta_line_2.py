#!/usr/bin/python

#usage
#python fasta.stats.py <filein>

import sys

counter=0
total_len=0

filein = open(sys.argv[1],'r')
for line in filein:
#   print line
   if line.startswith('>'):
      print line
      continue
   else:
      print (len(line))

