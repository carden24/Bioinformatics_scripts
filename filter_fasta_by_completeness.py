#!/usr/bin/python

#usage
#python filter_fasta_by_completeness.py <filein> > <fileout>

import sys
import Bio
from Bio import SeqIO

filein = open(sys.argv[1], 'rb')
fileout = open(sys.argv[2], 'w')

for seq_record in SeqIO.parse(filein, format = "fasta"):
   line = seq_record.description
#   print line
   line = line.split('#')
#   print line
   partial_info = line[4]
#   print partial_info
   partial = partial_info.split(';')
#   print partial
   if partial[1] == 'partial=00':
      fileout.write('>%s %s\n%s\n' %(seq_record.id, seq_record.description, seq_record.seq))
#      print 'complete'
   else:
      continue

#   print name
#   print '>%s\n%s' % (name, seq_record.seq)

filein.close()
fileout.close()



