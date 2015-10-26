#trim_bases_from_fastq.py

import sys
import re

# Creates an input output pair if input is just an input file
def create_output(input_file_name):
   # finds file format removes extension, case insensitive search
   base_name = re.sub('[.](fastq$|fq$)','',input_file_name, re.I)
   output_file = base_name+".trimmed.fastq"
   return output_file

filein = open(sys.argv[1], 'r')
fileout = open(create_output(sys.argv[1]), 'w')

bases_to_cut_pair1 = int(sys.argv[2])
bases_to_cut_pair2 = int(sys.argv[3])
name_base = str(sys.argv[4])

fastq_line = 0
title_line = 0

for line in filein:
    if line.startswith(name_base):
        #Process title line
        print line
        print 'title'
        fileout.write('%s' %line)
        if line[-1] == '1\n':
            cutter = bases_to_cut_pair1
        else:
            cutter = bases_to_cut_pair2
        title_line = 1
        continue

    elif (len(line) == 1):
        #Process + line
        fileout.write('%s' %line)
        continue

    else:
        if title_line == 1:
           #Process sequence line
           sequence = str (line)
           new_sequence = sequence[cutter:]
           fileout.write('%s' %new_sequence)
           title_line = 0
           continue
        else:
           #Process sequence line
           # if title_line is not 1
           quality = str (line)
           new_quality = quality[cutter:]
           fileout.write('%s' %new_quality)
           continue
            
filein = filein.close()
fileout = fileout.close()

