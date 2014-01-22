#usage python split.pairs.py <input.fastq>

import sys
import screed
from screed.fastq import fastq_iter

filein=sys.argv[1]

out1=filein+'_1.fastq'
out2=filein+'_2.fastq'
fileout1=open(out1,'w')
fileout2=open(out2,'w')

for n, record in enumerate(screed.open(filein)):
   name = record['name']
   sequence = record['sequence']
   accuracy = record['accuracy']
   description = record['annotations']
   if (description.find('1:N:0:')!=-1):
      fileout1.write('@%s %s' %(name,description))
      fileout1.write('\n')
      fileout1.write('%s' %sequence)
      fileout1.write('\n')
      fileout1.write('+')
      fileout1.write('\n')
      fileout1.write('%s' %accuracy)
      fileout1.write('\n')
   else:
      fileout2.write('@%s %s' %(name,description))
      fileout2.write('\n')
      fileout2.write('%s' %sequence)
      fileout2.write('\n')
      fileout2.write('+')
      fileout2.write('\n')
      fileout2.write('%s' %accuracy)
      fileout2.write('\n')
fileout1.close()
fileout2.close()



