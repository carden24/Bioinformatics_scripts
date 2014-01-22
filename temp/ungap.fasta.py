#!/usr/bin/python

#usage
#python trim.some.lines.py <filein> <fileout>

import Bio
from Bio import Seq
from Bio import SeqIO
import sys


filein=open(sys.argv[1],'r')
fileout=open(sys.argv[2],'w')

for seq_record in SeqIO.parse(filein,"fasta"):
   new_seq=seq_record.seq
   new_seq=new_seq.ungap("-")
   name=seq_record.id
   description=seq_record.description
   fileout.write('>%s\s%s\n%s'%(name,description,new_seq))

fileout.close()
filein.close()
