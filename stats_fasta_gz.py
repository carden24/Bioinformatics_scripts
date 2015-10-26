# python quality-trim.py <input fastq.gz file> 

import sys
import screed
import gzip

filein = sys.argv[1]

from screed.fastq import fastq_iter

counter=0
bases=0

for n, record in enumerate(fastq_iter(gzip.open(filein,'rb'))):
   counter=counter+1
   sequence = record['sequence']
   seq=str(sequence)
   seq2=len(seq)
   bases=bases+seq2

print "File: %s" %filein
print "Reads:%s" %counter
print "Bases:%s" %bases
