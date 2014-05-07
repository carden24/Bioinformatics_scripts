#!/usr/bin/python
# File created on 13 Feb 2014.
from __future__ import division

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"


#usage python create.newcazy.dictionary.py <fasta.file> <output.pkl.file> 
#        	0				1		2	

import pickle
import sys
import Bio
from Bio import SeqIO
import re

filein=open(sys.argv[1],'rb')
fileout=open(sys.argv[2],'w')
cazy_class=sys.argv[3]
cazy_family_number=sys.argv[4]


cazydict={}

for seq_record in SeqIO.parse(filein, format="fasta"):
    description=seq_record.description
#   print description
    subject=seq_record.name
#   print subject
#   organismsearch=re.search('\[[A-Za-z0-9\.\_\-\s\'\+\]]+',description)
    organismsearch=re.search('(\[)([A-Za-z0-9\.\_\-\s\'\/\=\#\(\)\:\*\&]+)(\])',description)
    if organismsearch==None:
        organism="None"
    else:
      #print organismsearch.group(0)
        organism=organismsearch.group(0)
    description_search=re.search(' (\()([AGCP])([AHTL])(\:)([A-Z]+)(_]+)(\))',description)
#   print description
#   print description_search.group()
#   familydata=description_search.group(0)
#   thecazyclass=familydata.split(':')
#   cazyclass=thecazyclass[0].strip('("')
#   cazy_family_number=thecazyclass[1].strip(')"')
#   cazy = cazy_class + cazy_family_number
#   print cazy
   


    x=cazydict.get(subject, [])
    x.append(description)
    x.append(cazy)
    x.append(cazyclass)
    x.append(organism)
    cazydict[subject]=x
    print cazydict

#pickle.dump(cazydict,fileout)
