
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

count = int(len(requestedsequences))
#out_handle = open(out_file, "a")
batch_size = 1000
for start in range(0, count, batch_size):
    end = min(count, start + count)
    #batch = gi_list[start:end]
    print "Going to download record %i to %i using epost+efetch" %(start + 1, end)
    #post_results = Entrez.read(Entrez.epost("nuccore", id=",".join(batch)))
    post_results = Entrez.read(Entrez.epost("protein", id=",".join(requestedsequences)))
    webenv = post_results["WebEnv"]
    query_key = post_results["QueryKey"]
    #fetch_handle = Entrez.efetch(db="nuccore", rettype="fasta",retmode="text", webenv=webenv, query_key=query_key)
    fetch_handle = Entrez.efetch(db="protein", rettype="gb",retmode="text", webenv=webenv, query_key=query_key)
    #data = fetch_handle.read()
    records = SeqIO.parse(fetch_handle,"genbank")

    for record in records:
        fileout.write ('%s\t%s\t%s\t%s\n' %(record.annotations['gi'], record.id, record.annotations['taxonomy'], record.annotations['organism']))
print "Done"
fileout.close()

#request = Entrez.epost(db='protein', id = ",".join(requestedsequences), rettype="gb", retmode="text")
#result = Entrez.read(request)

#handle = Entrez.efetch(db="protein", id=requestedsequences, rettype="gb", retmode="text")
#records = SeqIO.parse(handle,"genbank")
##print records

