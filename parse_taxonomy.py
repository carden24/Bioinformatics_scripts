#parse_taxonomy.py

import sys
import pickle

from Bio import Entrez

#Initialize files
filein = open(sys.argv[1],'r')
input_list = pickle.load(filein)

#output
#outy = sys.argv[1]
#out1 = outy +'.lineages.pkl'
#fileout = open(out1, 'w')

#lineage = {d['Rank']:d['ScientificName'] for d in 
#    input_dictionary[0]['LineageEx'] if d['Rank'] in ['family', 'order']}


for organism in input_list:
#    print organism
    lineage = {d['Rank']:d['ScientificName'] for d in organism['LineageEx'] if d['Rank'] in ['phylum', 'class', 'order', 'family', 'genus' ]}
    print lineage


for organism in input_list:
    for item in organism['LineageEx']:
        if item['Rank'] in ['phylum', 'class', 'order', 'family', 'genus']:

             print '%s\t%s\t%s' %(organism['TaxId'], item['Rank'], item['ScientificName'])

#    print organism
#    type(organism)
#    lineage_expanded = organism.get(LineagEx)
#    print lineage_expanded
#    for item in lineage_expanded:
#        if item['rank'] in ['phylum']:
#            print item['phylum']




