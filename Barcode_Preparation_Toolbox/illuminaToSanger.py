#! /usr/bin/env python

#Comai Lab, Ucdavis Genome Center
#Meric Lieberman, 2011
# This work is the property of UC Davis Genome Center - Comai Lab

# Use at your own risk. 
# We cannot provide support.
# All information obtained/inferred with this script is without any 
# implied warranty of fitness for any purpose or use whatsoever. 
#------------------------------------------------------------------------------

import os, sys, math

#illuminaToSanger.py

#Usage: programName.py fileName outputFileName.fq

#Input Parameters:
#filename: the filename/location of the illumina file to convert
#outputFileName: the destination filename/location of the result


#This program convers an illumina 1.5+ .txt file to
#a sanger .fq/.fastq format (phred+33 scaling)
 
#--------------------------------------------------------------------------


#open file, read 4 lines at a time
f = open(sys.argv[1])
o = open(sys.argv[2],'w')
while True:
   name = f.readline()
   if name == '':
      break
   seq = f.readline()
   name2 = f.readline()
   oldQual = f.readline()
   #illumina uses Phred + 64, sanger uses Phred+33, so illumina_score - 31 = sanger score
   newQual = "".join(map((lambda x: chr(ord(x)-31)),oldQual[:-1]))+'\n'
   #write to specified file
   o.write(name+seq+name2+newQual)
   
f.close()
o.close()