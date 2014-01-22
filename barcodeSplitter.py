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

#barcodeSplitter.py
   
#Usage: programName.py barcode_file.txt [p] [t] [u]

#Input Parameters:
#[t] output thrown out to a file
#[p] pair ended data
#[u] do not use T's in barcode
#Default is single ended, no rejected read output, use 'T' overhang

#This program that takes a barcode file and splits the lane sequence.txt files into specified 
#library.txt (lib#.txt) files. Note that Illumina 1.5-1.6 .txt format IS NOT sanger qualities 
#and needs converted, that is why the output should be .txt and not .fa/.fastq

#Also, running in paired ended mode will throw away both ends if one end is rejected, to keep both
#append the two raw files together and run single ended.

#This requires a barcode file with name "prefix"-barcodes
#In the barcodes file is a line for each lane, tab separated 
#in the form: lanenum<Tab>barcode1-libNum1<Tab>barcode2-libNum2<tab>...<Tab>barcodeLast-LibNumLast<EOL>

#Sample lane strings (in this case \t means tab and \n means end of line):

#File: test-barcodes.txt
#line1: 5\tAACCC-1\tCCATC-6\tGATGT-11\tGTGAG-16\n'
#line2: 7\tTTCCC-2\tGCACC-14\tAATGT-13\tATGAC-27\n'
#this barcode file would work with single ended files test-5.txt and test-7.txt,
#or paired end test-5-1.txt, test-5-2.txt, test-7-1.txt, and test-7-2.txt

#The files for each lane MUST BE in the form:
#Single-ended: prefix-laneNumber.txt
#Paired-ended: prefix-laneNumber-1.txt and prefix-laneNumber-2.txt (1 = forward, 2 = reverse)

#This program will then split the reads by barcode

#Important: 
#- if using the same barcode in two lanes, give them different library numbers, 
#	or the first lane lib#.txt will be overwritten.
#- The last line of the barcode file should end with a newline or the last 
#	charater of the last library name will be chopped off.
#- Make sure not to run two lanes carrying libraries with the same name otherwise, 
#	the data from the first lane will be overwritten when the second lane is processed. 
#- Barcode are the sequences that are present in the adaptors. This script will 
#	look for the reverse complement of that.
   
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

#Flags for single ended, 'T's or not added to barcode
#and throw out rejects to a file

single = 1
tover = 0
throw = 0

if 't' in sys.argv or 'T' in sys.argv:
   throw = 1
if 'p' in sys.argv or 'P' in sys.argv:
   single = 0
if 'u' in sys.argv or 'U' in sys.argv:
   tover = 1

prefix = sys.argv[1].split("-barcode")[0]

def run2(lane):
   #libs hold open file handlers for each barcode, is a dictionary of barcode to file
   #codes is the barcodes for the given lane
   counter = 0
   libs = {}
   codes = []
   if tover == 0:
      codes = map(lambda x:rev(str.upper(x.split('-')[0]))+'T',lane.split('\t')[1:])
   else:
      codes = map(lambda x:rev(str.upper(x.split('-')[0])),lane.split('\t')[1:])
   #get barcode length
   bar = len(codes[0])
   #open a output file for each library
   for x in map(lambda x:x.split('-'),lane.split('\t')[1:]):
      libs[str.upper(x[0])]=open("lib"+x[1]+".txt",'w')

   print codes
   #print libs   
   #open paired file
   f = open(prefix+'-'+lane.split('\t')[0]+'-1.txt')
   r = open(prefix+'-'+lane.split('\t')[0]+'-2.txt')
   #if specified open output file
   if throw == 1:
      out = open("lane_"+lane.split('\t')[0]+"_rem.txt",'w')
   count = 0
   #get file size
   for x in f:
      count+=1  
   f.seek(0)
   
   #assume illumina format
   for j in range(count/4):
      #output-status
      if j % 100000 == 8:
         print("Lane: "+lane.split('\t')[0]+"   Done: "+str(int(100*float(j)/(float(count)/4))) + '%   #Cut: '+str(counter))
      #open everything 
      test = 0      
      name = f.readline()
      seq = f.readline()
      sname = f.readline()
      sname = "+\n"
      qual = f.readline()
      sum = 0
      name2 = r.readline()
      seq2 = r.readline()
      sname2 = r.readline()
      sname2 = "+\n"
      qual2 = r.readline()
      sum2 = 0
      #trim barcode and mae sure paired ends match
      
      barF = seq[:bar]
      seq = seq[bar:]
      qual = qual[bar:]
      barR = seq2[:bar]
      seq2 = seq2[bar:]
      qual2 = qual2[bar:]
      name = name[:-1]+"_"+barF+'\n'
      name2 = name2[:-1]+"_"+barR+'\n'

      #barcodes must be equal and in the accepted list
      if barF != barR:
         test = 1
         sname = sname[:-1]+'\tMB\n'       
      if barF not in codes:
         #print barF,codes
         test = 2 
         sname = sname[:-1]+'\tB\n'
   

      #th is to output thrown out sequences
      if test == 0:
         #using the dictionary, lookup the file handler using barcode and write out
         if tover == 0:
            libs[rev(barF[:-1])].write(name+seq+sname+qual+name2+seq2+sname2+qual2)		   
         else:
            libs[rev(barF)].write(name+seq+sname+qual+name2+seq2+sname2+qual2)
      else:
         counter+=1
         if throw == 1:
            out.write(name+seq+sname+qual+name2+seq2+sname2+qual2)	
   f.close()
   r.close()
   #close all lib files
   if throw ==1:
      out.close()
   for f in libs:
      libs[f].close()

def run1(lane):
   #libs hold open file handlers for each barcode, is a dictionary of barcode to file
   #codes is the barcodes for the given lane
   #beginning is same as above
   counter = 0
   libs = {}
   codes = []
   if tover == 0:
      codes = map(lambda x:rev(str.upper(x.split('-')[0]))+'T',lane.split('\t')[1:])
   else:
      codes = map(lambda x:rev(str.upper(x.split('-')[0])),lane.split('\t')[1:])

   bar = len(codes[0])
   for x in map(lambda x:x.split('-'),lane.split('\t')[1:]):
      libs[str.upper(x[0])]=open("lib"+x[1]+".txt",'w')

   print codes
   #print libs   
   #open single file and output file
   f = open(prefix+'-'+lane.split('\t')[0]+'.txt')
   if throw == 1:
      out = open("lane_"+lane.split('\t')[0]+"_rem.txt",'w')
   count = 0
   #count file size
   for x in f:
      count+=1  
   f.seek(0)
   #for every 4 lines
   for j in range(count/4):
      if j % 100000 == 8:
         print("Lane: "+lane.split('\t')[0]+"   Done: "+str(int(100*float(j)/(float(count)/4))) + '%   #Cut: '+str(counter))
      #open everything 
      test = 0      
      name = f.readline()
      seq = f.readline()
      sname = f.readline()
      sname = "+\n"
      qual = f.readline()
      sum = 0
   
      #trim barcode and mae sure paired ends match

      barF = seq[:bar]
      seq = seq[bar:]
      qual = qual[bar:]
      name = name[:-1]+"_"+barF+'\n'

      #barcode must be accepted
      if barF not in codes:
         #print barF,codes
         test = 2 
         sname = sname[:-1]+'\tB\n'

      #th is to output thrown out sequences
      if test == 0:
         #using the dictionary, lookup the file handler using barcode and write out
         if tover == 0:
            libs[rev(barF[:-1])].write(name+seq+sname+qual)
         else:
            libs[rev(barF)].write(name+seq+sname+qual)		   
      else:
         counter+=1
         if throw == 1:
            out.write(name+seq+sname+qual)	
   #close all files
   f.close()
   if throw == 1:
      out.close()
   for f in libs:
      libs[f].close()


#read in the barcode file, and run each line
f = open(sys.argv[1])
for x in f:
   if single == 0:
      run2(x[:-1])
   else:
      run1(x[:-1])
f.close()








   

