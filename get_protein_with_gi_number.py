#usage 
#python retrieve_protein_with_gi_number.py <list.of.sequences.requested> <output.fa>
# 	0					1			2

import sys
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "carden24@mail.ubc.ca"

#inputs
filelist = open(sys.argv[1], 'r')

#output
fileout = open(sys.argv[2], 'w')


#create a list with the names of the sequences requested
requestedsequences = []
for line in filelist:
   line = line.strip('\n')
   requestedsequences.append(line)
print "%d Sequences requested" % len(requestedsequences)
print requestedsequences


#handle = Entrez.efetch(db="protein", id=requestedsequences, rettype="gb", retmode="text")
handle = Entrez.efetch(db = "protein", id = requestedsequences, rettype = "fasta", retmode = "text")
records = SeqIO.parse(handle, "fasta")

for record in records:
#   print record.id
#   print record.seq
   fileout.write(">%s\n%s\n" %(record.id, record.seq))

handle.close()
fileout.close()

