#!/usr/bin/python

#usage
#python ungap.fasta.py <filein>  <fileout>

import sys


filein = open(sys.argv[1], 'r')
fileout = open(sys.argv[2], 'w')

for line in filein:
   if line.startswith('>'):
      fileout.write('%s' %line)
      continue
   else:
      sequence = line
      sequence = line.replace('-','')
      sequence = sequence.replace('.','')
      sequence = sequence.replace(' ','')
      fileout.write('%s' %sequence)
filein.close()
fileout.close()
