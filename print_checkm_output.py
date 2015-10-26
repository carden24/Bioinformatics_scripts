# Usage python ./print_checkm_outpu.py <file.tsv>

import ast
import sys

file_input = open(sys.argv[1], 'r')

for line in file_input:
   line = line.split('\t')
   bin = line[0]
   line2 = line[1]
   dict = {}
   dict = ast.literal_eval(line2)
   print ('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %(sys.argv[1], \
   bin, dict['marker lineage'], dict[ 'Genome size'], dict[ 'N50 (contigs)'], dict['GC'], dict['Completeness'], dict['Contamination']))