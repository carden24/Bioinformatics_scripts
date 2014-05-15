#usage python score.OTU.from.fasta.py <file.fasta>
#        	0			        1		

import sys

filein=open(sys.argv[1],'r')
outy=sys.argv[1]


#split sample according to unique 
unique_sample=[]
for line in filein:
   line0=line.split(',')
   sample=line0[0]
   if sample in unique_sample:
     continue
   else:
      unique_sample.append(sample)
#   list0=set(unique_sample)
#   list1=list(list0)


#print unique_sample
counter=0
while counter<=len(unique_sample):
   sample_name=unique_sample[counter]
   for line in filein:
      print line
      line0=line.split(',')
      print line0      
      sample=line0[0]
      print sample
      if sample==sample_name:
         OTU=line0[1]
         out=sample_name+'.txt'
         fileout=open(out,'w')
         fileout.write(("%s" %(line)))
counter=counter+1
