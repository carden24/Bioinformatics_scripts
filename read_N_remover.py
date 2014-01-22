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

#read_N_remover.py

#Usage: programName.py fileName outputFileName.fq [p]

#Input Parameters:
#filename.fq = original file input, sanger .fastq file
#outputFileName.fq = output file name/location

#Script Options, add after normal parameters
#p = run with paired end data, removing mate or pair if one side fails

#This program takes a .fq/.fastq file and goes through the reads,
#rejecting any with 'N' instances.

#--------------------------------------------------------------------------

#for testing
good = 0
bad = 0

#option flag handling
pair = 0
if 'p' in sys.argv or 'P' in sys.argv:
   pair = 1

#if single ended, read 4 lines at a time
if pair == 0:
   f = open(sys.argv[1])
   o = open(sys.argv[2],'w')
   while True:
      name = f.readline()
      if name == '':
         break
      seq = f.readline()
      plus = f.readline()
      qual = f.readline()
      
      #if no 'N', accept and output
      if 'N' not in seq:
         good +=1
         o.write(name+seq+plus+qual)
      else:
         bad +=1
         
#read 8 lines at a time for interleaved paired end
else:
   f = open(sys.argv[1])
   o = open(sys.argv[2],'w')
   
   while True:
      name = f.readline()
      if name == '':
         break
      seq = f.readline()
      plus = f.readline()
      qual = f.readline()
      
      name2 = f.readline()
      seq2 = f.readline()
      plus2 = f.readline()
      qual2 = f.readline()
            
      #if no 'N's in either, output to reslut file
      if 'N' not in seq and 'N' not in seq2:
         good +=1
         o.write(name+seq+plus+qual+name2+seq2+plus2+qual2)
      else:
         bad +=1        
               
f.close()
o.close()










