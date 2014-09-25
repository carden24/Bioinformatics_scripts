#usage python genbank.to.table.py <genbank.input>
#        	0			       1

import sys
import re
from Bio import SeqIO
from optparse import OptionParser


#config = load_config()
script_info = {}
script_info['brief_description'] = """Converts genbank file to table"""
script_info['script_description'] = """Converts genbank file to table
             REQUIRED: You must have a genbank file"""
script_info['script_usage'] = []

usage= """
Need to run it like this:
./genbank_to_table.py  -i input_file
For more options:  ./genbank_to_table.py -h"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest = "input_fp",
                  help = 'the input genbank file [REQUIRED]')


#creates an input output pair if input is just an input file
def create_an_inputs_and_output(input_file):
    #finds file format removes extension, case insensitive search
    shortname = re.sub('[.](gb$|genbank$|gbk$)', '', input_file, re.I) 
    output_file = shortname + ".txt"
    return output_file

def main(argv):
    (opts, args) = parser.parse_args()

    # initialize the input file, create output file
    input_fp = opts.input_fp 
    output_file = create_an_inputs_and_output(input_fp)
    fileout = open(output_file, 'w')

    for seq_record in  SeqIO.parse(input_fp, "genbank"):
        feat = seq_record.features
        for f in feat:
            if f.type == "CDS":
                location = str(f.location)
                loca = location.strip('[]\'')
                coordinates = loca.split(':')
                beginning = str(coordinates[0])
                end = str(coordinates[1])
                try:
                    product = str(f.qualifiers['product'])
                    prod = product.strip('[]\'')
                except KeyError:
                    prod = 'No product'
                locus = str(f.qualifiers['locus_tag'])
                loc = locus.strip('[]\'')
                fileout.write ("%s\t%s\t%s\t%s\t%s\n" %(loc, beginning, end, prod, seq_record.id))
            else:
                continue

    fileout.close()

# the main function 
main(sys.argv[1:])
