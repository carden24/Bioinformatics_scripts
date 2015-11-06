#usage python score.blast.py <blast.output> <out.file.base>
#        		0			1				2	

import sys
print(sys.argv)
filein = open(sys.argv[1], 'r')
out1 = sys.argv[2] + '.richness'
fileout1 = open(out1, 'w')

gi_tracker = []
family_tracker = []
for line in filein:
   line = line.lstrip(" ")
   line = line.rstrip("\n ")
   line = line.split('\t')
   gi = line[1]
   family =  line[3]
   if family not in family_tracker:
      print family, len(gi_tracker), 
      gi_tracker = []
      gi_tracker.append(gi)
      family_tracker.append(family)
   else:
      gi_tracker.append(gi)
   
fileout1.close()
filein.close()

