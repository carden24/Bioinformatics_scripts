#usage python show.dict.py <file.pkl>
#        	0		1

import pickle
import sys

allcazymes=[]

filedict=open(sys.argv[1],'rb')
cazy_dict = pickle.load(filedict)
for key in cazy_dict.keys():
   allvalues=cazy_dict.get(key)
   cazymes=allvalues[1]
   if cazymes in allcazymes:
      continue
   else:
      allcazymes.append(cazymes)
aa=allcazymes.sort()
print aa
