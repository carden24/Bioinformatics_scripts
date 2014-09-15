# Usage python ./score.blast.py <dictionary.file> <blast.output> <out.file.base>
#		0		1			2		3	

import pickle
import sys

#threshold=float(0.4)
filedict = open(sys.argv[1], 'rb')
filein = open(sys.argv[2], 'r')
outy = sys.argv[3]
out1 = outy + 'family.out'
out2 = outy + 'subfamily.out'
out3 = outy + 'detailed'

fileout1 = open(out1, 'w')
fileout2 = open(out2, 'w')
fileout3 = open(out2, 'w')

cazy_or_foly_dict = pickle.load(filedict)
familydict = {}
subfamilydict = {}


for line in filein:
   # Split line from fasta
   line = line.split('\t')
   # Get query
   query = line[0]
   # Get evalue
   evalue = line[10]
   # Get subject
   subject = line[1]
   # Get info for subject in dictionary
   dict_entry = cazy_or_foly_dict.get(subject)
   # Obtain family
   family = dict_entry[2]
   # Entry family name in new dictionary, if absent use 0 if not get count
   fff = familydict.get(family,0)
   # Update count
   ggg = fff + 1
   # Update entry in dictionary				
   familydict[family] = ggg
   # Do the same for subfamily
   subfamily = dict_entry[1]
   sss = subfamilydict.get(subfamily, 0)
   ttt = sss + 1
   subfamilydict[subfamily] = ttt
   
   write.fileout3('%s\t%s\t%s\t%s\t%s\n' %(query, subject, family, subfamily, evalue))


#write familydict dictionary
for key1, value1 in familydict.iteritems():
   fileout1.write("%s\t%d\n" %(key1, value1))

#write subfamily dictionary
for key2, value2 in subfamilydict.iteritems():
   fileout2.write("%s\t%d\n" %(key2, value2))

