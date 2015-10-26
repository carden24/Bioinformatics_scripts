for i in query*;do echo -e '#!/bin/bash\n#PBS -l procs=1\n#PBS -l walltime=00:13:00\n#PBS -l pmem=1g\n#PBS -N 1'$i'\n#PBS -m abe\n#PBS -M carden24@mail.ubc.ca\n\nblastx -db ~/blastsearch/db/FOLy-2012-01-05 -max_target_seqs 1 -evalue 1e-5 -num_threads 1 -outfmt 6 -query ~/scratch/reads/OM0C0-M2/'$i' -out ~/scratch/reads/OM0C0-M2/'$i.vs.foly.out > $i.sh; done


