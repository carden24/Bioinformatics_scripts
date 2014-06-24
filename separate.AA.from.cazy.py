# Separate AA entries
# Read line split name, if it is an AA, then write, else ignore


#usage python separate.AA.from.cazy.py <cazy.fasta> <only_AA.fasta>
#        	0			1		2

import sys
#import Bio
from Bio import SeqIO
import re


all_cazy_fasta = open(sys.argv[1], 'rb')
only_AA_fasta = open(sys.argv[2], 'w')

filein = open(all_cazy_fasta,'rb')
fileout = open(only_AA,'w')

for seq_record in SeqIO.parse(filein, format = "fasta"):
        description = seq_record.description
        description_search = re.search('(\()([CAZY]+)(\:)('AA')(\)) ', description)
#        description_search = re.search('(\()([CAZy]+)(\:)([0-9A-Za-z\_\:\[\],]+)(\))', description)
#        print description
        if description_search == None:
            continue
        else:
            fileout.write('>%s\n%s\n' % (seq_record.name, seq_record.seq))


