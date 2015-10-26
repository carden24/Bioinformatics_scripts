#usage
#python fasta.to.stockholm.py <input.file.fasta> <output.file.sto>
#		0			1		2

import sys
from Bio import AlignIO

#input
filein = open(sys.argv[1], "r")

#outputs
fileout = open(sys.argv[2], 'w')


AlignIO.convert(filein, "fasta", fileout, "stockholm")

