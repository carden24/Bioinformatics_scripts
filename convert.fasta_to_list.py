#!/usr/bin/python

#usage
#python convert.fasta.to.list.py <filein.fasta> > file.to.print.to

import sys
import Bio
from Bio import SeqIO

filein=open(sys.argv[1],'r')
filename=sys.argv[1]

for seq_record in SeqIO.parse(filein, format="fasta"):
   name=seq_record.id
   print "%s\t%s" %(filename,name)
