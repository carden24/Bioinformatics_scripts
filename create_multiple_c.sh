for i in query*;do echo -e '#!/bin/bash\n#PBS -l procs=1\n#PBS -l walltime=04:45:00\n#PBS -l pmem=1g\n#PBS -N 1'$i'\n#PBS -m abe\n#PBS -M carden24@mail.ubc.ca\n\nblastx -db ~/blastsearch/db/CAZy.GH.GT.CE.PL-2011-08-05 -max_target_seqs 1 -evalue 1e-5 -num_threads 1 -outfmt 6 -query ~/scratch/reads/OM0C0-M2/'$i' -out ~/scratch/reads/OM0C0-M2/'$i.vs.cazy.out > $i.sh; done



