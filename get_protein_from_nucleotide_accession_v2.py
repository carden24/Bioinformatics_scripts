

#!/usr/bin/python
# File created on 28 Feb 2014.

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"

import sys
from Bio import SeqIO
from Bio import Entrez
from Bio.SeqIO.FastaIO import FastaWriter
import re 
import inspect
from commands import getstatusoutput
from optparse import OptionParser
Entrez.email = "carden24@mail.ubc.ca"
import time


script_info = {}
script_info['brief_description'] = """Gets protein from nucleotide accession"""
script_info['script_description'] = """Check accession number and retrieve
protein sequences from CDS 
"""
script_info['script_usage'] = []

usage= """
Need to run it like this:
./get_protein_from_nucleotide_accession.py -i input_file"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest = "input_fp",
                  help = 'the input fastq file [REQUIRED]')


# Creates an input output pair if input is just an input file
def create_an_inputs_and_output(input_file):
    input_output = []
    # finds file format removes extension, case insensitive search
    shortname = re.sub('[.](fasta$|fa$|fna$)','',input_file, re.I)
    output_file = shortname + ".faa"
    input_output.append(input_file)
    input_output.append(output_file)
    return input_output


# checks if the supplied arguments are adequate
def valid_arguments(opts, args):
    if opts.input_fp == None:
        return True
    else:
        return False


def main(argv):
    (opts, args) = parser.parse_args()
    if valid_arguments(opts, args):
        print usage
        sys.exit(0)

    # initialize the input directory or file
    input_fp = opts.input_fp 
    list_of_files = create_an_inputs_and_output(input_fp)
    filein  = open(list_of_files[0], 'r')
    fileout = open(list_of_files[1], 'w')

    for fasta_record in SeqIO.parse(filein,"fasta"):
        record_name = str(fasta_record.name)
        full_description = str(fasta_record.description).split()
        if len(full_description) == 6:
            dict_entry = full_description[0]
        else:
            dict_entry0 = full_description[5].split('#')
            dict_entry = dict_entry0[0]
        #print record_name
        #print dict_entry
        handle = Entrez.efetch(db = "nucleotide", id = record_name, rettype = "gb", retmode = "text")
        records = SeqIO.parse(handle, "genbank")
        time.sleep(0.5)
        for record in records:
            #print record
            annotations = record.annotations
            taxo = annotations.get('taxonomy')
            feat = record.features
            if dict_entry.count('.') > 1:
                #print 'use coordinates'
                for f in feat:
                    if f.type == "CDS":
                        try:
                            coordinates0 = str(f.location)
                            coordinates = coordinates0.lstrip('[').rstrip('\n').split(']')
                            coordinates = coordinates[0]
                            end0 = coordinates.split(':')
                            end = end0[1]
                            other_end0 = dict_entry.split('..')
                            other_end = other_end0[1]
                            #print '%s %s' %(end, other_end)
                
                            if end == other_end :
                                #print 'found gene'
                                quali = f.qualifiers
                                protein_id = str(quali.get('protein_id', 'no_protein_id'))
                                protein_id = protein_id.strip('\'[]')
                                translated_protein = str(quali.get('translation', 'no_translation'))
                                translated_protein = translated_protein.strip('\'[]')
                                fileout.write(">%s %s %s\n%s\n" %(record_name, protein_id, taxo, translated_protein))
                            else:
                                #print 'not the gene'
                                continue
                                                             
                        except AttributeError:
                            continue
                    else:
                        continue        

            else:
                #print 'use gene'
                for f in feat:
                    if f.type == "CDS":
                        quali = f.qualifiers
                        protein_id = str(quali.get('protein_id', 'no_protein_id'))
                        protein_id = protein_id.strip('\'[]')
                        translated_protein = str(quali.get('translation', 'no_translation'))
                        translated_protein = translated_protein.strip('\'[]')
                        fileout.write(">%s %s %s\n%s\n" %(record_name, protein_id, taxo, translated_protein))
                    else:
                        continue
    fileout.close()

# the main function 
main(sys.argv[1:])    

