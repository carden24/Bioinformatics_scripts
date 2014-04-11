#!/usr/bin/env sh

# Yanbin Yin
# 08/18/2011
# hmmscan output parser
# Usage: sh hmmscan-parser.sh hmmscan-output-file

# 1. take hmmer3 output and generate the tabular output
# 2. sort on the 6th and 7th cols
# 3. remove overlapped/redundant hmm matches and keep the one with the lower e-values
# 4. calculate the covered fraction of hmm (make sure you have downloaded the "all.hmm.ps.len" file to the same directory of this perl script)
# 5. apply the E-value cutoff and the covered faction cutoff
cat $1 | perl -e 'while(<>){if(/^\/\//){$x=join("",@a);($q)=($x=~/^Query:\s+(\S+)/m);while($x=~/^>> (\S+.*?\n\n)/msg){$a=$&;@c=split(/\n/,$a);$c[0]=~s/>> //;for($i=3;$i<=$#c;$i++){@d=split(/\s+/,$c[$i]);print $q."\t".$c[0]."\t$d[6]\t$d[7]\t$d[8]\t$d[10]\t$d[11]\n" if $d[6]<1;}}@a=();}else{push(@a,$_);}}' \
	| sort -k 1,1 -k 6,6n -k 7,7n | uniq \
        | perl -e 'while(<>){chomp;@a=split;next if $a[-1]==$a[-2];push(@{$b{$a[0]}},$_);}foreach(sort keys %b){@a=@{$b{$_}};for($i=0;$i<$#a;$i++){@b=split(/\t/,$a[$i]);@c=split(/\t/,$a[$i+1]);$len1=$b[-1]-$b[-2];$len2=$c[-1]-$c[-2];$len3=$b[-1]-$c[-2];if($len3>0 and ($len3/$len1>0.5 or $len3/$len2>0.5)){if($b[2]<$c[2]){splice(@a,$i+1,1);}else{splice(@a,$i,1);}$i=$i-1;}}foreach(@a){print $_."\n";}}' \
        | uniq | perl -e 'open(IN,"all.hmm.ps.len");while(<IN>){chomp;@a=split;$b{$a[0]}=$a[1];}while(<>){chomp;@a=split;$r=($a[4]-$a[3])/$b{$a[1]};print $_."\t".$r."\n";}' \
	| perl -e 'while(<>){@a=split(/\t/,$_);if(($a[-1]-$a[-2])>80){print $_ if $a[2]<1e-5;}else{print $_ if $a[2]<1e-3;}}' | awk '$NF>0.3'
