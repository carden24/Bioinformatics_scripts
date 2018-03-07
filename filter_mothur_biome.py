

# Script to remove unwanted samples from mothur shared file

# Read list of unwanted samples
# Read line


# Write if not in list


import sys
import re

# Inputs
filein = open(sys.argv[1], 'r')
filelist = open(sys.argv[2], 'r')

shared_shortname = re.sub('[.](shared)', '', sys.argv[1], re.I)
fileout_handle = shared_shortname + "_filtered.shared"
fileout = open(fileout_handle, 'w')


#create a list with the names of the samples requested
requested_samples = []
for sample in filelist:
    sample = sample.strip('\n').strip('\r')
    requested_samples.append(sample)
filelist.close()

# Print number of requested samples
print "%s records requested" % len(requested_samples)

found_counter = 0
for line in filein:
    line2 = line.strip('\n').strip('\r')
    line2 = line2.split('\t')
    # Second column correspond to the sample in the otu table
    if line2[1] in requested_samples:
        found_counter = found_counter + 1
        continue
    else:
        fileout.write("%s" % line)

print "%s samples removed" % found_counter

fileout.close()
filein.close()
