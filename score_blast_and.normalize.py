#usage python score.blast.and.normalize.py <dictionary.file> <assembly.dictionary> <blast.output> <out.file.base>
#        	0				1		2			3		4


import pickle
import sys

filedict=open(sys.argv[1],'rb')
filein=open(sys.argv[3],'r')
fileassembly_dict=open(sys.argv[2],'r')

outy=sys.argv[4]
out1=outy+'family.out'
out2=outy+'subfamily.out'
fileout1=open(out1,'w')
fileout2=open(out2,'w')

cazy_or_foly_dict = pickle.load(filedict)
assembly_dict = pickle.load(fileassembly_dict)

familydict={}
subfamilydict={}

for line in filein:
   line=line.split('\t')			#split line from fasta
   query=line[0]				#get query
   coverage=assembly_dict.get(query)	#get fold coverage from assembly dictionary   
   fold=float(coverage[9]) 
   subject=line[1]				#get subject
   dict_entry=cazy_or_foly_dict.get(subject)	#get info for subject in dictionary
#   print subject
#   print fold
   family=dict_entry[2]				#obtain family
   fff=familydict.get(family,0)			#Entry family name in new dictionary, if absent use 0 if not get count
   ggg=fff+fold					#update count
   familydict[family]=ggg			#update entry in dictionary
   subfamily=dict_entry[1]			#do the same for subfamily
   sss=subfamilydict.get(subfamily,0)
   ttt=sss+fold
   subfamilydict[subfamily]=ttt
#write familydict dictionary
for key1, value1 in familydict.iteritems():
   fileout1.write("%s\t%s\n" %(key1,value1))

#write subfamily dictionary
for key2, value2 in subfamilydict.iteritems():
   fileout2.write("%s\t%s\n" %(key2,value2))
