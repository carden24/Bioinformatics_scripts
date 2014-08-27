#usage
#python retrieve.lineage.py <names_list>
# 	0			1	

from Bio import Entrez
import sys
import pickle

Entrez.email = "carden24@mail.ubc.ca"     # Always tell NCBI who you are

#input
filein = open(sys.argv[1],'r')

#output
outy = sys.argv[1]
out1 = outy +'.lineages.pkl'
fileout = open(out1, 'w')


def retrieve_annotation(id_list):
 
    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information. 
    Returns a list of dictionaries with the annotations."""
 
    request = Entrez.epost(db='taxonomy', id = ",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError as e:

        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)
    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.efetch(db="taxonomy", webenv=webEnv, query_key=queryKey)
    annotations = Entrez.read(data)
    return annotations

#Create a list with the names of the sequences requested
requested_sequences = []
for line in filein:
   line = line.strip('\n').strip('\r')
   requested_sequences.append(line)

anno = retrieve_annotation(requested_sequences)

pickle.dump(anno,fileout)

fileout.close()
filein.close()

