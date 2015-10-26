#usage 
#python retrieve_taxonomy_from_gis.py <list.of.sequences.requested> <output.fa>
# 	0					1			2

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
print "%d Sequence(s) requested" % len(requestedsequences)
print ''


handle = Entrez.efetch(db="protein", id=requestedsequences, rettype="gb", retmode="text")
records = SeqIO.parse(handle, "genbank")
##print records

for record in records:
#   print record.id
   fileout.write ('%s\t%s\t%s\t%s\n' %(record.annotations['gi'], record.id, record.annotations['taxonomy'], record.annotations['organism']))
   #print record.name
   #print record.seq
   #print record.features
 #  print record.annotations['taxonomy']
  # print record.annotations['organism']

##request = Entrez.epost(db='protein', id = ",".join(requestedsequences), rettype="gb", retmode="text")
##result = Entrez.read(request)

#try:
#    result = Entrez.read(request)
#except RuntimeError as e:
#    #FIXME: How generate NAs instead of causing an error with invalid IDs?
#    print "An error occurred while retrieving the annotations."
#    print "The error returned was %s" % e
#    sys.exit(-1)
##webEnv = result["WebEnv"]
##queryKey = result["QueryKey"]
#data = Entrez.efetch(db="protein", webenv=webEnv, query_key=queryKey, retmode="text")
##data = Entrez.efetch(db="protein", webenv=webEnv, query_key=queryKey, rettype="gb", retmode="text")
##print data
#records = SeqIO.parse(data,"genbank")
#annotations = Entrez.read(data)
#print records

fileout.close()

