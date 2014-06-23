#!/usr/bin/python
# File created on 28 Feb 2014.
from __future__ import division

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"


import sys
from Bio import SeqIO
from Bio.SeqIO.FastaIO import FastaWriter
import re 
import inspect
from commands import getstatusoutput
from optparse import OptionParser

#config = load_config()
script_info={}
script_info['brief_description'] = """Converts fastq to fasta"""
script_info['script_description'] = """Read fastq with Biopython, writes fasta
             REQUIRED: You must have a fasta file"""
script_info['script_usage'] = []

usage= """
Need to run it like this:
./fastq.to.fasta.py  -i input_file"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest="input_fp",
                  help='the input fastq file [REQUIRED]')


# Creates an input output pair if input is just an input file
def create_an_inputs_and_output(input_file):
   input_output = []
   # finds file format removes extension, case insensitive search
   shortname = re.sub('[.](fastq$|fq$)','',input_file, re.I)
   output_file = shortname+".fasta"
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
   filein = open(list_of_files[0], 'r')
   fileout = open(list_of_files[1], 'w')

   for record in SeqIO.parse(filein,"fastq"):
      fileout.write('>%s\n%s\n' % (record.name, record.seq))
   filein.close()
   fileout.close()

# the main function 
main(sys.argv[1:])    

