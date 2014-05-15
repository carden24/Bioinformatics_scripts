#usage
#python count.genomes.py genome

import sys
import math
from math import sqrt


pkl_file = open('genome_len_dict3.pkl', 'rb')
genome_length_dict = pickle.load(pkl_file)

#2. check dictionary to create right index



genome=sys.argv[1]
b=genome_length_dict[genome]
b1=b[0]
imported_genome_length=(int(b1))
index=[0]*imported_genome_length

file=open(sys.argv[1],'r')

for line in file:
    line=line.rstrip().split('\t')
    init=int(line[2])
    AA=init+(int(line[3]))
    counter=init
    while counter <=AA:
        index[counter]=index[counter]+1
        counter=counter+1

recovery=len(index)-index.count(0)
#print recovery, 'bases were recovered'
mean=float(sum(index)/float(recovery))
mean1=str(mean)
#print 'mean coverage is', mean
covmax=max(index)
#print 'maximum coverage is ' ,covmax

recovery2=float((100*recovery)/float(c))
#print 'recovery is', recovery2, '%'

#histo=range(0,10000,1)
#for i in histo:
#    histo[i]=0
#    i=i+1
#histo2=histo[0:covmax]

histo2=[0]*covmax


#print 'this should be a zero', sum(histo)    
counter=1
while counter<=covmax:
    if index.count(counter)==0:
        histo2[counter-1]=0
        #print 'working at', counter, 'coverage'
        counter=counter+1
    else:
        histo2[counter-1]=float((index.count(counter))*((float((counter-mean)**2))))
        #print 'working at', counter, 'coverage'
        counter=counter+1
#print histo2
#print sum(histo2)
SD=float(sqrt((sum(histo2))/float(recovery-1)))
SD1=str(SD)
#print SD1
  
print 'genome', a, 'has size', c, recovery, 'bases recovered, or ',recovery2, '%'
ff=sys.argv[1]+'.processed2.txt'
fff=open(ff,'w')
fff.write('%s' %a)
fff.write('\t')
fff.write('%d' %recovery)
fff.write('\t')
fff.write('%s' %recovery2)
fff.write('\t')
fff.write('%s' %mean1)
fff.write('\t')
fff.write('%s' %SD1)
fff.write('\n')
fff.close()
