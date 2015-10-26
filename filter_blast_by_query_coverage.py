
#usage python filter.blast.by.query.coverage.py <blast.result> <output>
#        	0		        1		2	


import sys

filein = open(sys.argv[1], 'r')
out1 = sys.argv[2]

fileout = open(out1, 'w')

#blast output
#HS6_179:1:1101:10145:166587/1	gi|49642693|emb|CAH00655.1|	58.33	   24	4e-04	35.0	79
#qsid 				ssid				 %identity query.len	subject.len	alignment.len	evalue  bits   score
# 0 				1				2	   3   		4      		  5     	  6	7	8


for line in filein:
   output = line   
   line = line.split('\t')			#split line from blast output
   query_len = float(line[3])		 	#get query lenght
   alignment_len = float(line[5])			#get alignment length
   query_coverage = alignment_len / query_len	#get query coverage
   print query_len
   print alignment_len
   print query_coverage
   if query_coverage >= 0.7:
      fileout.write ('%s' %output)
   else:
      continue


filein.close()
filein.out()
