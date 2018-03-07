#! /usr/bin/python

# author__ = "Erick Cardenas Poire"
# Usage python ./score_butyrate.py -i <input file> -d <dictionary file>

import sys
import re
from optparse import OptionParser


#config = load_config()
script_info = {}
script_info['brief_description'] = """Converts a tabular BLAST output
             into a table with count for butyrate synthesis genes.
             It requires a table that links the img ids with the gene names"""

script_info['script_usage'] = []

usage = '''
Usage:
python score_blast_butyrate.py -i <blast tabular input> -d <dictionary file>
 -o <output text file>
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_blast_result", dest="input_file",
                  help='The blast tabular input [REQUIRED]')
parser.add_option("-d", "--dictionary_file", dest="dictionary_file",
                  help='The dictionary file [REQUIRED]')


def main(argv):
    (opts, args) = parser.parse_args()
    print ''
    print 'Initializing...'

    # initialize the input file, dictionary, and output file
    input_file = opts.input_file
    dictionary_file = opts.dictionary_file
    shortname = re.sub('[.](txt)', '', input_file, re.I)
    output_file = shortname + "_summary.txt"

    filedict = open(dictionary_file, 'r')
    filein = open(input_file, 'r')
    fileout = open(output_file, 'w')

    gene_id_dictionary = {}
    for line in filedict:
        line = line.rstrip(' ')
        line = line.rstrip('\n')
        line = line.split('\t')
        gene_id = line[0]
        gene = line[1]
        gene_id_dictionary[gene_id] = gene

    gene_count_dictionary = {}
    for line2 in filein:
        line2 = line2.lstrip(' ').rstrip(' ')
        line2 = line2.strip('\n')
       # Split line from results
        line2 = line2.split(' ')
        subject = line2[1]
        line_count = int(line2[0])
        the_gene = gene_id_dictionary.get(subject, 'no_match')
        print the_gene
        # Get current count and update, if not found use zero

        current_gene_count = gene_count_dictionary.get(the_gene, 0)
        new_score = current_gene_count + line_count
        gene_count_dictionary[the_gene] = new_score

    for key, value in gene_count_dictionary.iteritems():
        fileout.write("%s\t%s\t%s\n" % (input_file, key, value))

    # Closing file
    filein.close()
    filedict.close()
    fileout.close()


# the main function
main(sys.argv[1:])