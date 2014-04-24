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

#countAllBarcodes-RAW.py

#use: countAllBarcodes.py readFile.txt

#This program counts all barcodes in a raw illumina "@SOLEXA" and "@HWI-" sequenced
#file and outputs the counts of the barcodes in descending order.

#Input Parameters:
#readFile.txt = original read file input, sinlge ended running only.

#For paired end data, run on each side individually or append files together. 

#--------------------------------------------------------------------------


#for reverse complement
def comp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'R': 'R', 'Y': 'Y', 'S': 'S', 'W': 'W', 'M': 'M', 'K': 'K'}
    complseq = [complement[base] for base in seq]
    return complseq

def rev(seq):
    seq = list(seq)
    seq.reverse()
    return ''.join(comp(seq))


f = open(sys.argv[1])
bar = {}

#read in 4 lines(one read) at a time, adding each barcode
#to the result dictionary
while True:
   n1 = f.readline()
   if n1 == "":
      break
   seq = f.readline()
   n2 = f.readline()
   seqq = f.readline()
   if n1[:7] == "@SOLEXA" or n1[:5] == "@HWI-":
      #l = x.split("#0/")
      #if 'N' not in l[1][2:-1]:
      try:
         bar[seq[:5]] += 1
      except:
         bar[seq[:5]] = 1
#sort the dictionary, giving the barcodes in 
#decending order
   
new = []
for x in bar:
   new.append([x, bar[x]])

new.sort(lambda x, y: cmp( y[1], x[1] ) )

#output barcode counts
o = open("counted-"+sys.argv[1],'w')
for x in new:
   o.write(rev(x[0])+'\t'+str(x[1])+'\n')

o.close()
f.close()
