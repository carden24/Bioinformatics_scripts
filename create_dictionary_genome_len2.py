import screed
import pickle
import sys

genome_length_dict={}
for record in screed.open(sys.argv[1]):
    leno=len(record.sequence)
    genome_length_dict[record.name]=leno
print genome_length_dict
output = open(sys.argv[2], 'wb')
pickle.dump(genome_length_dict,output)
