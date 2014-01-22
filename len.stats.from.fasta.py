import sys
filein=open(sys.argv[1],'r')
print 'Reading ', sys.argv[1]
out=sys.argv[1]

fileout=out+'.stats.txt'
print fileout

fp=open(fileout, 'w')

big_table=[]
for line in filein:
   if line.startswith('>'):
      continue
   else:
      length=int(len(line))
      big_table.append(length)
count=len(big_table)
average=sum(big_table)/float(count)
mini=min(big_table)
maxi=max(big_table)

print count , ' reads detected'
print 'With an average read lenght of ' , average , 'bases'
print 'And a range of ' , mini , ' to ' ,maxi

fp.write('Reads\tAverage\tMinimum\tMaximum\n')
fp.write('%d\t' %count)
fp.write('%d\t' %average)
fp.write('%d\t' %mini)
fp.write('%d\t' %maxi)
fp.close()

