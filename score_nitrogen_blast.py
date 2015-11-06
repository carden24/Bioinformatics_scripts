# Usage python ./score_nitrogen_blast.py <dictionary.file> <blast.output> <out.file.base>
#		0			1			2		3	

import pickle
import sys

filedict = open(sys.argv[1], 'rb')
filein = open(sys.argv[2], 'r')
outy = sys.argv[3]
out1 = outy + '_cluster.txt'
out2 = outy + '_taxonomy.txt'
out3 = outy + '_detailed.txt'

fileout1 = open(out1, 'w')
fileout2 = open(out2, 'w')
fileout3 = open(out3, 'w')

nitrogen_dict = pickle.load(filedict)
cluster_dict = {}
taxonomy_dict = {}


for line in filein:
   # Split line from fasta
   line = line.split('\t')
   # Get query
   query = line[0]
   # Get evalue
   evalue = line[10]
   # Get subject
   subject = line[1]
   # Get similarity
   similarity = line[2]
   # Get bits
   bits = line[11]

   # Get info for subject in nitrogen  dictionary
   dict_entry = nitrogen_dict.get(subject)


   # Obtain cluster
   cluster = dict_entry[1]
   # Entry family name in new dictionary, if absent use 0 if not get count
   fff = cluster_dict.get(cluster, 0)
   # Update count
   ggg = fff + 1
   # Update entry in dictionary				
   cluster_dict[cluster] = ggg

   # Do the same for taxonomy
   taxonomy  = dict_entry[2]
   sss = taxonomy_dict.get(taxonomy, 0)
   ttt = sss + 1
   taxonomy_dict[taxonomy] = ttt

   fileout3.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(query, subject, evalue, bits, cluster, taxonomy, similarity))


#write cluster_dict dictionary
for key1, value1 in cluster_dict.iteritems():
   fileout1.write("%s\t%s\t%d\n" %(sys.argv[2], key1, value1))

#write taxonomy_family dictionary
for key2, value2 in taxonomy_dict.iteritems():
   fileout2.write("%s\t%s\t%d\n" %(sys.argv[2], key2, value2))

fileout1.close()
fileout2.close()
fileout3.close()
