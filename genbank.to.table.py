#usage python genbank.to.table.py <genbank.input>
#        	0			       1


import sys, screed, pickle

filein=open(sys.argv[1],'r')

out0=str(sys.argv[1])
out00=out0.split('.')
out000=out00[0]+'.xls'

fileout=open(out000,'w')

from Bio import SeqIO
for seq_record in  SeqIO.parse(filein, "genbank"):
   feat=seq_record.features
   for f in feat:
      if f.type=="CDS":
         location = str(f.location)
         loca=location.strip('[]\'')
         product = str(f.qualifiers['product'])
         prod=product.strip('[]\'')
         locus = str(f.qualifiers['locus_tag'])
         loc=locus.strip('[]\'')
         fileout.write("%s\t%s\t%s\n" %(loc,loca,prod))

