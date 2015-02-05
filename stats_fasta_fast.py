#!/usr/bin/python

#usage
#python stats_fasta_fast.py <filein>

import sys
import Bio
from Bio import SeqIO

filein = open(sys.argv[1], 'r')

counter = 0
total_len = 0

for seq_record in SeqIO.parse(filein, format = "fasta"):
   len_seq = len(seq_record.seq)
   total_len = total_len + len_seq
   counter = counter + 1

print '%s\t%s\t%s' %(sys.argv[1], str(counter), str(total_len))



