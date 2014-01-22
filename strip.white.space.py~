#usage python strip.white.space.py <file>
#        	0			        1		

import sys

filein=open(sys.argv[1],'r')
outy=sys.argv[1]
out1=outy+'.csv'
fileout=open(out1,'w')

for line in filein:
   line0=line.lstrip(' ').strip('\r\n')
   line1=line0.split(' ')
   otucount=str(line1[0])
   line2=line1[1].split(',')
   sample=line2[0]
   otu=line2[1]
   fileout.write("%s,%s,%s\n" %(sample,otu,otucount))
