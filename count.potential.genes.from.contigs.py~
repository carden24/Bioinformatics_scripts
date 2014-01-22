#usage python count.potential.genes.from.contigs.py <orfs.from.contigs.fasta> <Reads.mapping.table> 
#        	0			       		 1			2			

import sys, screed

contigsdict={}
for line in open(sys.argv[2]):
   if line.startswith('ID'):
      continue
   else:
      line=line.split('\t')
      contig_name=line[0]
      contigs_fold=(line[3])
      contig_fold=float(contigs_fold)
      z=contigsdict.get(contig_name,[])
      z.append(contig_fold)
      contigsdict[contig_name]=z

potential_protein=0.0
for record in screed.open(sys.argv[1]):
   seq_name=record.name			#get sequence name
   seq_name=seq_name.split('_')   
   seq_contig=seq_name[0]
   seq_fold=contigsdict.get(seq_contig)
   fold=float(seq_fold[0])
   potential_protein=potential_protein+fold

filein=sys.argv[1]   

print "Protein Potential for %s is: %s" % (filein, potential_protein)
