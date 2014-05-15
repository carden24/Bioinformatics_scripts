for i in *fasta;do echo $i;

sed 's/contig_//g' $i > $i.2;
mv $i.2 $i;

echo "Counting kmers";
perl ~/tools/multi-metagenome/R.data.generation/calc.kmerfreq.pl -i $i -o $i.kmer.tab -min 0;
echo "Counting GC";
perl ~/tools/multi-metagenome/R.data.generation/calc.gc.pl -i $i -o $i.gc.tab;
echo 'Predicting genes';
~/tools/prodigal.v2_60/prodigal -a $i.temp.orf.faa -i $i -m -o $i.temp.txt -p meta -q;
echo 'Modifying predicted genes';
cut -f1 -d" " $i.temp.orf.faa > $i.final.orfs.faa;
echo 'Searching essential genes';
hmmsearch --tblout $i.hmm.orfs.txt --cut_tc --notextw ~/tools/multi-metagenome/R.data.generation/essential.hmm $i.final.orfs.faa;
echo 'Format magic';
tail -n+4 $i.hmm.orfs.txt |sed 's/ * / /g' |cut -f1,4 -d" " | sed 's/_/ /' > $i.orfs.hmm.id.txt;

tail -n+4 $i.hmm.orfs.txt |cut -f1 -d " " >$i.list.of.positive.orfs.txt;

echo 'Retrieving positive hmm hits';
perl ~/tools/multi-metagenome/R.data.generation/extract.using.header.list.pl -l  $i.list.of.positive.orfs.txt -s $i.final.orfs.faa -o $i.orfs.hmm.faa;

echo 'Blasting essential genes';
blastp -query $i.orfs.hmm.faa -db ~/blastsearch/db/refseq_protein -evalue 1e-5 -num_threads 60 -max_target_seqs 5 -outfmt 5 -out $i.orfs.hmm.blast.xml;

echo 'Running MEGAN';
MEGAN +g -x "import blastfile= $i.orfs.hmm.blast.xml meganfile=temp.rma;recompute toppercent=5;recompute minsupport=1;update;collapse rank=Species;update;select nodes=all;export what=CSV format=readname_taxonpath separator=tab file=$i.orfs.hmm.blast.tax.txt;update;close";
sed 's/\t/;/' $i.orfs.hmm.blast.tax.txt | cut -f1,5 -d ";" | sed 's/;/\t/' | sed 's/_/\t/' > $i.orfs.hmm.blast.tax.tab;

echo 'Aggregating results at scaffold level';
perl ~/tools/multi-metagenome/R.data.generation/hmm.majority.vote.pl -i $i.orfs.hmm.blast.tax.txt -o $i.tax.consensus.txt -n;

python ~/scripts/fasta.stats.v3.py $i > $i.length.tab;

done

