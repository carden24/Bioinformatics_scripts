import pickle
import sys

filein = sys.argv[1]
fileout = sys.argv[2]

fw = open(fileout, 'w')

#1. create dictionary with lenght for each genome

#file3     = open(filein,'r')

genome_length_dict={}
for line in file3:
    line=line.rstrip().split('\t')
    genome2=line[1]
    length2=line[0]
    if genome_length_dict.has_key(length2):
        genome_length_dict[length2].append(genome2)
    else:
        genome_length_dict[length2]=[genome2]
#print genome_length_dict

output = open(fileout, 'wb')
pickle.dump(genome_length_dict,output)

#################################################
