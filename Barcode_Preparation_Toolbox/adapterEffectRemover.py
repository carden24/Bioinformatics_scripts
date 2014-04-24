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

#adapterEffectRemover.py

#Usage: programName.py minLength fileName outputFileName.fq [p] [b]

#Input Parameters:
#minLength = after trimming, minimum read length
#filename.fq = original file input, sanger .fastq file
#outputFileName.fq = output file name/location

#Script Options, add after normal parameters
#b = data does not use barcodes
#p = run with paired end data, reoving mate or pair if one side fails


#This should be used with interleaved paired-ended data.

#This program takes a .fq/.fastq file an looks for adapter contamination
#adapter is then removed, if read is shorter than specified minLength
#the read is rejected.

#--------------------------------------------------------------------------

#reverse complement
def comp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'R': 'R', 'Y': 'Y', 'S': 'S', 'W': 'W', 'M': 'M', 'K': 'K'}
    complseq = [complement[base] for base in seq]
    return complseq

def rev(seq):
    seq = list(seq)
    seq.reverse()
    return ''.join(comp(seq))

#Adapter to look for
solAd1 = "AGATCGGAAG"
solB = "AGATCGGAAGAGC"

#command line info
minLength = int(sys.argv[1])
f = open(sys.argv[2])
o = open(sys.argv[3],'w')

#additoanl option behavior flags
pair = 0
barcode = 1

if 'p' in sys.argv or 'P' in sys.argv:
   pair = 1

if 'b' in sys.argv or 'B' in sys.argv:
   barcode = 0

#for testing
good = 0
bad = 0
other = 0

#if singled ended, read 4 lines at a time
if pair == 0:
   while True:
      name = f.readline()
      if name == '':
         break
      seq = f.readline()
      plus = f.readline()
      qual = f.readline()
      
      if barcode == 1:
         barF = name[-7:-1]
         #check for main type of adapter contamination and trim as needed
         if rev(barF[:-1])+solB in seq:
            t1 = seq[:seq.index(rev(barF[:-1])+solB)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'
         
      #check for secondary adapter contam, trim as needed
      if solAd1 in seq:
         t1 = seq[:seq.index(solAd1)]
         l1 = len(t1)          
         seq = t1+'\n'
         qual = qual[:l1]+'\n'     	
   		
      #check that chopped length is not too small
      #if too small and option set send to throw out file
      #otherwise write to output file
      if len(seq) > minLength: 
         good +=1
         o.write(name+seq+plus+qual)
      else:
         bad +=1
#if pair ended read 8 lines at a time from interleaved sanger fastq
else:
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
      
      if barcode == 1:
         barF = name[-7:-1]
         barR = name[-7:-1]
      		
         #check for main type of adapter contamination and trim as needed
         if rev(barF[:-1])+solB in seq:
            t1 = seq[:seq.index(rev(barF[:-1])+solB)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'
         if rev(barR[:-1])+solB in seq2:
            t2 = seq2[:seq2.index(rev(barR[:-1])+solB)]
            l2 = len(t2)          
            seq2 = t2+'\n'
            qual2 = qual2[:l2]+'\n'         
            
      #check for secondary adapter contam, trim as needed
      if solAd1 in seq:
         t1 = seq[:seq.index(solAd1)]
         l1 = len(t1)          
         seq = t1+'\n'
         qual = qual[:l1]+'\n'         
      #if single == 0:
      if solAd1 in seq2:
         t2 = seq2[:seq2.index(solAd1)]
         l2 = len(t2)          
         seq2 = t2+'\n'
         qual2 = qual2[:l2]+'\n'  
         
      #check that chopped length is not too small
      #if too small and option set send to throw out file
      #otherwise write to output file, other elif and else 
      #for testing purpose counts
      if len(seq) > minLength and len(seq2) > minLength:
         good +=1 
         o.write(name+seq+plus+qual+name2+seq2+plus2+qual2)
      elif len(seq) > minLength or len(seq2) > minLength:
         other+=1
      else:
         bad +=1
         
f.close()
o.close()
