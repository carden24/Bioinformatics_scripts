#!/usr/bin/python
import sys, os, re, getopt, glob, subprocess, os.path, numpy as np, time
import timeit
from cogent.parse.ncbi_taxonomy import NcbiTaxonomyFromFiles

start = timeit.default_timer()

Usage = """
REQUIRED ARGUMENTS:
	-d	a .tsv file containing two columns:

		1) Metagenome Name
		2) the location of your enumerated CAZyme file (or any file really, but you'll have to hack the script to import the correct column containing the GI number)

	-b	the location of the NCBI dataBase relating GI to Taxonomic ID (gi_taxid_prot.dmp)

	-t	the taxonomic level(s) you would like to output. Specify either: 1|superkingdom, 2|phylum, 3|class, 4|order, 5|family, 6|genus, 7|species

DEPENDENCIES:
		'gi_taxid_prot.dmp'	Downloadable from ftp://ftp.ncbi.nih.gov/pub/taxonomy/)
					(Note there are different ID's for nucleic acid .db and protein.db)
		'names.dmp' & 'nodes.dmp'	Downloadable from ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdmp.zip

Usage:  ./GET_LINEAGES_NCBI.py -d FILE_NAMES.tsv -b ./gi_taxid_prot.dmp -t 1,2,3,6

or

Usage:  ./GET_LINEAGES_NCBI.py -d FILE_NAMES.tsv -b ./gi_taxid_prot.dmp -t superkingdom,phylum,class,genus

"""

if len(sys.argv)<2:
        print Usage
        sys.exit()

# Initialize all containers for input
FILE_LIST=''
NCBI_DB=''
TAX_LEVEL=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"d:b:t:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-d':
	FILE_LIST= a
    if o == '-b':
	NCBI_DB= a
    if o == '-t':
	TAX_LEVEL= a

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

## Set TAX_LEVEL
if len(TAX_LEVEL) == 0:
        print Usage
	print "You must specify a taxonomic level or levels with the -t argument"
        sys.exit()

else:
	print "You will produce output files for the following taxonomic levels: "+TAX_LEVEL

## IMPORT DIR NAMES into DICTIONARY
FILE_DICT={}

with open(FILE_LIST) as f:
        for line in f:
                line = line.strip("\r\n")
                line = line.split("\t")
#		print line
                FILE_DICT[line[0]] = line[1]
header = 'Metagenome ID, CAZyme, GenBank TaxID, GenBank GI, Taxonomy, Count'
header = re.sub(",","\t", header)

header2 = 'Error Message, GI Number'
header2 = re.sub(",","\t", header2)

## BUILD DICTIONARY CONTAINING GI # and TAXID # FOR ALL READS
for key, value in FILE_DICT.iteritems():
	
	SAMPLE_ID = key
	GENBANK_FILE = value

	print 'building dictionary for '+SAMPLE_ID

	with open(GENBANK_FILE, 'r') as blast_table:
		next(blast_table) #skip first line

		for each in blast_table:
			each = each.split('\t')
			foo = each[2]
#			gi = foo.split('|')
#			gi = gi[1]
# New code starts
			if foo.startswith('gi|'):
				gi = foo.split('|')
				gi = gi[1]
				subprocess.call('grep --max-count=1 \"'+gi+'\" \"'+NCBI_DB+'\" | tee -a blast_taxid.txt', shell = True)
			else:
				gi = foo.split('_')
				gi = gi[1]
				subprocess.call('grep --max-count=1 \"'+gi+'\" \"'+NCBI_DB+'\" | tee -a blast_taxid.txt', shell = True)
# New code ends

	map_dict = {}
	with open('blast_taxid.txt') as gi_taxid:
		for each in gi_taxid:
			each = each.split()
			gi = each[0]
			taxid = each[1]
			map_dict[gi] = taxid

	print 'reading in files for '+SAMPLE_ID

#	tree = NcbiTaxonomyFromFiles(open('/home/roli/scripts/Python/GI_annotations/nodes.dmp'), open('/home/roli/scripts/Python/GI_annotations/names.dmp'))
	tree = NcbiTaxonomyFromFiles(open('nodes.dmp'), open('names.dmp'))
	root = tree.Root

	print 'generating lineages for '+SAMPLE_ID 

	error = open(SAMPLE_ID+'.no.lineage.found.out','w')
	error.write(header2+"\n")

	if re.search("1|superkingdom",TAX_LEVEL):
		output_kingdom = open(SAMPLE_ID+'.superkingdom.blast_lineage.out', 'w')
		output_kingdom.write(header+"\n")

	if re.search("2|phylum",TAX_LEVEL):
		output_phylum = open(SAMPLE_ID+'.phylum.blast_lineage.out', 'w')
		output_phylum.write(header+"\n")

	if re.search("3|class",TAX_LEVEL):
		output_class = open(SAMPLE_ID+'.class.blast_lineage.out', 'w')
		output_class.write(header+"\n")

	if re.search("4|order",TAX_LEVEL):
		output_order = open(SAMPLE_ID+'.order.blast_lineage.out', 'w')
		output_order.write(header+"\n")

	if re.search("5|family",TAX_LEVEL):
		output_family = open(SAMPLE_ID+'.family.blast_lineage.out', 'w')
		output_family.write(header+"\n")

	if re.search("6|genus",TAX_LEVEL):
		output_genus = open(SAMPLE_ID+'.genus.blast_lineage.out', 'w')
		output_genus.write(header+"\n")

	if re.search("7|species",TAX_LEVEL):
		output_species = open(SAMPLE_ID+'.species.blast_lineage.out', 'w')
		output_species.write(header+"\n")

	## OPEN FILES AND ATTRIBUTE LINEAGE TO GI
	with open(GENBANK_FILE, 'r') as input:
		next(input)

		for line in input:
			try:
				line = line.split('\t')
				foo = line[2]
#				gi = foo.split('|')
#				gi = gi[1]
#new code begins
				if foo.startswith('gi|'):
					gi = foo.split('|')
					gi = gi[1]
				else:
					gi = foo.split('_')
					gi = gi[1]
				taxid = int(map_dict[gi])
#new code ends

				if re.search("1|superkingdom",TAX_LEVEL):
					ranks = ['superkingdom']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_kingdom.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))
	
				if re.search("2|phylum",TAX_LEVEL):
					ranks = ['phylum']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_phylum.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

				if re.search("3|class",TAX_LEVEL):
					ranks = ['class']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_class.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

				if re.search("4|order",TAX_LEVEL):
					ranks = ['order']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_order.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

				if re.search("5|family",TAX_LEVEL):
					ranks = ['family']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_family.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

				if re.search("6|genus",TAX_LEVEL):
					ranks = ['genus']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_genus.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

				if re.search("7|species",TAX_LEVEL):
					ranks = ['species']

					node = tree.ById[taxid]
					tax = get_lineage(node, ranks)
					tax = str(tax[0]).lower()

					output_species.write(SAMPLE_ID+"\t"+line[1]+'\t'+str(taxid)+'\t'+str(gi)+'\t'+tax+'\t'+str(line[3]))

			except KeyError:
				error.write('key error'+"\t"+str(gi))

		if re.search("1|superkingdom",TAX_LEVEL):
			output_kingdom.close()

		if re.search("2|phylum",TAX_LEVEL):
			output_phylum.close()

		if re.search("3|class",TAX_LEVEL):
			output_class.close()

		if re.search("4|order",TAX_LEVEL):
			output_order.close()

		if re.search("5|family",TAX_LEVEL):
			output_family.close()

		if re.search("6|genus",TAX_LEVEL):
			output_genus.close()

		if re.search("7|species",TAX_LEVEL):
			output_species.close()

		error.close()


stop = timeit.default_timer()

print "This operation took " + str(stop - start) + " seconds."

