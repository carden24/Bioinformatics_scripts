import sys
import screed

for record in screed.open(sys.argv[1]):
   print '%s\t%s' %(record.name, record.description)

