#!/usr/bin/python
#calculate_sequence_conservation.py <fasta>

from Bio import AlignIO
import sys
import os

#alignment = Clustalw.parse_file(os.path.join(os.curdir, sys.argv[1]))

filein = sys.argv[1]
from Bio.Align import AlignInfo

align = AlignIO.read(filein, 'fasta')
summary_align = AlignInfo.SummaryInfo(align)

consensus = summary_align.dumb_consensus()
my_pssm = summary_align.pos_specific_score_matrix(consensus,
                                                  chars_to_ignore = ['N'])

fileout = sys.argv[1] + '.matrix.txt'
fileout2 = open(fileout, 'w')

fileout2.write('%s' %my_pssm)

fileout2.close()
