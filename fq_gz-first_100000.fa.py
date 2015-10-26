# python quality-trim.py <input fastq.gz file> <output fasta file>

import sys
import screed
import gzip

filein = sys.argv[1]
fileout = sys.argv[2]

fw = open(fileout, 'w')

from screed.fastq import fastq_iter

for n, record in enumerate(fastq_iter(gzip.open(filein,'rb'))):
   if n <= 100000:
      sequence = record['sequence']
      name = record['name']
      fw.write('>%s\n%s\n' % (name, sequence))
   else:
      break

fw.close

