#usage python score.blast.py <dictionary.file> <blast.output> <out.file.base>
#        	0		1		2		3	

import pickle
import sys

filedict = open(sys.argv[1], 'rb')
filein = open(sys.argv[2], 'r')
outy = sys.argv[3]
out1 = outy + '.annotated.out'
fileout1 = open(out1, 'w')

cazy_or_foly_dict = pickle.load(filedict)

for line in filein:
   print line
   line = line.lstrip(" ")
   line = line.rstrip("\n ")
   line = line.split('\t')
   subject_count = line[0]			#get subject count
   subject = line[1]				#get subject
   print subject
   dict_entry = cazy_or_foly_dict.get(subject)	#get info for subject in dictionary
   gi_line  = dict_entry[0]
   gi_line = gi_line.split('|')
   gi = gi_line[1]
   cazy_class = dict_entry[1]		#obtain class
   cazy_family = dict_entry[2]		#obtain family
   fileout1.write ("%s\t%s\t%s\t%s\n" %(sys.argv[3], gi, cazy_family, cazy_class))

fileout1.close()
filein.close()
filedict.close()
