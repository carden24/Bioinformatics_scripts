#!/usr/bin/perl -w
use strict;
use POSIX qw(strftime);
use Data::Dumper;

use Getopt::Long;
use POSIX qw(ceil);

my $OUTPUT;
my $INPUT;
my $result=0;
my $BLOCKSIZE=1000;
my $DEBUG;
my $CPUS=8;

my ($BLASTN)= grep {-e} map {"$_/blastn"} split(/:/,$ENV{'PATH'});
if (!defined $BLASTN) { $BLASTN="/usr/local/ncbi/bin/blastn";}
if (!-f $BLASTN || !-x _) { die("$BLASTN isn't an executable file!");}

my ($BLASTP)= grep {-e} map {"$_/blastp"} split(/:/,$ENV{'PATH'});
if (!defined $BLASTP) { $BLASTP="/usr/local/ncbi/bin/blastp";}
if (!-f $BLASTP || !-x _) { die("$BLASTP isn't an executable file!");}

my ($MAKEBLASTDB)= grep {-e} map {"$_/makeblastdb"} split(/:/,$ENV{'PATH'});
if (!defined $MAKEBLASTDB) { $MAKEBLASTDB="/usr/local/ncbi/bin/makeblastdb"; }
if (!-f $MAKEBLASTDB || !-x _) { die("$MAKEBLASTDB isn't an executable file!");}

# If there are command line arguments:
if (defined $ARGV[0]) {
  # Process command line arguments
  $result=GetOptions(
    "blocksize:i"=>\$BLOCKSIZE,  # How much to make into blocks?
    "cpus:i"=>\$CPUS,  # How many cpus to use?
    "debug"=>\$DEBUG,  # Debug the program
    "output=s"=>\$OUTPUT);  # One output file

  # The input files without flags, so you can use wildcards.
  $INPUT=$ARGV[0];
}

# Usage, or bad arguments:
if (!$result or !defined $OUTPUT or !defined $INPUT) {
  die("Usage: $0 [-b blocksize] -o output.csv input.fasta
  
    This program will read the input FASTA file and produce a CSV file
    containing the reference score of each FASTA sequence blasted against
    itself.

    -o output.csv: the name of the output file.

    -d: debug mode, which writes stats to 'stats.csv' and quits after 3 blocks
    -b blocksize: the size of chunks to self-blast (default $BLOCKSIZE)
    -c cpus: how many cpus to use, -a option for blastall (default $CPUS)\n");
}

my $prog;

# Read in the data:
if(!-f $INPUT || !-r _) { die("$INPUT isn't a readable file!"); }

my $start=time();
my $last=$start;
my $size=-s $INPUT;
if ($size==0) {die("$INPUT is empty?\n");}

my $count=0;

open(IN,"<$INPUT") or die("$INPUT: $!");
open(OUT,">$OUTPUT") or die("$OUTPUT: $!");
my $I="/tmp/bl2seq.$$.txt";
open(OUT2,">$I") or die("$I: $!");
if (defined $DEBUG) {open(STAT,">>stats.csv") or die("stats.csv: $!");}

local $/="\n>";
while (<IN>) {
  $count++;
  s/^>?/>/s;  s/>$//s; # Fixup $/ hack; line will start with '>' and end with '\n'
  # Parse into header and sequence values ($1,$2):
  if (!m/^>(\S[^\n]*)\n(.*)$/s) { die("\nThis line (from $INPUT) was weird:\n".substr($_,0,100)."\n"); }

  my $p=tell(IN)/$size;
  my $duration=(time()-$start)||1;
  my $eta=$duration/$p;
  my $rate=$count/$duration;
  #if ($duration>1 and $last!=time() and (time()%5)==0) {
  if ($duration>1 and $last!=time()) {

    # Debugging code:
    if (defined $DEBUG) {
    #if (defined $DEBUG and $count>$BLOCKSIZE*3) {
      if ($DEBUG<2) {
        $DEBUG=2;
        print STAT "# time,tell,size,percent,duration,eta,count,rate\n";
        print "Statistics are being written to stats.csv\n";
      }
      print STAT time().",@{[tell(IN)]},$size,$p,$duration,$eta,$count,$rate\n";
      #exit 0;
    }

    printf STDERR "\rPercent done: %2.1f%%  ETA: %s  Rate: %2.1f seqs/sec      ", $p*100, strftime("%Y-%m-%d %H:%M:%S",localtime($eta+$start)),$rate;
    $last=time();
  }
  process($1,$2);
}
$count=0;
process("","");# Final process update

close(IN);
close(OUT);
close(OUT2);

sub process {
  my ($q,$s)=@_;
  if (!defined $prog) {
    $prog="T"; # protein=true
    if ($s=~m/^[abcdghkmnrstuvwyx\n ]+\s*$/i) { $prog="F"; } # Protein = false
  }
  if ($q ne "") {print OUT2 ">$q\n$s";} # $q == "" if end of input reached; clear out remaining sequences.

  local $/="\n";

  if (($count%$BLOCKSIZE)==0) {
    # MacosX Snowleopard takes its time to update the file's size; it claims $I is empty.
    #my $sz=getsize($I);
    #if ($sz == 0) {die("-z $I is zero");return;} # Empty file - give up!
    #print STDERR "Looking at $I\n";
    my $cmd1="cd /tmp;$MAKEBLASTDB -in $I -dbtype ".(($prog eq "T")?"prot":"nucl");
    my $r1=`$cmd1 2>&1`;
    if (! defined $r1) {die("Command not found: $cmd1");}
    if ($r1 !~ m/Adding sequences from FASTA/) {die("Strange result from '$cmd1':\n$r1");}

    my $cmd2="cd /tmp;$BLASTN -evalue 80 -num_threads 7 -outfmt 6 -dust no -db $I -query $I -out $I.blastout -max_target_seqs 1 -perc_identity 100";
    if ($prog eq "T") {
      $cmd2="cd /tmp;$BLASTP -evalue 80 -num_threads 7 -outfmt 6 -seg no -db $I -query $I -out $I.blastout -max_target_seqs 1";
    }
    my $r2=`$cmd2 2>&1`;
    if (!defined $r2 or $r2 ne "") {die("Strange result from '$cmd2'\nr2=$r2");}

    # Load the list of queries into %hits, and put them into %lookup
    my %hits;
    my $seqnum=0;
    my %lookup;
    open(IN2,"<$I") or die("$I: $!");
    while (my $k=<IN2>) {
      if ($k=~m/^>\s*(\S+)/){
        $hits{$1}=1;
        $lookup{"gnl|BL_ORD_ID|$seqnum"}=$1; # Formatdb from blast++ does this
        $lookup{$1}=$1; # Identity transformation for older blast
	$seqnum++;
      } 
    }
    close(IN2);

    # Tr1560_1000	Tr1560_1000	100.00	54	0	0	1	54	1	54	4e-28	 110
    open(IN2,"<$I.blastout") or die("$I.blastout: $!");
    while(my $l=<IN2>){
      if ($l !~ /^(\S+)\t(\S+)\t.*\t *([\d.+e]+) *$/) {die("Line failed pattern: $l\n ");} # erk?
      if (!defined $lookup{$2}) {die("Could not find '$2' in lookup table");} # Must be there.
      if ($1 eq $lookup{$2} and $3>$hits{$1}) {$hits{$1}=$3;} # The best self-hits are recorded here.
    }
    close(IN2);

    print OUT map {"$_\t$hits{$_}\n"} sort keys %hits;
    #print "See $I.blastout\n";
    #exit 0;

    # Rewind the temporary file:
    truncate(OUT2,0);
    seek(OUT2,0,0);
  }
}

# #/usr/local/ncbi/bin/bl2seq -p blastn -i /tmp/bl2seq.2196.txt -j /tmp/bl2seq.2196.txt -D 1
# # BLASTN 2.2.15 [Oct-15-2006]
# # Query: AHHF254.g1
# # Fields: Query id, Subject id, % identity, alignment length, mismatches, gap openings, q. start, q. end, s. start, s. end, e-value, bit score
# AHHF254.g1	AHHF254.g1	100.00	508	0	0	367	874	367	874	0.0	 959
# AHHF254.g1	AHHF254.g1	100.00	295	0	0	41	335	41	335	5e-171	 585
# AHHF254.g1	AHHF254.g1	100.00	11	0	0	840	850	287	277	0.14	22.3
# AHHF254.g1	AHHF254.g1	100.00	11	0	0	367	377	353	343	0.14	22.3
# AHHF254.g1	AHHF254.g1	100.00	11	0	0	277	287	850	840	0.14	22.3
