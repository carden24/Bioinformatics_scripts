#!/usr/bin/python
# File created on 13 Feb 2014.
from __future__ import division

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"



#creates dictionary file stored in pickle file


#usage python create.cazy.dictionary.py <maxbitsfile> <csv.file> <output.pkl.file>
#        	0				1		2		3	

import pickle
import sys
import csv

max_bits_dict={}

filemaxbitsin=open(sys.argv[1],'r')





for line in filemaxbitsin:
   line=line.split('\t')
   subject1=line[1]
   maxbits1=float(line[11])
   max_bits_dict[subject1]=maxbits1

filein=open(sys.argv[2],'r')
fileout=open(sys.argv[3],'w')

folydict={}

for row in csv.reader(filein):
   subject=row[0]
   description=row[1]
   foly1=row[2]
   foly2=row[3]
   maxbits=max_bits_dict.get(subject) 
   print maxbits   
   x=folydict.get(subject, [])
   x.append(description)
   x.append(foly1)
   x.append(foly2)
   x.append(maxbits)
   folydict[subject]=x

#print folydict
pickle.dump(folydict,fileout)

