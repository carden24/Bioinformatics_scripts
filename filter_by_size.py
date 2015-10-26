#!/usr/bin/python
# File created on 13 Feb 2014.
from __future__ import division

__author__ = "Erick Cardenas Poire"
__copyright__ = "Copyright 2014"
__credits__ = [""]
__version__ = "1.0"
__maintainer__ = "Erick Cardenas Poire"
__status__ = "Release"

try:
   import sys
   import Bio
   from Bio import SeqIO
   from optparse import OptionParser
   from commands import getstatusoutput
   from os import makedirs, sys, listdir, environ, path
   import re 
   import inspect
   import shutil 




except:
   print """Could not load some required modules"""
   print """Check if you have Biopython installed"""
   sys.exit(3)


#config = load_config()
script_info = {}
script_info['brief_description'] = """Filters sequence according to a minimum size parameter"""
script_info['script_description'] = """Reads sequences, calculates size and writes to output 
             if length is more or equal to size parameter
             REQUIRED: You must have a fasta and size parameter"""
script_info['script_usage'] = []

usage = """
Sorry to bother you, but you
need to run it like this:
python filter.by.size.py -i <filein> > -s <size.threshold>
"""

parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest = "input_fp",
                  help = 'the input fasta file [REQUIRED]')
parser.add_option("-s", "--input_size", dest = "threshold_size",
                  help = 'the input threshold  [REQUIRED]')




#creates an input output pair
def create_inputs_and_output(input_file):
   input_output = []
   shortname = re.sub('[.](fasta$|fas$|fna$|faa$|fsa$|fa$)','',input_file, re.I)  #finds file format removes extension, case insensitive search
   output_file = shortname + ".filtered.fasta"
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

   # initialize the inputs and outputs
   input_fp = opts.input_fp
   list_of_files=create_inputs_and_output(input_fp)
   size = opts.threshold_size
   fileout = open(list_of_files[1], 'w')
   print ("Filtering out sequences smaller than %s bases" %size)

   #Read sequences and filter
   for seq_record in SeqIO.parse(list_of_files[0], format = "fasta"):
      seq_size = (len(seq_record.seq))
      if float(seq_size) >= float(size):
         fileout.write('>%s %s\n%s\n' %(seq_record.id, seq_record.description, seq_record.seq))
      else:
         continue
   fileout.close()

# the main function 
if __name__ == "__main__":
    main(sys.argv[1:])    




