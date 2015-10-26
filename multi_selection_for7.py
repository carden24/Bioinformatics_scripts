#usage
#python fastaselection2.py <originalfile.fasta> <namelist1> <namelist2> <namelist3>
#       0                       1               2               3       4

import sys, screed

def update_progress(progress):
    barLength = 30 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done.....\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "="*block + " "*(barLength-block), progress*100, status)
    sys.stderr.write(text)
    sys.stderr.flush()





#inputs
filein = open(sys.argv[1], 'r')
filelist1 = open(sys.argv[2], 'r')
filelist2 = open(sys.argv[3], 'r')
filelist3 = open(sys.argv[4], 'r')
filelist4 = open(sys.argv[5], 'r')
filelist5 = open(sys.argv[6], 'r')
filelist6 = open(sys.argv[7], 'r')
filelist7 = open(sys.argv[8], 'r')


#outputs
out1 = sys.argv[1] + '.subselection.by' +sys.argv[2]
out2 = sys.argv[1] + '.subselection.by' +sys.argv[3]
out3 = sys.argv[1] + '.subselection.by' +sys.argv[4]
out4 = sys.argv[1] + '.subselection.by' +sys.argv[5]
out5 = sys.argv[1] + '.subselection.by' +sys.argv[6]
out6 = sys.argv[1] + '.subselection.by' +sys.argv[7]
out7 = sys.argv[1] + '.subselection.by' +sys.argv[8]

fileout1 = open(out1, 'w')
fileout2 = open(out2, 'w')
fileout3 = open(out3, 'w')
fileout4 = open(out4, 'w')
fileout5 = open(out5, 'w')
fileout6 = open(out6, 'w')
fileout7 = open(out7, 'w')

#create a list with the names of the sequences requested
requestedsequences1 = []
requestedsequences2 = []
requestedsequences3 = []
requestedsequences4 = []
requestedsequences5 = []
requestedsequences6 = []
requestedsequences7 = []

for line in filelist1:
   line = line.strip('\n').strip('\r')
   requestedsequences1.append(line)

for line in filelist2:
   line = line.strip('\n').strip('\r')
   requestedsequences2.append(line)

for line in filelist3:
   line = line.strip('\n').strip('\r')
   requestedsequences3.append(line)

for line in filelist4:
   line = line.strip('\n').strip('\r')
   requestedsequences4.append(line)

for line in filelist5:
   line = line.strip('\n').strip('\r')
   requestedsequences5.append(line)

for line in filelist6:
   line = line.strip('\n').strip('\r')
   requestedsequences6.append(line)

for line in filelist7:
   line = line.strip('\n').strip('\r')
   requestedsequences7.append(line)


filelist1.close()
filelist2.close()
filelist3.close()
filelist4.close()
filelist5.close()
filelist6.close()
filelist7.close()


reque1 = set(requestedsequences1)
reque2 = set(requestedsequences2)
reque3 = set(requestedsequences3)
reque4 = set(requestedsequences4)
reque5 = set(requestedsequences5)
reque6 = set(requestedsequences6)
reque7 = set(requestedsequences7)

rr1 = len(reque1)
rr2 = len(reque2)
rr3 = len(reque3)
rr4 = len(reque4)
rr5 = len(reque5)
rr6 = len(reque6)
rr7 = len(reque7)


print "%s %s %s %s %s %s %s records requested" %(rr1, rr2, rr3, rr4, rr5, rr6, rr7)



counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0


for record in screed.open(sys.argv[1]):
   # Get sequence name
   sequence_name = record.name
   if sequence_name in reque1:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout1.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter1 = counter1 + 1
      progress = counter1/float(rr1)
      update_progress(progress)
   elif sequence_name in reque2:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout2.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter2 = counter2 + 1
      progress = counter2/float(rr2)
      update_progress(progress)
   elif sequence_name in reque3:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout3.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter3 = counter3 + 1
      progress = counter3/float(rr3)
      update_progress(progress)
   if sequence_name in reque4:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout4.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter4 = counter4 + 1
      progress = counter4/float(rr4)
      update_progress(progress)
   elif sequence_name in reque5:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout5.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter5 = counter5 + 1
      progress = counter5/float(rr5)
      update_progress(progress)
   elif sequence_name in reque6:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout6.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter6 = counter6 + 1
      progress = counter6/float(rr6)
      update_progress(progress)
   elif sequence_name in reque7:
      sequence = record.sequence
      sequence = sequence.strip('*')
      description = record.description
      fileout7.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
      counter7 = counter7 + 1
      progress = counter7/float(rr7)
      update_progress(progress)
   else:
      continue

fileout2.close()
fileout3.close()
fileout1.close()
fileout4.close()
fileout5.close()
fileout6.close()
fileout7.close()


filein.close()
