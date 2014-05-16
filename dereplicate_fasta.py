#!/usr/bin/python
from __future__ import division

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"

try:
    from Bio import SeqIO
    import sys
    import inspect
    from optparse import OptionParser
    import re
except:
     import_exception = """ Could not load some modules """
     print import_exception 
     sys.exit(3)



# config = load_config()
script_info={}
script_info['brief_description'] = """Dereplicates sequences based on name"""""
script_info['script_description'] = """
	    REQUIRED: Fasta file
	    REQUIRED Modules: Biopython"""

script_info['script_usage'] = []

usage = '''
Usage:  
python dereplicate_fasta.py -i <input fasta>

Dependency: 	i) Biopython
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_fasta", dest="input_fp",
                  help='The input fasta file [REQUIRED]')

# checks if the supplied arguments are adequate
def valid_arguments(opts, args):
    if opts.input_fp == None :
        return True
    else:
        return False

def create_output_name(input_file):
    shortname = re.sub('[.](fasta$|fas$|faa$|fsa$|fa$)', '', input_file, re.I)
    output_file_name = shortname + ".unique.fasta"
    return output_file_name

def main(argv):
    (opts, args) = parser.parse_args()
    print ''
    print 'Initializing...'

    if valid_arguments(opts, args):
        print usage
        sys.exit(0)

    # initialize the input directory or file
    input_fp = opts.input_fp 

    #Create output file
    output_fp = create_output_name (input_fp)
    fileout = open (output_fp, 'w')

    #Create empty list
    fasta_names = []
    removed_counter = 0

    for record in SeqIO.parse ( input_fp,"fasta" ) :
        if record.name not in fasta_names:
            fasta_names.append ( record.id )
            fileout.write ('>%s\n%s\n' % (record.description, record.seq))
#        if record.name in fasta_names:
        else:
            removed_counter = removed_counter + 1
            text = '\r   Replicated sequence found. Skipped %d' %removed_counter
            sys.stderr.write(text)
            sys.stderr.flush()
            continue
 
# the main function
 main(sys.argv[1:])
