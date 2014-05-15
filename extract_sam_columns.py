#usage Python extract.sam.columns.py <filein> <fileout>
#										arg1     arg2 

import sys

filein=open(sys.argv[1],'r')
fileout=open(sys.argv[2],'w')

for line in filein:
   if line.startswith('@'):
      continue #skip headers if present
   else:
      line=line.rstrip().split('\t')
      if line[2]=='*':
	     continue #skip lines with no alignments
      elif line[5]=='*':
         continue	  
      else:
         name=line[0]
         reference=line[2]
         start=line[3]
         lenght=len(line[9])
         fileout.write('%s'%name)
         fileout.write('\t')
         fileout.write('%s' %reference)
         fileout.write('\t')
         fileout.write('%s' %start)
         fileout.write('\t')
         fileout.write('%d' %lenght)
         fileout.write('\n')

fileout.close()
