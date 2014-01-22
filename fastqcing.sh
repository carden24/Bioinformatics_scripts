#PBS -N Fastqcing
#PBS -m abe
#PBS -M carden24@su.edu
#PBS -l walltime=2:00:00
#PBS -l procs=1
#PBS -l pmem=512m


cd ~/scratch/fastq/
~/tools/FastQC/fastqc -noextract OC-OM0C0-M.fastq

