#!/usr/bin/python
# File created on 28 Feb 2014.

# Author__ = "Erick Cardenas Poire"

import sys
from Bio import SeqIO
from Bio import Entrez
from Bio.SeqIO.FastaIO import FastaWriter
import re 
import inspect
from commands import getstatusoutput
from optparse import OptionParser
Entrez.email = "carden24@mail.ubc.ca"


script_info = {}
script_info['brief_description'] = """Gets protein from nucleotide accession"""
script_info['script_description'] = """Check accession number and retrieve
protein sequences from CDS 
"""
script_info['script_usage'] = []

usage = """
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

#create a list with the names of the sequences requested
def get_list_of_requested_accessions(file_in):
    requested_sequences = {}
    #requested_sequences = []
    for record in SeqIO.parse(file_in,"fasta"):
        record_name = str(record.name)
        full_description = str(record.description).split()
        if len(full_description) == 6:
            dict_entry = full_description[0]
            requested_sequences[record_name] = dict_entry
        else:
            dict_entry0 = full_description[5].split('#')
            dict_entry = dict_entry0[0]
            requested_sequences[record_name] = dict_entry
        #requested_sequences.append(str(record.name))
    return requested_sequences


# retrieving nucleotide accesion and printing protein data
def get_proteins(accession_list, filein, fileout):
    handle = Entrez.efetch(db="nucleotide", id=accession_list.keys(), rettype="gb", retmode="text")
    records = SeqIO.parse(handle, "genbank")
    for record in records:
        print record.locus
        nucleotide_id0 = record.id
        nucleotide_id = nucleotide_id0.split('.')
        nucleotide_id = nucleotide_id[0]
        print nucleotide_id
        dict_entry = accession_list.get(nucleotide_id)
        print dict_entry
        #if dict_entry == None:
        #    print record
        annotations = record.annotations
        taxo = annotations.get('taxonomy')
        #print taxo
        #my_locus = record.ID
        feat = record.features
        for f in feat:
            #print ''
            #print f
            break
            if f.type == "CDS":
                quali = f.qualifiers
                gene = str(quali.get('gene', 'no_gene_name'))
                gene = gene.strip('\'[]')
                if gene == 'nifH':
                #product = str(quali.get('product', 'no_product_name'))
                #product = product.strip('\'[]')
                #Print product
                #Description=gene+'-'+product
                    protein_id = str(quali.get('protein_id', 'no_protein_id'))
                    protein_id = str(f.qualifiers['protein_id'])
                    protein_id = protein_id.strip('\'[]')
                    translated_protein = str(quali.get('translation', 'no_translation'))
                    #translated_protein=str(f.qualifiers['translation'])
                    translated_protein = translated_protein.strip('\'[]')
                    #fileout.write(">%s %s\n%s\n" %(protein_id, gene, translated_protein))
                    fileout.write(">%s %s\n%s\n" %(nucleotide_id, taxo, translated_protein))
            else:
                continue
    fileout.close()



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

    # Get list of accesions
    accession_list = get_list_of_requested_accessions(filein)

    # Process genbanks
    get_proteins(accession_list, filein, fileout)

# the main function 
main(sys.argv[1:])    

