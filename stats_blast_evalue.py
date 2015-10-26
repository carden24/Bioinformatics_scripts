#usage python stats_blast_evalue.py <blast.output> 
#        	0		        1		
#Assumes that the evalue column is the eleventh

import numpy
import sys

filein = open(sys.argv[1],'r')

all_evalue=[] #careful with scientific numbers here

for line in filein:
    #split line from blast output
    line=line.split('\t')		
    if len(line) == 21:
        print line
    else:
      #get evalue
        evalue = float (line[10])
        all_evalue.append(evalue)

histo=numpy.histogram(all_evalue,bins=[1e-60,1e-55,1e-50,1e-45,1e-40,1e-35,1e-30,1e-25,1e-20,1e-15,1e-10,1e-5])

print histo

