#! /bin/bash
cd ~
cd fastq/
for i in *.fastq;do ~/tools/FastQC/fastqc -noextract $i;done
