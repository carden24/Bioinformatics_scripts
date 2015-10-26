#usage python score.blast.py <dictionary.file> <blast.output> <out.file.base>
#        	0		1		2		3	

import pickle
import sys

threshold = float(0.4)
filedict = open(sys.argv[1], 'rb')
filein = open(sys.argv[2], 'r')

outy = sys.argv[3]
out1 = outy + 'family.out'
out2 = outy + 'subfamily.out'

fileout1 = open(out1, 'w')
fileout2 = open(out2, 'w')

cazy_or_foly_dict = pickle.load(filedict)
familydict = {}
subfamilydict = {}

#blast output
#HS6_179:1:1101:10145:166587/1	gi|49642693|emb|CAH00655.1|	58.33	   24	4e-04	35.0	79
#qsid 				ssid				 %identity len evalue   bits    score
# 0 				1				2	   3   4         5       6



for line in filein:
   line = line.split('\t')			#split line from blast output
   subject = line[1]				#get subject
   bits = float(line[6])				#get raw score
   dict_entry = cazy_or_foly_dict.get(subject)	#get info for subject in dictionary
   maxbits = float(dict_entry[3])			#get maximum raw score ratio for the subject vs itself
   scoreratio = bits/float(maxbits)		#calculate bits score ratio
   if scoreratio >= threshold:			#if bits score ratio is higher than treshold
      family = dict_entry[2]			#obtain family
      fff = familydict.get(family, 0)		#Entry family name in new dictionary, if absent use 0 if not get count
      ggg = fff + 1					#update count
      familydict[family] = ggg			#update entry in dictionary
      subfamily = dict_entry[1]			#do the same for subfamily
      sss = subfamilydict.get(subfamily, 0)
      ttt = sss + 1
      subfamilydict[subfamily] = ttt
   else:
      continue

#write familydict dictionary
for key1, value1 in familydict.iteritems():
   fileout1.write("%s\t%s\n" %(key1, value1))

#write subfamily dictionary
for key2, value2 in subfamilydict.iteritems():
   fileout2.write("%s\t%s\n" %(key2, value2))

