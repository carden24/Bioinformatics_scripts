#!/usr/bin/python
# File created on 27 Jan 2012.
from __future__ import division

__author__ = "Kishori M Konwar"
__copyright__ = "Copyright 2010, The EngCyc Project"
__credits__ = ["r"]
__version__ = "1.0"
__maintainer__ = "Kishori M Konwar"
__status__ = "Release"

from os import makedirs, sys, remove
from sys import path

from optparse import OptionParser
from python_modules.engcyc_utils  import parse_command_line_parameters, fprintf
from python_modules.sysutil import getstatusoutput





usage= """./run_pgdb_pipeline.py  -i input_fasta_file -o output_file """
parser = OptionParser(usage)
parser.add_option("-i", "--input_file", dest="input_fasta",
                  help='the input fasta file [REQUIRED]')
parser.add_option("-o", "--output_file", dest="output_file",
                  help='the output fasta file [REQUIRED]')
parser.add_option("-B", "--BLAST_EXEUTABLE", dest="blast_executable",
                  help='the BLAST executable  [REQUIRED]')
parser.add_option("-F", "--FORMAT_EXECUTABLE", dest="formatdb_executable",
                  help='the FORMATDB executable file [REQUIRED]')


def check_arguments(opts, args):
    if opts.input_fasta == None or opts.output_file == None:
       return True
    else:
       return False

class FastaRecord(object):
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

#    return FastaRecord(title, sequence)

def read_fasta_records(input_file):
    records = []
    sequence=""
    name=""
    while 1:
         line = input_file.readline()
         if line == "": 
            if sequence!="" and name!="":
               records.append(FastaRecord(name, sequence))
            return  records

         if line=='\n':
            continue

         line = line.rstrip()
         if  line.startswith(">") :
            if sequence!="" and name!="":
               records.append(FastaRecord(name, sequence))

            name = line.rstrip()
            sequence =""
         else:
            sequence = sequence + line.rstrip()
    return records

def format_db(formatdb_executable, seq_subset_file):
    cmd='%s -p T -i %s' %(formatdb_executable, seq_subset_file.name)
    result= getstatusoutput(cmd)
    

def blast_against_itself(blast_executable, seq_subset_file, blast_table_out):
    cmd='%s -p blastp -m 8 -d %s -i %s -o %s' %(blast_executable,  seq_subset_file.name, seq_subset_file.name, blast_table_out)
    print cmd
    result= getstatusoutput(cmd)

def add_refscore_to_file(blast_table_out, refscore_file):
    infile = open( blast_table_out,'r')

    lines = infile.readlines()
    for line in lines:
       line=line.rstrip()
       fields = line.split('\t')
       if len(fields) != 12:
          print 'Error in the blastout file'
          sys.exit(1)
       if fields[0].rstrip()==fields[1].rstrip():
          fprintf(refscore_file, "%s\t%s\n",fields[0], fields[11]);
    infile.close()
        

# compute the refscores
def compute_refscores(formatdb_executable, blast_executable,seq_subset_file, refscore_file):
    format_db(formatdb_executable, seq_subset_file)
    blast_table_out = seq_subset_file.name + ".blastout"
    blast_against_itself(blast_executable, seq_subset_file, blast_table_out)
    add_refscore_to_file(blast_table_out,refscore_file)
    return None

# the main function
def main(argv): 
    (opts, args) = parser.parse_args()
    if check_arguments(opts, args):
       print usage
       sys.exit(0)

    input_fasta = opts.input_fasta
    output_file = opts.output_file
    blast_executable = opts.blast_executable
    formatdb_executable = opts.formatdb_executable
 
    infile = open(input_fasta,'r')
    outfile = open(output_file, 'w') 

    count = 0

    for record in read_fasta_records(infile):
        if count %20 == 0:
            if count > 0:
              seq_subset_file.close()
              compute_refscores(formatdb_executable, blast_executable,seq_subset_file, outfile);
              remove(seq_subset_file.name)
              remove(seq_subset_file.name +".blastout")
              remove(seq_subset_file.name +".phr")
              remove(seq_subset_file.name +".pin")
              remove(seq_subset_file.name +".psq")

            seq_subset_file = open(output_file +'.tmp.'+ str(count) +'.fasta','w')
            
        fprintf(seq_subset_file, "%s\n", record.name)
        fprintf(seq_subset_file, "%s\n", record.sequence)

        count = count + 1

    if (count-1) %20 != 0:
       seq_subset_file.close()
       compute_refscores(formatdb_executable, blast_executable,seq_subset_file, outfile);
       remove(seq_subset_file.name)
       remove(seq_subset_file.name +".blastout")
       remove(seq_subset_file.name +".phr")
       remove(seq_subset_file.name +".pin")
       remove(seq_subset_file.name +".psq")

    #print count
    outfile.close()

# the main function of EngCyc
if __name__ == "__main__":
    main(sys.argv[1:])

