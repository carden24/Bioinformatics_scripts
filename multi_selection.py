#usage
#python fastaselection2.py <originalfile.fasta> <namelist1> <namelist2> <namelist3>
# 	0			1		2		3	4

import sys, screed

#inputs
filein = open(sys.argv[1], 'r')
filelist1 = open(sys.argv[2], 'r')
filelist2 = open(sys.argv[3], 'r')
filelist3 = open(sys.argv[4], 'r')

#outputs
out1 = sys.argv[2] + '.subselection'
out2 = sys.argv[3] + '.subselection'
out3 = sys.argv[4] + '.subselection'
fileout1 = open(out1, 'w')
fileout2 = open(out2, 'w')
fileout3 = open(out3, 'w')



#create a list with the names of the sequences requested
requestedsequences1 = []
requestedsequences2 = []
requestedsequences3 = []

for line in filelist1:
   line = line.strip('\n').strip('\r')
   requestedsequences1.append(line)

for line in filelist2:
   line = line.strip('\n').strip('\r')
   requestedsequences2.append(line)

for line in filelist3:
   line = line.strip('\n').strip('\r')
   requestedsequences3.append(line)

filelist1.close()
filelist2.close()
filelist3.close()

reque1 = set(requestedsequences1)
reque2 = set(requestedsequences2)
reque3 = set(requestedsequences3)

print "%s %s %s records requested" %(len(reque1), len(reque2), len(reque3))


#read file, read each record, if name is in list write it, otherwise continue
#counter=1
for record in screed.open(sys.argv[1]):
   # Get sequence name
   sequence_name = record.name
   if sequence_name in reque1:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout1.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
   elif sequence_name in reque2:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout2.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
   elif sequence_name in reque3:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout3.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
   else:
      continue

fileout2.close()
fileout3.close()
fileout1.close()
filein.close()
