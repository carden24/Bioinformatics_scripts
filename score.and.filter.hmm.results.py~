
#usage python score.and.filter.hmm.results.py <hmmr.tabular.output>
#        	0			        1		

import sys

filein=open(sys.argv[1],'r')
outy=sys.argv[1]
output=outy+'.score.txt'
fileout=open(output,'w')


read_dictionary={}
KO_dictionary={}


for line in filein:
   if line.startswith('#'):
      continue
   else:
      line1=line.split(' ')
      query=line1[0]
      subject=line1[2]
      domain_score=line1[8]
      current_value=read_dictionary.get(query,[0,0])	#get evalue 
      if domain_score > current_value[1]:  
         new_result=[subject,domain_score]         
         read_dictionary[query]=new_result		#update entry in dictionary
      else:
         continue

#process read_dictionary to count 

for value in read_dictionary.itervalues():
      KO=value[0]
      KO_count=KO_dictionary.get(KO,0)		#find  KO count, if absent none count is zero
      New_KO_count=KO_count+1			#update count
      KO_dictionary[KO]=New_KO_count		#update entry in dictionary


#write KO_dictionary
fileout.write("%s\n" %(sys.argv[1]))

for key1, value1 in KO_dictionary.iteritems():
   fileout.write("%s\t%d\n" %(key1,value1))

fileout.close()
filein.close()

