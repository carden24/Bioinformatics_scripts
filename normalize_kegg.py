#!/usr/bin/python

import sys
from optparse import OptionParser

script_info = {}
script_info['brief_description'] = """This script normalizes the KO count according to the number of read in the library."""

script_info['script_usage'] = []

usage = '''
Usage:  

python normalize_kegg.py -i <kegg table input> -d <list_of_files.txt>
 -o <output text file>
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_kegg_count_file", dest = "input_file",
                  help = 'The tabular input [REQUIRED]')
parser.add_option("-d", "--library_read_ciybt", dest = "dictionary_file",
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

    if output_file == 'None' :
        print 'No output file was specified'
        output_file = input_file + '_normalized'
        print 'Output will be directed to file: %s' %output_file

    # Open input and outputs
    filedict = open(dictionary_file, 'r')
    filein = open(input_file, 'r')
    fileout = open(output_file, 'w')
    if verbose:
        print 'Loading dictionary: %s' %dictionary_file
    
    file_read_count_dict = {}

    for line in filedict:
        #print line
        line = line.strip('\n\r').split('\t')
        #print line
        my_file = line[0]
        file_read_count = line[1]
        file_read_count_dict[my_file] = file_read_count   
    if verbose:
        print 'Loading complete'

    # Normalizing the output
	# This is how the summary file is formatted
	# TXA-OM3C0-O3-3300001461.u.ko_summary.txt
	# This is how the summary file "file" column looks like
	# TXA/TXA-OM3C0/TXA-OM3C0-O3-3300001461.u.ko.txt
	# or
	# TXA-OM3C0-O3-3300001461.u.ko.txt

    if verbose:
        print 'Starting normalization'
    the_read_count = file_read_count_dict.get(input_file, 0)

    if the_read_count == 0:
         print "No read count was found for %s" %input_file
         sys.exit(0)

    for line2 in filein:
        line2 = line2.strip('\n\r').split('\t')  # split the file into three
        the_file0 = line2[0]
        # This takes care of the wd path if it appears
        the_file =  the_file0.split('/')[-1]
        the_KEGG_number = line2[1]
        the_KEGG_count = int(line2[2])
        the_new_KEGG_count = (the_KEGG_count/float(the_read_count)) *1000
        fileout.write('%s\t%s\t%f\n' %(the_file, the_KEGG_number, the_new_KEGG_count))
    if verbose:
        print 'Normalization complete'
    filein.close()
    fileout.close()
    filedict.close()


# the main function
main(sys.argv[1:])





