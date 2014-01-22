#!/bin/sh
#PBS -l walltime=4:00:00
#PBS -l procs=1
#PBS -l pmem=2g
#PBS -N Bam_stats
#PBS -m abe
#PBS -M carden24@msu.ca
#PBS -o Bamstats.txt

cd ~
for i in */*/*/*.bam;do echo $i;/home/carden24/tools/samtools-0.1.18/samtools flagstat $i;done

