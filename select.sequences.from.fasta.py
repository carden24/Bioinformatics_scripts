#usage
#python fastaselection2.py <originalfile.nucleotide.fasta> <otu.list.file>
# 	0			1				2		

import sys, screed

#inputs
filein=open(sys.argv[1],'r')
filelist=open(sys.argv[2],'r')

#outputs
outy=sys.argv[1]
out1=outy+'.subselection'
fileout=open(out1,'w')

# create group of list

#groups of lists=[]
for line in filelist:
   line1=line.split(' ')
   print line1

 
for i in line1:
   if i.startswith('\s'):
      continue
   else:
      requested=i.split(',')
      outy=sys.argv[1]
      out1=outy+'_'+str(requested[0])
      fileout=open(out1,'w')

      for record in screed.open(sys.argv[1]):
         sequence_name=record.name			#get sequence name
         if sequence_name in requested:
            sequence=record.sequence
#            description=record.description
            fileout.write(">%s\n%s\n" %(sequence_name, sequence))
         else:
            continue
fileout.close()           
