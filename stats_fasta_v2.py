#!/usr/bin/python

#usage
#python fasta.stats.v2.py <filein>

import sys
import Bio
from Bio import SeqIO
import numpy

filein=open(sys.argv[1],'r')

counter=0
total_len=[]

for seq_record in SeqIO.parse(filein, format="fasta"):
   len_seq=len(seq_record.seq)
   total_len.append(len_seq)
   counter=counter+1

#histo=numpy.histogram(total_len)
#print histo

len_sum=numpy.sum(total_len)
#print len_sum

average_len=len_sum/float(counter)
#print average_len

median_len=numpy.median(total_len)

print 'Reads found: %s' %counter
print 'Total bases: %s' % len_sum
print 'Average read length: %s' %average_len
print 'Median read length: %s' %median_len



