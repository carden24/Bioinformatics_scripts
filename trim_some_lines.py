#!/usr/bin/python

#usage
#python trim.some.lines.py <filein> <fileout>

import sys

filein=open(sys.argv[1],'r')
fileout=open(sys.argv[2],'w')

for line in filein:
#   print line
   if line.startswith('MM'):
      continue
   elif line.startswith('CGTGAGTGTAAGTTTTCTGGTCAGGTCATA'):
      continue
   else:
      fileout.write('%s'%line)
fileout.close()
