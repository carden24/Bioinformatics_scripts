#usage
#python fasta.removal.py <originalfile.nucleotide.fasta> <namelist>
# 	0			1		2		

import sys, screed

#inputs
filein = open(sys.argv[1], 'r')
filelist = open(sys.argv[2], 'r')

#outputs
outy = sys.argv[1]
out1 = outy + '.cleaned.sequences'
fileout1 = open(out1, 'w')

outy = sys.argv[1]
out2 = outy + '.removed.sequences'
fileout2 = open(out2, 'w')



#create a list with the names of the sequences requested
requestedsequences = []
for line in filelist:
   line = line.strip('\n').strip('\r')
   requestedsequences.append(line)

#print requestedsequences
number_records = len(requestedsequences)
print "%s records requested" % number_records


#read file, read each record, if name is in list write it, otherwise continue
counter = 1
for record in screed.open(sys.argv[1]):
   sequence_name = record.name			#get sequence name
   if sequence_name in requestedsequences:
      print "%s of %s records found" %(counter, number_records)
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout2.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter = counter + 1
   else:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout1.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
fileout.close()
fileout2.close()
