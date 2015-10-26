#usage
#python multiline_fasta_to_fasta.py <filein>

import sys
import Bio
from Bio import SeqIO

filein = open(sys.argv[1], 'r')
fileout_name = sys.argv[1] + '_new.fa'
fileout = open(fileout_name, 'w')

for seq_record in SeqIO.parse(filein, format = "fasta"):
   fileout.write('>%s %s\n%s\n' %(seq_record.id, seq_record.description, seq_record.seq))

filein.close()
fileout.close()

