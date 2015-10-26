# This scripts will do a blast search against the nr database
# The blast program as well as search parameters 
# can be specified inthe lines below

# Usage
# python remoteblastp.py <originalfile.fasta> <output.xml>
# 	 0			1		2		


my_perc_ident = 'none'
my_blast_program = 'blastp'
my_evalue_treshold = 0.00001
my_hitlist_size = 10

import sys
import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#input
filein = open(sys.argv[1], "r")

#outputs
myout = sys.argv[2]
fileout = open(myout, 'w')


for seq_record in SeqIO.parse(filein, format="fasta"):
#   print seq_record   
#   print seq_record.format("fasta")
   result_handle = NCBIWWW.qblast(my_blast_program, "nr", seq_record.format("fasta"), hitlist_size = my_hitlist_size, expect = my_evalue_treshold, perc_ident = my_perc_ident)
   fileout.write(result_handle.read())
filein.close()
fileout.close()
