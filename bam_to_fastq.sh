#!/bin/sh
#PBS -l nodes=1:ppn=1,walltime=2:00:00,mem=2Gb
#PBS -N Bam_to_fastq.
#PBS -m abe
#PBS -M carden24@mail.ubc.ca

cd ~
cd illumina

java -Xmx2g -jar /global/software/picard/picard157/picard-tools-1.57/SamToFastq.jar INPUT= INX752_D0DWKACXX_1_CAAAAG.bam OUTPUT_PER_RG=True OUTPUT_DIR=.
