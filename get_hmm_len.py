#usage
#python get.hmm.len.py <model.hmm> <output>
#	0		1		 2

import sys

#Extract model length

#Read line
#if line starts with NAME get line
#	split line
#	get second elements
#	name write name.hmm
#	write tab
#if line starts with LENG get name write name.hmm
#read next line

filein = open(sys.argv[1], 'r')
fileout = open(sys.argv[2], 'w')

for line in filein:
   if line.startswith('NAME'):
      line = line.strip('\n')
      line = line.split(' ')
      name = line[2]
      fileout.write('%s\t' %name)
      #print line[2]
   else:
      if line.startswith('LENG'):
         line = line.strip('\n')
         line = line.split(' ')
         len = line[2]
         fileout.write('%s\n' %len)
#         print line[2]
      else:
         continue

