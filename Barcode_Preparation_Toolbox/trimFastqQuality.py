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
 
#trimFastqQuality.py

#Usage: programName.py low_quality_cutoff#(phred-score) minLength fileName.fq outputFileName.fq [t] [p]

#Input Parameters:
#low_quality_cutoff# = minimum phred score, for sliding window average quality
#*It checks all 5 base windows of the read for an average quality less than the cutoff,
#cutting at the begining of the window if it finds a bad one(scans from start of read)
#minLength = after trimming, minimum read length
#filename.fq = original file input, sanger .fastq file
#outputFileName.fq = output file name/location

#Script Options, add after normal parameters
#t = output rejected reads to "removed-"+original_file_name
#p = if the data is paired

#If you run it paired, it will discard the read mate. So if the /1 forward read is rejected
#then the /2 reverse corresponding read will be rejected also.

#This program takes a SANGER .FQ/.FASTQ file and
#trims by a quality cutoff.
#DO NOT use with unconverted raw Illumina reads.

#If trimmed to length less than min_read_length_number,
#rejects read and trimmed read does not output even if t flag is used.

#--------------------------------------------------------------------------

#all command line info
low = int(sys.argv[1])
minLength = int(sys.argv[2])
f = open(sys.argv[3])
o = open(sys.argv[4],'w')

#for testing purposes
good = 0
bad = 0
other = 0

#additional option flags
throw = 0
if 't' in sys.argv or 'T' in sys.argv:
   throw = 1
   t = open("removed-"+sys.argv[3],'w')

pair = 0
if 'p' in sys.argv or 'P' in sys.argv:
   pair = 1


#if processing single ended, read in 4 lines
if pair == 0:   
   while True:
      name = f.readline()
      if name == '':
         break
      seq = f.readline()
      plus = f.readline()
      qual = f.readline()
   
      #check average quality of read and trim if needed
#      for x in range(len(qual[:-1])):		     
#      	if ord(qual[x])-33 < low :
#      		qual = qual[0:x] + '\n'
#      		seq = seq[0:x] + '\n'
#      		break			
      quals = map(lambda x: ord(x)-33, qual[:-1])
      for x in range(len(quals)-4):
         cut = quals[x:x+5]
         ave = float(sum(cut))/5.0
         if ave < 20.0:
            qual = qual[:x]+'\n'
            seq = seq[:x]+'\n'
            break
      #check that chopped length is not too small
      #if too small and option set send to throw out file
      #otherwise write to output file
      if len(seq) >= minLength: 
         good +=1
         o.write(name+seq+plus+qual)
      else:
         bad +=1
         if throw == 1:
            t.write(name+seq+plus+qual)
#otherwise, if processing paired end
else:   
   #read in 8 lines at a time from interleaves sanger file
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
      
      #check average quality of read and trim if needed		
#      for x in range(len(qual[:-1])):		     
#      	if ord(qual[x])-33 < 20:
#      		qual = qual[0:x] + '\n'
#      		seq = seq[0:x] + '\n'
#      		break		
#
#      for x in range(len(qual2[:-1])):
#      	if ord(qual2[x])-33 < 20:
#      		qual2 = qual2[0:x] + '\n'
#      		seq2 = seq2[0:x] + '\n'
#      		break		
      quals = map(lambda x: ord(x)-33, qual[:-1])
      for x in range(len(quals)-4):
         cut = quals[x:x+5]
         ave = float(sum(cut))/5.0
         if ave < 20.0:
            qual = qual[:x]+'\n'
            seq = seq[:x]+'\n'
            break
      quals2 = map(lambda x: ord(x)-33, qual2[:-1])
      for x in range(len(quals2)-4):
         cut2 = quals2[x:x+5]
         ave2 = float(sum(cut2))/5.0
         if ave2 < 20.0:
            qual2 = qual2[:x]+'\n'
            seq2 = seq2[:x]+'\n'
            break
      #check that chopped length is not too small
      #if too small and option set send to throw out file
      #otherwise write to output file
      if len(seq) >= minLength and len(seq2) >= minLength: 
         good +=1
         o.write(name+seq+plus+qual+name2+seq2+plus2+qual2)
      elif len(seq) >= minLength or len(seq2) >= minLength:
         other +=1
         if throw == 1:
            t.write(name+seq+plus+qual+name2+seq2+plus2+qual2)
      else:
         bad +=1
         if throw == 1:
            t.write(name+seq+plus+qual+name2+seq2+plus2+qual2)
            
#close open file descriptors  
f.close()
o.close()
if throw == 1:
   t.close()




