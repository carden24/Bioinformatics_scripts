#this need to be adapted to the particular genome

#usage 
#python retrieve.genbank.record.py <list.of.sequences.requested> <output.fa>
# 	0					1			2

import sys
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "carden24@mail.ubc.ca"

#inputs
filelist=open(sys.argv[1],'r')

#output
fileout=open(sys.argv[2],'w')


#create a list with the names of the sequences requested
requestedsequences=[]
for line in filelist:
   line=line.strip('\n')
   requestedsequences.append(line)
print "%d Sequences requested" % len(requestedsequences)
print requestedsequences


handle = Entrez.efetch(db="protein", id=requestedsequences, rettype="gb", retmode="text")
records=SeqIO.parse(handle,"genbank")

for record in records:
   feat=record.features
   for f in feat:
      if f.type=="CDS":
         quali=f.qualifiers
         gene=str(quali.get('gene','no_gene_name'))
         gene=gene.strip('\'[]')
         locus=str(quali.get('locus_tag','no_locus_tag'))
         locus=locus.strip('\'[]')
         old_locus=str(quali.get('old_locus_tag','no_old_locus_tag'))
         old_locus=old_locus.strip('\'[]')
         product=str(quali.get('product','no_product_name'))
         product=product.strip('\'[]')
         protein_id=str(quali.get('protein_id','no_protein_id'))
         protein_id=protein_id.strip('\'[]')
         fileout.write("%s\t%s\t%s\t%s\t%s\n" %(gene,locus,old_locus,product,protein_id))
      else:
         continue
fileout.close()
filelist.close()
