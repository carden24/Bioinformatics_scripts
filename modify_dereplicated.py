#!/usr/bin/python

#usage
#python modify.dereplicated.py <dereplicated.fasta> <dereplication.table> 
#       	0			 1		2		


import sys
import Bio
from Bio import SeqIO


#Create dereplication dictionary
derep_dictionary = {}

derep_table = open(sys.argv[2],'r')

for line in derep_table:
   if line.startswith('Representative'):
      continue
   else:
      line = line.split("\t")
      seq = line[0] #extract sequence name
      seq_count = line[1] #extract sequence count
      seq_count = seq_count.rstrip('\n')
      derep_dictionary[seq] = seq_count
derep_table.close()
print derep_dictionary

filein = open(sys.argv[1],'r')


out0 = str(sys.argv[1])
out = out0.rsplit( ".", 1 )[ 0 ]
out1 = out + '.modified.fasta'
fileout1 = open(out1,'w')


for seq_record in SeqIO.parse(filein, format = "fasta"):
   name = seq_record.id
   name_count = derep_dictionary.get(name)	#get info for read in dictionary   
   new_name = name + 'size=' + name_count + ';'
   sequence = seq_record.seq
   fileout1.write('>%s\n%s\n' %(new_name, sequence))
fileout1.close()

