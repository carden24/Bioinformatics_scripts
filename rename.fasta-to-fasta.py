#!/usr/bin/python

#usage
#python rename.fasta-to-fasta.py <filein> > <fileout>

import sys
import Bio
from Bio import SeqIO

filein=open(sys.argv[1],'rb')

for seq_record in SeqIO.parse(filein, format="fasta"):
   line=seq_record.id
#   print line
   line=line.split('|')
#   print line
   name=line[2]
#   print name
   print '>%s\n%s' % (name, seq_record.seq)

filein.close()



