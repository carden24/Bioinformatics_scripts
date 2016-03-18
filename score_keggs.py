#!/usr/bin/python

import sys
import subprocess
import re
from optparse import OptionParser

script_info = {}
script_info['brief_description'] = """This script converts a tabular KO summary 
into a table with count for each KEGG Module """

script_info['script_usage'] = []

usage = '''
Usage:  

python score_keggs_to_module.py -i <IMG kegg tabular input> -d <kegg dictionary>
 -o <output text file>
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_kegg_input", dest = "input_file",
                  help = 'The tabular input [REQUIRED]')
parser.add_option("-d", "--kegg_dictionary", dest = "dictionary_file",
                  help = 'The dictionary file [REQUIRED]')
parser.add_option("-o", "--output_table", dest = "output_file", default = 'None',
                  help = 'The output file [OPTIONAL]')
parser.add_option("-v", action="store_true", dest="verbose")




# checks if the supplied arguments are adequate
def valid_arguments(opts, args):
    if (opts.input_file == None or opts.dictionary_file == None ):
        return True
    else:
        return False

   
def main(argv):
    (opts, args) = parser.parse_args()
    verbose = opts.verbose
    parser.set_defaults(verbose=False)

    if verbose:
        print ''
        print "Verbosity is on"
    if verbose:
        print 'Initializing...'

    if valid_arguments(opts, args):
        print usage
        sys.exit(0)

    # initialize the input file, dictionary, and output file
    input_file = opts.input_file 
    dictionary_file = opts.dictionary_file
    output_file = opts.output_file
    if output_file == 'None':
        output_file = input_file + '_' + dictionary_file
        if verbose:
            print 'No output file was specified'
            print 'Output will be directed to file: %s' %output_file

    # Open input and outputs
    filedict = open(dictionary_file, 'r')
    filein = open(input_file, 'r')
    fileout = open(output_file, 'w')

    ko_count = {}
    # Ko6506	K06478	K06458	K06459	K01488	K06713	K06450	K06451	K06454
    for line in filedict:
        line = line.strip('\n\r').split("\t")
        my_key = line[0]
        my_results = line[1:len(line)]
        for result in my_results:
            p = subprocess.Popen('grep %s %s' %(result, input_file), stdout=subprocess.PIPE, shell=True)
            node0 = p.communicate()[0]
            if len(node0) == 0:
                continue
            else:
                node1 = node0.strip('\r\n').split('\t')
                count = float(node1[2])    
                current_count =  ko_count.get(my_key, 0)
                new_count = current_count + count
                ko_count[my_key] = new_count
              
#    print ko_count
    # write family_dictionary
    for key, value in ko_count.iteritems():
        fileout.write("%s\t%s\t%f\n" %(input_file, key, value))
# the main function
main(sys.argv[1:])
