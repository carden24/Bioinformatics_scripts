#usage python score.blast.py <sorted.annotated.blast.output>
#        		0			    1				

import sys
filein = open(sys.argv[1], 'r')
out1 = sys.argv[1] + '.richness'
fileout = open(out1, 'w')
family_dict = {}
gi_tracker = []
family_tracker = []
for line in filein:
#   print line
   line = line.lstrip(" ")
   line = line.rstrip("\n ")
   line = line.split('\t')
#   print line
   gi = line[1]
   family =  line[3]
   if family not in family_tracker:
      gi_tracker = []
      gi_tracker.append(gi)
      family_tracker.append(family)
   else:
      gi_tracker.append(gi)

#   print family, len(gi_tracker)
   family_dict[family] = gi_tracker

for key, value in family_dict.iteritems():
#    print sys.argv[1], key, len(set(value))
   fileout.write("%s\t%s\t%d\n" %(sys.argv[1], key, len(set(value))))
   
fileout.close()
filein.close()

