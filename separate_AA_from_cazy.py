# Separate AA entries
# Read line split name, if it is an AA, then write, else ignore


#usage python separate.AA.from.cazy.py <cazy.fasta> <only_AA.fasta>
#        	0			1		2

import sys
#import Bio
from Bio import SeqIO
import re


all_cazy_fasta = sys.argv[1]
only_AA_fasta = sys.argv[2]

filein = open(all_cazy_fasta,'rb')
fileout = open(only_AA_fasta,'w')

for seq_record in SeqIO.parse(filein, format = "fasta"):
        description = seq_record.description
        description_search = re.search('(\()([CAZy]+)([A0-9noe\:]+(\)))', description)
        if description_search == None:
            continue
        else:
            print description_search.group(0)
            fileout.write('>%s\n%s\n' % (seq_record.description, seq_record.seq))

