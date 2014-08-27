# python quality-trim.py <input fastq.gz file> 

import sys
import screed

filein = sys.argv[1]

from screed.fasta import fasta_iter

counter = 0
bases = 0

for n, record in enumerate(fasta_iter(open(filein,'rb'))):
   counter = counter + 1
   bases = bases + len(str(record['sequence']))

print "File: %s" %filein
print "Reads:%s" %counter
print "Bases:%s" %bases
