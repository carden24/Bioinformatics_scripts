# Usage
# python trim_bases_from_fastq.py <fastq> <cutoff_for_pair1> <cutoff_for_pair2>

# Created by Erick Cardenas Poire
# on 2/5/2015

# This scripts removes a given number of bases from both the sequence 
# and the quality line of a fastq file. The user can use different 
# cutoffs for either pair
# Asumptions:
# -Assumes that the third line only has the character '+'
# -Assumes that the last character in the title line shows the pair group
# -If the last assumption is false, it will use the first given cutoff


import sys
import re

# Creates an output file from input file
def create_output(input_file_name):
    # finds file format removes extension, case insensitive search
    base_name = re.sub('[.](fastq$|fq$)', '', input_file_name, re.I)
    output_file = base_name+".trimmed.fastq"
    return output_file

# Read input and options 
filein = open(sys.argv[1], 'r')
fileout = open(create_output(sys.argv[1]), 'w')

bases_to_cut_pair1 = int(sys.argv[2])
bases_to_cut_pair2 = int(sys.argv[3])

# This part is to grab the first five characters in the name.
# I need to do this to detect that I am reading a title line.
# I could search for an '@' at the beginning of the line,
# but this character is sometimes used as a quality score code

first_line = filein.readline()
first_line = str(first_line)
name_base =  first_line[:5]
assert (name_base.startswith('@')) or (name_base.startswith('>'))


filein.close()


# This counter is used to know when I passed the title line.
# So I know the next line is the sequence line
# After modifying the sequence line, the parameter is reset to zero
title_line = 0

# I need to reopen the file
filein = open(sys.argv[1], 'r')

for line in filein:
    print line
    if line.startswith(name_base):       
        #Process title line
        line = line.rstrip('\n')
        #print 'title'
        fileout.write('%s\n' %line)
        if line[-1] == '1':
            #print 'Pair 1'
            cutter = bases_to_cut_pair1
        elif line[-1] == '2':
            #print 'Pair2'
            cutter = bases_to_cut_pair2
        else:
            print 'Could not determined the pair'
            print 'Assuming no pair1 cutoff'
            cutter = bases_to_cut_pair1
        title_line = 1
        continue

    elif (len(line) == 2):
        # Assumes that the + line has a length of two, one for '+' and one for the newline
        # I may be safer to strip blankspaces, new lines, and carriage returns and then insert
        # a new line character each time       
        # Processing '+' line
        #print '+'
        fileout.write('%s' %line)
        continue

    else:
        if title_line == 1:
            # This is tru if we just passed the title line and changed the counter
            #Process sequence line
            #print 'sequence'
            sequence = str(line)
            new_sequence = sequence[cutter:]
            print new_sequence
            fileout.write('%s' %new_sequence)
            # Here we reset the counter so the next line should be the quality one
            title_line = 0
            continue
        else:
            # This is false if we just passed the sequence line and reseted the 
            # title counter to zero
            #Process quality line
            #print 'quality'
            quality = str(line)
            new_quality = quality[cutter:]
            fileout.write('%s' %new_quality)
            continue
            
filein = filein.close()
fileout = fileout.close()
