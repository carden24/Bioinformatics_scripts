for i in *part*;do echo -e '#!/bin/bash\n#PBS -l procs=1\n#PBS -l walltime=00:15:00\n#PBS -l pmem=1g\n#PBS -N 1'$i'\n#PBS -m abe\n#PBS -M carden24@mail.ubc.ca\n\nhmmsearch -E 1e-5 --cpu 1 -A '$i'.sto -o /dev/null --tblout '$i'.txt ~/hmm/11_Nitrate_Reduction.hmm '$i > $i.sh;done

