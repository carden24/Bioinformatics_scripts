#!/usr/bin/python
import sys, os, re, glob, subprocess, numpy as np, pickle
from cogent.parse.ncbi_taxonomy import NcbiTaxonomyFromFiles
from optparse import OptionParser

#config = load_config()
script_info={}
script_info['brief_description'] = """Adds lineage to dictionary"""
script_info['script_description'] = """Adds lineage to dictionary"""
script_info['script_usage'] = []

usage= """
Need to run it like this:
./add_lineage_to_dictionary  -i input_file"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_dictionary", dest="input_fp",
                  help='the input dictionary file [REQUIRED]')
parser.add_option("-o", "--destination_dictionary", dest="output_fp",
                  help='the output dictionary file [REQUIRED]')
parser.add_option("-t", "--tax_level", dest="tax_level",
                  help='the desired taxonomic levels [REQUIRED]')
parser.add_option("-d", "--ncbi_database", dest="ncbi_db",
                  help='ncbi database [REQUIRED]')

## Define function for pulling lineage info from NCBI nodes and names files
def get_lineage(node, my_ranks):
	ranks_lookup = dict([(r,idx) for idx, r in enumerate(my_ranks)])
	lineage = [None] * len(my_ranks)
	curr = node
	while curr.Parent is not None:
		if curr.Rank in ranks_lookup:
			lineage[ranks_lookup[curr.Rank]] = curr.Name
		curr = curr.Parent
	return lineage


#def get_lineage_from_taxid(gi):
#        try:
#            # Superkingdom search
#            node = tree.ById[taxid]

#            tax_superkingdom = get_lineage(node, 'superkingdom')
#            tax_superkingdom = str(tax_superkingdom[0]).lower()

#            tax_phylum = get_lineage(node, 'phylum')
#            tax_phylum = str(tax_phylum[0]).lower()

#            tax_class = get_lineage(node, 'class')
#            tax_class = str(tax_class[0]).lower()

#            tax_order = get_lineage(node, 'order')
#            tax_order = str(tax_order[0]).lower()

 #           tax_family = get_lineage(node, 'family')
  #          tax_family = str(tax_family[0]).lower()

   #         tax_genus = get_lineage(node, 'genus')
    #        tax_genus = str(tax_genus[0]).lower()

     #       tax_species = get_lineage(node, 'species')
      #      tax_species = str(tax_species[0]).lower()

       #     tax = [tax_superkingdom, tax_phylum, tax_class, tax_order, tax_family, tax_genus, tax_species] 
        #except KeyError:
         #   tax = ['NA','NA','NA','NA','NA','NA','NA']
        #print tax



def main(argv):
    (opts, args) = parser.parse_args()

    #Initialize files
    input_fp = opts.input_fp 
    input_dictionary_file = open(input_fp, "rb")
    input_dictionary = pickle.load(input_dictionary_file)

    output_fp = opts.output_fp 
    output_file = open(output_fp, "w")
#    output = {}
    ncbi_db = opts.ncbi_db 

    # Print loading dictionary    
#    test_dictionary = {'gi_63300aaa':['a','b','c'], 'gi|163862923|gb_ABY43982.1_': ['d','e','f']}

    # Print loading tree
#    tree = NcbiTaxonomyFromFiles(open('nodes.dmp'), open('names.dmp'))
#    root = tree.Root
#    all_taxids = []

    for key in input_dictionary.keys():
#    for key in test_dictionary.keys():
        #print key
        if key.startswith('gi|'):
            gi_location = key.split('|')
            gi = gi_location[1]
        else:
            gi_location = key.split('_')
            gi = gi_location[1]
#        subprocess.call('grep --max-count=1 \"'+gi+'\" \"'+ncbi_db+'\" | tee -a blast_taxid.txt', shell = True)
        grep = subprocess.Popen('grep --max-count=1 \"'+gi+'\" \"'+ncbi_db+'\"', shell = True, stdout = subprocess.PIPE)
        node0 = grep.communicate()[0]
        node1 = node0.strip('\n').split('\t')
        try:
            taxid = int(node1[1])
        except IndexError:
            taxid = 'nope'
        #print taxid
        output_file.write ('%s\t%s\t%s\n' %(key, gi, taxid))
        #print 'end'

#        if taxid  == None :
#            print 'No taxid found for gi %s' %gi
#            taxid = 'nope'
#        else:
#            continue
         #       all_taxids.append(taxid)

#        value = test_dictionary.get(key)
#        print value
#        print 'gi is %s' %gi
#        value2 = value.append(str(gi))
#        print value2
#        value3 = value2.append(str(taxid))
#        print value

#        output[key] = value2
#    print len(set(all_taxids))
#    print all_taxids.count('none')
#    input_dictionary_file.close()
#    pickle.dump(output,output_file)
    output_file.close()

# Run main function 
main(sys.argv[1:])


