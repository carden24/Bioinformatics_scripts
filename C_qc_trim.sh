#!/bin/bash
#PBS -N Fq.trimm.OC-OM2C0-M2_1
#PBS -l walltime=2:45:00
#PBS -l procs=1
#PBS -l pmem=2g
#PBS -m bea
#PBS -M carden24@msu.edu
#PBS -o OC-OM2C0-M2_1.txt

cd ~
cd fastq
python ~/lib/quality-trim.py OC-OM2C0-M2_1.fastq OC-OM2C0-M2_1.trimmed.fastq
#OC-OM2C0-M2_2.fastq
#OC-OM2C0-M3_1.fastq
#OC-OM2C0-M3_2.fastq
#OC-OM2C0-O1_1.fastq
#OC-OM2C0-O1_2.fastq
#OC-OM2C0-O2_1.fastq
#OC-OM2C0-O2_2.fastq
#OC-OM2C0-O3_1.fastq
#OC-OM2C0-O3_2.fastq
#OC-OM3C0-M1_1.fastq
#OC-OM3C0-M1_2.fastq
#OC-OM3C0-M2_1.fastq
#OC-OM3C0-M2_2.fastq
#OC-OM3C0-M3_1.fastq
#OC-OM3C0-M3_2.fastq
