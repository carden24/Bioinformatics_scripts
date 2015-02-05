
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


#first get GI for query accesions
query  = " ".join(requestedsequences)
print query
handle = Entrez.esearch( db="nuccore", term=query, retmax = 10 )
giList = Entrez.read(handle)['IdList']
print giList


count = int(len(giList))
batch_size = 500

for start in range(0, count, batch_size):
    end = min(count, start + count)

    print "Going to download record %i to %i using epost+efetch" %(start + 1, end)
    post_results = Entrez.read(Entrez.epost(db="nuccore", id=",".join(giList)))
    webenv = post_results["WebEnv"]
    query_key = post_results["QueryKey"]
    fetch_handle = Entrez.efetch(db="nuccore", rettype="gb",retmode="text", webenv=webenv, query_key=query_key)
    #data = fetch_handle.read()
    records = SeqIO.parse(fetch_handle,"genbank")
    for record in records:
        fileout.write ('%s\t%s\t%s\t%s\n' %(record.annotations['gi'], record.id, record.annotations['taxonomy'], record.annotations['organism']))
print "Done"
fileout.close()

