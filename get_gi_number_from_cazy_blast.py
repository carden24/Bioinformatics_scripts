#usage python get_gi_number_from_cazy_blast.py <blast.output> <out.file>
#        	0				1		2	

import sys

filein = open(sys.argv[1], 'r')
fileout = open(sys.argv[2], 'w')

gi_number_list = []
for line in filein:
    line0 = line.split('\t')
    if len(line0) == 1 :
        break
    else:
        gi_column = line0[1]
        print gi_column
        if gi_column.startswith('gi|'):
            gi_location = gi_column.split('|')
            gi_number = gi_location[1]
            gi_number_list.append(gi_number)
        else:
            gi_location = gi_column.split('_')
            gi_number = gi_location[1]
            gi_number_list.append(gi_number)

 

