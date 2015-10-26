#!/usr/bin/python
# File created on 13 Feb 2014.

# Author = "Erick Cardenas Poire"


import pickle
import sys
import Bio
from Bio import SeqIO
import re
from optparse import OptionParser

#config = load_config()
script_info={}
script_info['brief_description'] = """ This script will parse the CAZy database 
             file and generate a dictionary that will be stored as a pickle object"""

script_info['script_usage'] = []

usage = '''
Usage:  
./HMM.search.and.parse.and.extract.py -i <input proteins> -m <hmm database>
 -o <output directory>

python create_newcazy_dictionary.py -i <fasta.file> -o <output.pkl.file> 


DEPENDENCIES: 	i)Biopython
'''

parser = OptionParser(usage)
parser.add_option("-i", "--input_fasta", dest = "input_file",
                  help = 'The input fasta protein [REQUIRED]')
parser.add_option("-o", "--output_pickle", dest = "output_file",
                  help = 'The output file [REQUIRED]')

# checks if the supplied arguments are adequate
def valid_arguments(opts, args):
    if (opts.input_file == None or opts.output_file == None ):
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

    # initialize the input directory or file
    input_file = opts.input_file 
    output_file = opts.output_file 
    filein = open(input_file,'rb')
    fileout = open(output_file,'w')

    cazydict = {}
    counter = 0
    for seq_record in SeqIO.parse(filein, format = "fasta"):
        description = seq_record.description
#        print seq_record.id
        subject = seq_record.name
        # Capture organism information
        organismsearch = re.search('(\[)([A-Za-z0-9\.\_\-\s\'\/\=\#\(\)\:\*\&]+)(\])', description)
        if organismsearch == None:
            organism = "None"
        else:
            organism = organismsearch.group(0)
            organism = organism.strip('[]')

        # Capture CAZy family information
        description_search = re.search(' (\()([AGCP])([AHTEL])(\:)([A-Z0-9_]+)(\))', description)
        if description_search == None:
            print 'No CAZY family found for:'
            print description
        familydata = description_search.group(0)
        the_cazy_class = familydata.split(':')
        cazy_class = the_cazy_class[0].strip(' (')
        cazy_family_number = the_cazy_class[1].strip(')')
        if cazy_family_number.find('_') != -1:
            # if there is subfamily information just ignore it
            # And use the family information instead
            cazy_family_number.split('_')
            cazy_family_number = cazy_family_number[0]
            cazy = cazy_class + cazy_family_number
        else:
            cazy = cazy_class + cazy_family_number

        # Create empty list to append the results 
        result = []
        result.append(description)
        result.append(cazy)
        result.append(cazy_class)
        result.append(organism)

        # Update dictionary with results
        cazydict[subject] = result
        counter = counter + 1
        text = "\r   Sequences found= %s" %counter
        sys.stderr.write(text)
        sys.stderr.flush()
    print ''
    print 'writing to %s' %output_file
    pickle.dump(cazydict,fileout)


# Run main function 
main(sys.argv[1:])
