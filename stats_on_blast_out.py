#usage python stats.on.blast.out.py <blast.output> <results>
#        	0		        1		2	

import numpy
import sys

filein=open(sys.argv[1],'r')

out1=sys.argv[2]
fileout=open(out1,'w')

all_perc_ident=[]
all_len=[]
all_evalue=[] #careful with scientific numbers here
all_bits=[]

#blast output
#HS6_179:1:1101:10145:166587/1	gi|49642693|emb|CAH00655.1|	58.33	   24	4e-04	35.0	79
#qsid 				ssid				 %identity len evalue   bits    score
# 0 				1				2	   3   4         5       6


for line in filein:
   line=line.split('\t')		#split line from blast output
   perc_ident=float(line[2])		#get percent identity
   lengths=int(line[3])                 #get lengths
   evalue=float(line[4])		#get evalue
   bits=float(line[5])			#get bits
   all_perc_ident.append(perc_ident)	#append to lists
   all_len.append(lengths)
   all_evalue.append(evalue)
   all_bits.append(bits)

mean1=numpy.average(all_perc_ident)
median1=numpy.median(all_perc_ident)
std1=numpy.std(all_perc_ident)
mini1=min(all_perc_ident)
maxi1=max(all_perc_ident)

mean2=numpy.average(all_len)
median2=numpy.median(all_len)
std2=numpy.std(all_len)
mini2=min(all_len)
maxi2=max(all_len)

mean3=numpy.average(all_evalue)
median3=numpy.median(all_evalue)
std3=numpy.std(all_evalue)
mini3=min(all_evalue)
maxi3=max(all_evalue)

mean4=numpy.average(all_bits)
median4=numpy.median(all_bits)
std4=numpy.std(all_bits)
mini4=min(all_bits)
maxi4=max(all_bits)

fileout.write("%s\n" %(sys.argv[1]))
fileout.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("Variable ","Mean","Median","St.dev","Min.","Max"))
fileout.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("Identity(%)",mean1,median1,std1,mini1,maxi1))
fileout.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("Length",mean2,median2,std2,mini2,maxi2))
fileout.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("E.value",mean3,median3,std3,mini3,maxi3))
fileout.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("Bits.score",mean4,median4,std4,mini4,maxi4))

