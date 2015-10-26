#!/usr/bin/python
# File created on 3 Mar 2014.

# author__ = "Erick Cardenas Poire"

# Usage python ./score_cgff.py <prodigal_output.gff>

import sys
import re

#3300001079.a:JGI12696J13243_100010     Prodigal_v2.6.2 CDS     315     1454    132.9   -       0       ID=1_1;partial=00;start_type=ATG;rbs_motif=3Base/5BMM;rbs_space$

filein = open(sys.argv[1], 'r')
shortname = re.sub('[.](gff)', '', sys.argv[1], re.I)
output_file = shortname + "_summary.txt"
fileout = open(output_file, 'w')

contig_length_dictionary = {}

for line in filein:
   if line.startswith('#'):
      continue
   else:
      # Split line from results
      line = line.split('\t')
      contig = line[0]
      score_group = line[8]
      score_column = score_group.split(';')
      score_column = score_column[8]
      score = score_column.split('=')
      score = float(score[1])
      # Get current contig score, if not found use zero
      temp_score = contig_length_dictionary.get(contig, 0)
      new_score = temp_score + score
      contig_length_dictionary[contig] = new_score

for key, value in contig_length_dictionary.iteritems():
   fileout.write("%s\t%s\t%s\n" %(sys.argv[1], key, value))

filein.close()
fileout.close()

import os
output_file2 = shortname + "_table.csv"

print 'Reformating table'
os.system(' '.join(['Rscript ~/scripts/three_column_table_to_matrix.R',output_file,output_file2]))





