#usage python create.max.bits.dictionary.py <input.file> <output.file>


import pickle
import sys

max_bits_dictionary={}

filein=open(sys.argv[1],'r')
fileout=open(sys.argv[2],'w')

for line in filein:
    line=line.split('\t')
    subject=line[1]
    maxbits=float(line[11])
    max_bits_dictionary[subject]=maxbits

pickle.dump(max_bits_dictionary,fileout)
