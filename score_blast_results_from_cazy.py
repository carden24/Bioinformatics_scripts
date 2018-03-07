#!/usr/bin/python

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__maintainer__ = "Erick Cardenas Poire"

import pickle
import sys
import re
from optparse import OptionParser

#config = load_config()
script_info = {}
script_info['brief_description'] = """This script converts a tabular BLAST
             output into a table with count for each CAZy family.
             It requires a pregenerated dictionary (pkl) from the CAZy file used
             as BLAST database """

script_info['script_usage'] = []

usage = '''
Usage:
python score_blast_results_from_cazy.py -i <blast tabular input>
-d <cazy dictionary>
 -o <output text file>
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_blast_result", dest="input_file",
                  help='The blast tabular input [REQUIRED]')
parser.add_option("-d", "--dictionary_file", dest="dictionary_file",
                  help='The dictionary file [REQUIRED]')
parser.add_option("-o", "--output_table", dest="output_file", default='None',
                  help='The output file [OPTIONAL]')


# checks if the supplied arguments are adequate
def valid_arguments(opts, args):
    if (opts.input_file == None or opts.dictionary_file == None ):
        return True
    else:
        return False


def main(argv):
    (opts, args) = parser.parse_args()
    print ''
    print 'Initializing...'

    if valid_arguments(opts, args):
        print usage
        sys.exit(0)

    # initialize the input file, dictionary, and output file
    input_file = opts.input_file
    dictionary_file = opts.dictionary_file
    output_file = opts.output_file
    if output_file == 'None':
        print 'No output file was specified'
        output_file = input_file + '_cazy_family'
        print 'Output will be directed to file: %s' % output_file
#    else:
#        continue

    # Open input and outputs
    filedict = open(dictionary_file, 'rb')
    filein = open(input_file, 'r')
    fileout = open(output_file, 'w')
    print 'Loading dictionary %s' % dictionary_file
    cazy_dictionary = pickle.load(filedict)
    print 'Loading complete'
    family_output_dictionary = {}

    print 'Starting scoring process'
    entry_counter = 0
    for line in filein:
        entry_counter = entry_counter + 1
        # Split line from blast output
        line = line.split('\t')
        # Get subject from blast output
        subject = line[1]
#        print subject
        # Get info for that subject in dictionary
        new_dictionary_entry = cazy_dictionary.get(subject)
        if new_dictionary_entry == None:
            print 'Could not find data for %s' % subject
            print 'Please check you are using the correct dictionary file'
            sys.exit(0)
         # Obtain CAZy family
        family = new_dictionary_entry[1]
        # Entry family name in results dictionary
        # If there is no result use zero as the initial count
        initial_count = family_output_dictionary.get(family, 0)
        # Update count
        updated_count = initial_count + 1
        # Update entry in dictionary
        family_output_dictionary[family] = updated_count

    print 'Found a total of %s entries' % entry_counter
    print 'And a total of %d families' % len(family_output_dictionary.keys())
    print 'Writing to %s' % output_file

    # write family_dictionary
    for key, value in family_output_dictionary.iteritems():
        fileout.write("%s\t%d\n" % (key, value))
    fileout.close()
    filein.close()
    filedict.close()

# the main function
main(sys.argv[1:])
