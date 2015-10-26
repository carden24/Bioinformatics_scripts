#usage python find.unique.contigs.hit.py <blast.file> <out>
#        	0			        1	2

import sys 

out1 = sys.argv[2]
fileout = open(out1,'w')

contiglist = []
for line in open (sys.argv[1]):
   line = line.split('\t')
   contig0 = line[0]
   contig1 = contig0.split('_')
   contig2 = contig1[0]
   contiglist.append(contig2)

lista = set(contiglist)
#print lista

contigdict={}
for member in lista:
   contigdict[member]=contiglist.count(member)

for key in contigdict:
   firstcol = key
   secondcol = contigdict.get(key)
   fileout.write ('%s\t%s\n' %(firstcol , secondcol))
#fileout.write('%s' %contiglist)
   
   

