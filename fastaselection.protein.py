


#usage
#python fastaselection2.py <originalfile.fasta> <namelist>
# 	0			1		2		

import sys, screed


# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%

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
filein=open(sys.argv[1],'r')
filelist=open(sys.argv[2],'r')

#outputs
outy=sys.argv[1]
out1=outy+'.subselection'
fileout=open(out1,'w')


#create a list with the names of the sequences requested
requestedsequences=[]
for line in filelist:
   line=line.strip('\n').strip('\r')
   requestedsequences.append(line)

reque=set(requestedsequences)
duplicated=len(requestedsequences)-len(reque)

if (duplicated > 0):
   print "You have %s duplicated requested sequences" %duplicated


#number_records=len(requestedsequences)
number_records=len(reque)
print "%s records requested" % number_records







#read file, read each record, if name is in list write it, otherwise continue
#counter=1
found_counter=0
found_list=[]
for record in screed.open(sys.argv[1]):
   sequence_name=record.name			#get sequence name
#   if sequence_name in requestedsequences:
   if sequence_name in reque:
      found_list.append(sequence_name)
      found_counter=found_counter+1
#      print "%s of %s records found" %(counter, number_records)
      progress=found_counter/float(number_records)
      update_progress(progress)
      sequence=record.sequence
      sequence=sequence.strip('*') #get rid of stop codon marked as *
      description=record.description
      fileout.write(">%s %s\n%s\n" %(sequence_name, description, sequence))
 #     counter=counter+1
   else:
      continue

print "\n"
print "%s records requested" % number_records
print "%s records found" % found_counter

if number_records == found_counter:
   print 'Keep calm and carry on'
else:
      notfound=list(reque-set(found_list))
      print "Not found:%s" %notfound

fileout.close()
filein.close()
filelist.close()
