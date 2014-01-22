#! /usr/bin/env python
import sys
import screed

for record in screed.open(sys.argv[1]):
   if len(record.sequence)==75:
      print '>%s %s\n%s' % (record.name, record.description,record.sequence)
   else:
      continue
