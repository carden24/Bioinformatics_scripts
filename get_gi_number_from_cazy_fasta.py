#usage python get_gi_number_from_cazy_blast.py <blast.output> <out.file>
#        	0				1		2	


import sys

import sys
from Bio import SeqIO


filein = open(sys.argv[1], 'r')
fileout = open(sys.argv[2], 'w')

for record in SeqIO.parse(filein,"fasta"):
    gi_column = record.id
    if gi_column.startswith('gi|'):
        print '1'
        gi_location = gi_column.split('|')
        gi_number = gi_location[1]
        fileout.write('%s\t%s\n' %(gi_column, gi_number))
    else:
        print '2'
        gi_location = gi_column.split('_')
        gi_number = gi_location[1]
        fileout.write('%s\t%s\n' %(gi_column, gi_number))

filein.close()
fileout.close()

 

