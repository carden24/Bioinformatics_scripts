#! /bin/sh
sort $1 |uniq > $1.unique
awk -F" " '{printf "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19}' $1.unique > $1.unique.csv

python ~/scripts/score.and.filter.hmm.results.py $1.unique.csv




