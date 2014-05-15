#usage score.paired.ends.py <blast.output> <dictionary.for.scoring>
#           0                  1  

import sys
import pickle

filedict=open(sys.argv[2],'rb')
cazy_or_foly_dict = pickle.load(filedict)


#gi|188989396|ref|NC_010688.1|_3592220_3592547_0_1_0_0_6:0:0_3:0:0_10	gi_21112230_gb_AAM40486.1_	75	452	24	6e-06	47.8
#qsid 									ssid				piden	slen	len	evalue	bits
#0									1				2	3	4	5	6

hitlist=[]
line_counter=0

filein=open(sys.argv[1],'r')
for line in filein:
   line_counter=line_counter+1
   itemlist=[]
   line=line.split('\t')
   qsid=line[0]
   ssid=line[1]
   itemlist.append(qsid)
   itemlist.append(ssid)
   hitlist.append(itemlist)

same_pair_counter=0
samehit_counter=0
same_superfamily_counter=0
same_family_counter=0


counter=0
while counter<(line_counter - 1):
#while counter<10:
   item_1=hitlist[counter]
   query1=item_1[0]
   q1=query1.split('/')
   q_1=q1[0]
   item_2=hitlist[counter+1]
   query2=item_2[0]
   q2=query2.split('/')
   q_2=q2[0]
   counter=counter+1

   if q_1==q_2:
      same_pair_counter=same_pair_counter+1
      subject1=item_1[1]
      subject2=item_2[1]
      if subject1==subject2:
         samehit_counter=samehit_counter+1
      else:
         dict_entry1=cazy_or_foly_dict.get(subject1)	#get info for subject in dictionary
         superfamily1=dict_entry1[2]
         family1=dict_entry1[1]		
         dict_entry2=cazy_or_foly_dict.get(subject2)	#get info for subject in dictionary
         superfamily2=dict_entry2[2]
         family2=dict_entry2[1]		
         if superfamily1==superfamily2:
            same_superfamily_counter=same_superfamily_counter+1
         else:
            continue
         if family1==family2:
            same_family_counter=same_family_counter+1
         else:
            continue
         continue
   else:
      continue

myfile=sys.argv[1]

#print sys.argv[1]
#print '%s records found' %line_counter
#print '%s sets of paired ends' %same_pair_counter
#print '%s of pairs hit same subject' %samehit_counter
#print '%s of pairs hit same superfamily' %same_superfamily_counter
#print '%s of pairs hit same family' %same_family_counter

#print 'File\tRecords found\tPair sets\tSet hits same subject\tPairs hits different subjects but same superfamily\tPairs hits different subjects but same family'
#print '%s\t %s\t%s\t%s\t%s\t%s' %(myfile,line_counter,same_pair_counter,samehit_counter,same_superfamily_counter,same_family_counter)

if same_pair_counter==0:
   print '%s\t%s\t%s\t0\t0\t0\t0' %(myfile,line_counter,same_pair_counter)
else:
   score_three=(samehit_counter*100)/float(same_pair_counter)
   score_two=(same_family_counter*100)/float(same_pair_counter)
   score_one=((same_superfamily_counter*100)/float(same_pair_counter))-score_two
   score_zero=100-(score_one + score_two + score_three)
   print '%s\t%s\t%s\t%s\t%s\t%s\t%s' %(myfile,line_counter,same_pair_counter,score_three,score_two,score_one,score_zero)


#X0                                                      
#X1                             |=>same superfamily         
#X2             |=>same family  |
#X3  |=>same hit
#X3  |
 








