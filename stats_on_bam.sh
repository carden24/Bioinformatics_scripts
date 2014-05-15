#!/bin/sh
#PBS -l nodes=1:ppn=1,walltime=2:00:00,mem=2Gb
#PBS -N Bam_stats
#PBS -m abe
#PBS -M carden24@mail.ubc.ca
#PBS -o Bamstats.txt

cd ~
cd illumina
for i in */*.bam;do /home/carden24/tools/samtools-0.1.18/samtools flagstat $i;done

