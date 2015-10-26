# This script was used to count the times of members of a pair end agree on the subject of CAZY family

#usage score.paired.ends.py <blast.output> <dictionary.for.scoring>
#           0                  1  

import sys
import pickle

# Loads scoring dictionary
filedict=open(sys.argv[2],'rb')
cazy_or_foly_dict = pickle.load(filedict)

hitlist = []
line_counter = 0

filein = open(sys.argv[1], 'r')
# Storing results in list with query-subject pair
for line in filein:
    line_counter = line_counter + 1
    itemlist = []
    line = line.split('\t')
    qsid = line[0]
    ssid = line[1]
    itemlist.append(qsid)
    itemlist.append(ssid)
    hitlist.append(itemlist)

same_pair_counter = 0
samehit_counter = 0
same_family_counter = 0
same_superfamily_counter = 0

counter = 0
while counter < (line_counter - 1):
    # Processing files
    item_1 = hitlist[counter]
    query1 = item_1[0]
    q1 = query1.split('/')
    q_1 = q1[0]
    item_2 = hitlist[counter + 1]
    query2 = item_2[0]
    q2 = query2.split('/')
    q_2 = q2[0]
    counter = counter + 1

    # Are both pairs in results
    if q_1 == q_2:
        # Both pairs are present
        same_pair_counter = same_pair_counter + 1
        subject1 = item_1[1]
        subject2 = item_2[1]
        if subject1 == subject2:
            samehit_counter = samehit_counter + 1
        else:
            # Get info for subject in dictionary
            dict_entry1 = cazy_or_foly_dict.get(subject1)
            superfamily1 = dict_entry1[2]
            family1 = dict_entry1[1]		
            # Get info for subject in dictionary
            dict_entry2 = cazy_or_foly_dict.get(subject2)	
            superfamily2 = dict_entry2[2]
            family2 = dict_entry2[1]		
            if superfamily1 == superfamily2:
                same_superfamily_counter = same_superfamily_counter + 1
            else:
                continue
            if family1 == family2:
                same_family_counter=same_family_counter + 1
            else:
                continue
            continue
    else:
        continue

myfile = sys.argv[1]


if same_pair_counter == 0:
    print '%s\t%s\t%s\t0\t0\t0\t0' %(myfile, line_counter, same_pair_counter)
else:
    score_same_hit = (samehit_counter * 100) / float(same_pair_counter)
    score_same_family = (same_family_counter * 100) / float(same_pair_counter)
    score_same_superfamily = ((same_superfamily_counter * 100) / float(same_pair_counter)) - score_same_family
    score_zero = 100 - (score_same_hit + score_same_family + score_same_superfamily)
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s' %(myfile, line_counter, same_pair_counter, score_same_hit, score_same_family,  score_same_superfamily, score_zero)

# Both pairs are present in result : same_pair_counter
# Subjects are the same : samehit_counter
# Both superfamilies are the same : same_superfamily_counter
# Both families are the same : same_family_counter


#X0                                                      
#X1                             |=>same superfamily         
#X2             |=>same family  |
#X3  |=>same hit
#X3  |
 

