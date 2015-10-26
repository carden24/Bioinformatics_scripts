#usage
#python fastaselection2.py <originalfile.fasta> name.iteself
# 	0			1		2		

import sys, screed

#inputs
filein = open(sys.argv[1], 'r')
name = sys.argv[2]

#outputs
outy = sys.argv[1]
out1 = outy + '.' + name + '.fasta'

fileout = open(out1, 'w')


#read file, read each record, if name is in list write it, otherwise continue
for record in screed.open(sys.argv[1]):
   sequence_name = record.name			#get sequence name
   if sequence_name == name:
      description = record.description
      sequence = record.sequence      
      print "Records found"
      fileout.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
   else:
      continue

fileout.close()
filein.close()
