
import sys
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "carden24@mail.ubc.ca"


# Inputs
filelist = open(sys.argv[1], 'r')

# Output
out1 = sys.argv[1] + '.lineages.txt'
fileout = open(out1, 'w')

# Create a list with the names of the sequences requested
requestedsequences = []
for line in filelist:
   line = line.strip('\n')
   line = line.strip('\r')
   requestedsequences.append(line)
print requestedsequences
print "%d Sequence(s) requested" % len(requestedsequences)
print ''

handle = Entrez.efetch(db="nuccore", id=requestedsequences, rettype="gb", retmode="text")
records = SeqIO.parse(handle,"genbank")

for record in records:
#   print record.id
   fileout.write ('%s\t%s\t%s\t%s\n' %(record.annotations['gi'], record.id, record.annotations['taxonomy'], record.annotations['organism']))

print "Done"
fileout.close()

