#usage
#python retrieve.lineage.py <namelist>
# 	0			1	

from Bio import Entrez
import sys, screed

Entrez.email = "carden24@mail.ubc.ca"     # Always tell NCBI who you are

#input
filein=open(sys.argv[1],'r')

#output
outy=sys.argv[1]
out1=outy+'.lineages.txt'
fileout=open(out1,'w')


#create a list with the names of the sequences requested
requestedsequences=[]
for line in filein:
   line=line.strip('\n').strip('\r')
   requestedsequences.append(line)

number_records=len(requestedsequences)
print "%s records requested" % number_records

for query in requestedsequences:
   handle = Entrez.efetch(db="Taxonomy", id=query, retmode="xml")
   print query
   records = Entrez.read(handle)
   lineage=records[0]["Lineage"]
   fileout.write("%s\t%s\n" %(query, lineage))

fileout.close()
filein.close()

