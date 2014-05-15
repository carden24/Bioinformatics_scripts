#usage python evalue.stats.py <blast.output> <results>
#        	0		        1		2	

import numpy
import sys

filein=open(sys.argv[1],'r')
#fileout=open(sys.argv[2],'w')

all_evalue=[] #careful with scientific numbers here



for line in filein:
#   print line
   line=line.split('\t')		#split line from blast output
#   print len(line)
   if len(line)==21:
      print line
   else:
      evalue=float(line[10])		#get evalue
      all_evalue.append(evalue)


#for running tests
#all_evalue=[1e-25,1e-15,1e-6,2e-25,1e-9,1e-4] 



#histo=numpy.histogram(all_evalue,bins=[1e-20,1e-19,1e-18,1e-17,1e-16,1e-15,1e-14,1e-13,1e-12,1e-11,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5])
histo=numpy.histogram(all_evalue,bins=[1e-60,1e-55,1e-50,1e-45,1e-40,1e-35,1e-30,1e-25,1e-20,1e-15,1e-10,1e-5])
#histo=numpy.histogram(all_evalue,bins=[1e-60,1e-58,1e-56,1e-54,1e-52,1e-50,1e-48,1e-46,1e-44,1e-42,1e-40,1e-38,1e-36,1e-34,1e-32,1e-30,1e-28,1e-26,1e-24,1e-22,1e-20,1e-18,1e-16,1e-14,1e-12,1e-10,1e-8,1e-6,1e-4])



print histo




