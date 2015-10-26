

#usage python score.blast.py <dictionary.file> <blast.output> <out.file.base>
#usage python score.blast.py <dictionary.file> <blast.count.file> <out.file.base>
#        	0		1		2		3	

import pickle
import sys

#threshold=float(0.4)
filedict = open(sys.argv[1], 'rb')
filein = open(sys.argv[2], 'r')
outy = sys.argv[3]
out1 = outy + '.family.out'
fileout1 = open(out1, 'w')

cazy_or_foly_dict = pickle.load(filedict)
subfamilydict = {}


for line in filein:
   line = line.lstrip(" ")
   line = line.rstrip("\n ")
   line = line.split(' ')			#split line from fasta
   subject_count = line[0]			#get subject count
   subject = line[1]				#get subject
   dict_entry = cazy_or_foly_dict.get(subject)	#get info for subject in dictionary
   family = dict_entry[1]				#obtain family
#   print subject
#   print subject_count
#   print family
   fileout1.write("%s\t%s\t%s\n" %(subject, subject_count, family))
fileout1.close()
filein.close()
filedict.close()
