#!/usr/bin/python

"""
File created on 28 Feb 2014.
By Erick Cardenas Poire
Multiprocessor part added on jan 2016 based on code from Zach Charlop-Powers
https://gist.github.com/zachcp/c45433307a292513af41

"""
from __future__ import with_statement
import sys
import os

from Bio import SeqIO
from Bio.SeqIO.FastaIO import FastaWriter
from Bio.SeqIO.QualityIO import FastqGeneralIterator

import re 
from optparse import OptionParser
import multiprocessing


script_info = {}
script_info['brief_description'] = """Converts fastq to fasta"""
script_info['script_description'] = """Read fastq with Biopython, writes fasta
             REQUIRED: You must have a fasta file"""
script_info['script_usage'] = []

usage = """
Need to run it like this:
./fastq.to.fasta.py  -i input_file"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest = "input_fp",
                  help = 'the input fastq file [REQUIRED]')
parser.add_option("-p", "--cpu", dest = "n_processors",
                  help = 'the number of processors used [OPTIONAL]', default = 1)


# Creates an output file based on the name of the input file
# output is a list with input and the output names
def create_an_inputs_and_output(input_file):
   input_output = []
   # finds file format removes extension, case insensitive search
   shortname = re.sub('[.](fastq$|fq$)','',input_file, re.I)
   output_file = shortname + ".fasta"
   input_output.append(input_file)
   input_output.append(output_file)
   return input_output

def create_an_inputs_and_output(input_file):
   # finds file format removes extension, case insensitive search
   shortname = re.sub('[.](fastq$|fq$)','',input_file, re.I)
   output_file_name = shortname + ".fasta"
   return output_file_name

# Receives fastq data as tuples and returns only the title and the sequence
def process_fastq(fastq_data):
   title, seq, qual = fastq_data
   return ">%s\n%s\n" %(title, seq)

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

   num_processors = int(opts.n_processors)

   # Initialize a pool of processing nodes
   proc_pool = multiprocessing.Pool(num_processors)
   
   # initialize the input directory or file
   input_fp = opts.input_fp 
   output_fp = create_an_inputs_and_output(input_fp)

   # Start processing
   with open(input_fp, 'r') as filein:
      with open(output_fp, 'w') as fileout:
         # FastqGeneralIterator passes fastq records as string tuples
         fastqs = (record for record in FastqGeneralIterator(filein))
         results = proc_pool.imap(process_fastq, fastqs)
         for result in results:
            fileout.write(str(result))
   
  
# the main function 
main(sys.argv[1:])    

