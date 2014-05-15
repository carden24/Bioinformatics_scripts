#!/usr/bin/python

#usage
#python count.total.bases.py <filein>

import sys
import Bio
from Bio import SeqIO
import gzip

filein=gzip.open(sys.argv[1],'rb')

counter=0
total_len=0

for seq_record in SeqIO.parse(filein, format="fasta"):
   len_seq=len(seq_record.seq)
   total_len=total_len+len_seq
   counter=counter+1

print 'Reads found: %s' %counter
print 'Total bases: %s' %total_len

