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




## Define function for pulling lineage info from NCBI nodes and names files
def get_lineage(node, my_ranks):
	ranks_lookup = dict([(r,idx) for idx,r in enumerate(my_ranks)])
	lineage = [None] * len(my_ranks)
	curr = node
	while curr.Parent is not None:
		if curr.Rank in ranks_lookup:
			lineage[ranks_lookup[curr.Rank]] = curr.Name
		curr = curr.Parent
	return lineage

#Initialize files
input_fp = opts.input_fp 
input_dictionary_file = open(input_fp, "rb")
input_dictionary = pickle.load(input_dictionary_file)

output_fp = opts.output_fp 
output = open(output_fp, "w")

#Initialize tree

tree = NcbiTaxonomyFromFiles(open('nodes.dmp'), open('names.dmp'))
root = tree.Root

for key in cazy_dictionary.keys():
    if key.startswith('gi|'):
        gi_location = key.split('|')
        gi_number = gi_location[1]
    else:
        gi_location = key.split('_')
        gi_number = gi_location[1]
    # get node information
    subprocess.call('grep --max-count=1 \"'+gi+'\" \"'+NCBI_DB+'\" | tee -a blast_taxid.txt', shell = True)
    gi_number








input_dictionary_file.close()
output.close()
