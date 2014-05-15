import sys
import math
import pickle
import numpy
from math import sqrt


pkl_file = open('genome_len_dict.pk3', 'rb')
genome_length_dict = pickle.load(pkl_file)

#print genome_length_dict

#2. check dictionary to create right index


file2=open(sys.argv[1],'r')
genome=sys.argv[1]
b=genome_length_dict[genome]
b1=b[0]
imported_genome_length=(int(b1))
index=[0]*imported_genome_length



#3 count positions
for line2 in file2:
    line2=line2.rstrip().split('\t')
    init=int(line2[2])
    AA=init+(int(line2[3]))
    counter=init
    while counter <=AA:
        index[counter]=index[counter]+1
        counter=counter+1

##############################################
#4 Create dictionary for gene locations

genome2=genome.split('.') #This is just to get the name of out my files that have a .MMB1.txt extension
genome3=genome2[0]
print genome3


#open corresponding gene location map

file4='./locations/'+genome3+'_gene_mapping.txt' #This is to open the gene mapping files using the right name of the genome
#print file4

file5=open(file4,'r')



gene_locations={}
for line in file5:
    line=line.split('\t')
    gene_name=line[1]
    location=line[2]
    ids00=line[6]
    ids0=ids00.split('\n')
    ids=ids0[0]
#    print location
    if location.startswith('join'):
        print 'join found'      
        continue
    elif location.startswith('complement(j'):
        print 'complement(join found'
        continue
    elif location.startswith('complement'):
        location2=location.strip('complement()')
        location2=location2.split('..')
        gene_beginning=location2[0]
        gene_ending=location2[1]
    else:
        location2=location.rstrip().split('..')
        gene_beginning=location2[0]
        gene_ending=location2[1]
    xxx=gene_locations.get(ids,[])
    xxx.append(gene_name)
    xxx.append(gene_beginning)
    xxx.append(gene_ending)
    gene_locations[ids]=xxx
	
print gene_locations

#5 Loop through each value of the dictionary to subselect region of the gene from the index
#  then get the median for that region and if the median is more than two then record the gene id, gene name, coordinates and median.

list_of_genes= gene_locations.keys()
len_list_of_genes=len(list_of_genes)

ff=genome3+'_genes_found.txt'
fff=open(ff,'w')

counter_genes=0
while counter_genes<len_list_of_genes:
    particular_gene=list_of_genes[counter_genes]
    gene_info=gene_locations[particular_gene]
    gene_start00=gene_info[1]
    gene_start0=gene_start00.strip('><') #this takes care of gene coordinates starting with ">" or "<"
    gene_start=int(gene_start0)-1
    gene_end00=gene_info[2]
    gene_end0=gene_end00.strip('><')
    gene_end=int(gene_end0)-1
    retrieved_genome_section=index[gene_start:gene_end]
    median_retrieved_genome=numpy.median(retrieved_genome_section)
    if median_retrieved_genome>=2:
        gene_desc=gene_info[0]
        fff.write ('%s \t' %genome3)
        fff.write ('%s \t' %particular_gene)
        fff.write ('%s \t' %gene_desc)
        fff.write ('%d \t' %gene_start)
        fff.write ('%d \t' %gene_end)
        fff.write ('%d \n'%median_retrieved_genome)
        counter_genes=counter_genes+1
    else:
#        gene_desc=gene_info[0]
#        fff.write ('%s \t' %genome3)
#        fff.write ('%s \t' %particular_gene)
#        fff.write ('%s \t' %gene_desc)
#        fff.write ('%d \t' %gene_start)
#        fff.write ('%d \t' %gene_end)
#       fff.write ('%d \n'%median_retrieved_genome)
        counter_genes=counter_genes+1

