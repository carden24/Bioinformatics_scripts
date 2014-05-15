#!/usr/bin/python

#usage
#python fasta.stats.v3.py <filein> > file.to.print.to

import sys
import Bio
from Bio import SeqIO

filein=open(sys.argv[1],'r')

counter=0
total_len=[]

print sys.argv[1]

for seq_record in SeqIO.parse(filein, format="fasta"):
   name=seq_record.id
   len_seq=str(len(seq_record.seq))
   print "%s\t%s" %(name,len_seq)
