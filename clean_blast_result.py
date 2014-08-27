#usage python clean_blast_result.py <blast.result> <output>
#        	0		        1		2	


import sys

filein = open(sys.argv[1], 'r')
fileout = open(sys.argv[2], 'w')


for line in filein:
    if line.startswith('H'):
        fileout.write ('%s' %line)
    else:
        continue

filein.close()
filein.out()
