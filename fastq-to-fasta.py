import sys
sys.path.insert(0, '/u/t/dev/screed')
import screed
from screed.fastq import fastq_iter

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%

def update_progress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
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
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "="*block + " "*(barLength-block), progress*100, status)
    sys.stderr.write(text)
    sys.stderr.flush()

counter = 0
for n, record in enumerate(fastq_iter(open(sys.argv[1]))):
   counter = counter + 1
   print ('%s reads found' %counter)

for n, record in enumerate(fastq_iter(open(sys.argv[1]))):
   if n % 1 == 0:
      progress=n / float(counter)
      update_progress(progress)
#print>>sys.stderr, '...', n     
   sequence = record['sequence']
   name = record['name']

   if 'N' in sequence:
      continue

   print ">" + name
   print sequence


        
