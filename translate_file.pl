#!/usr/bin/perl -w
use strict;

if (@ARGV==0){die("Usage: $0 inputfile outputfile

  This program will translate the given nucleotide fasta file sequences
  into a amino acid fasta file.
");
}

my $GCODE=11;

# Load up the codon table:
my $table=join("",grep {!m/^--/} <DATA>);
$table=~s/.*::= {\n {\n//s;
$table=~s/\n }\n}$//;
my @gcode=grep {/ id $GCODE ,/} split(/ },\n {\n/,$table);
if (!defined $gcode[0]) {die("Genetic code $GCODE not found in NCBI table\n");}
my ($nuc,$stn,$b1,$b2,$b3)=$gcode[0]=~m/ncbieaa  "([^"]{64})",.*sncbieaa "([^"]{64})".*-- Base1  ([ACTG]{64}).*-- Base2  ([ACTG]{64}).*-- Base3  ([ACTG]{64})/s;
my %codons=map {substr($b1,$_,1).substr($b2,$_,1).substr($b3,$_,1)=>substr($nuc,$_,1)} 0..63;   # Codon table
#my %stcodon=map {substr($b1,$_,1).substr($b2,$_,1).substr($b3,$_,1)=>substr($stn,$_,1)} 0..63;  # Start codons (not needed in this program)
# Free up space:
$table=undef;
@gcode=();

my $INFILE=$ARGV[0];
if (!-e $INFILE) {die("$INFILE doesn't exist!\n");}
if (!-r $INFILE) {die("$INFILE isn't readable!\n");}
if (!-f $INFILE) {die("$INFILE isn't a file!\n");}
open(IN,"<$INFILE") or die("Couldn't open $INFILE\n");

my $OUTFILE=$ARGV[1];
open(OUT,">$OUTFILE") or die("Couldn't open $OUTFILE\n");

my $id;
my $seq;
while(my $line=<IN>) {
  if ($line=~ m/^>/) { process($id,$seq); $id=$line; $seq=""; next;}
  $seq=$seq . $line;
}
process($id,$seq);
close(IN);
close(OUT);
exit 0;

sub process {
  my ($ID,$SEQ)=@_;
  if (!defined $ID) {return;}
  chomp($ID);
  $ID=~s/ .*//;
  $SEQ=uc($SEQ);
  $SEQ=~s/\n//gs;
  print OUT "${ID}_frame1\n";
  print OUT translate($SEQ,"")."\n";
  print OUT "${ID}_frame2\n";
  print OUT translate(substr($SEQ,1),"")."\n";
  print OUT "${ID}_frame3\n";
  print OUT translate(substr($SEQ,2),"")."\n";
  print OUT "${ID}_frame-1\n";
  print OUT translate(revcomp($SEQ),"")."\n";
  print OUT "${ID}_frame-2\n";
  print OUT translate(substr(revcomp($SEQ),1),"")."\n";
  print OUT "${ID}_frame-3\n";
  print OUT translate(substr(revcomp($SEQ),2),"")."\n";
}

# Translate a dna sequence into amino acids:
sub translate {  # Input: dna and codon table, Output: protein
  my ($in,$sname)=@_;
  my $l=length($in);
#  if ($l%3!=0) {die("$sname: dna sequence of length $l: $in ");}
  my @c;
  while(defined $in and $in ne "") {
    push @c,substr($in,0,3);
    if (length($in)<3) {last;}
    $in=substr($in,3);
  }
#  if ($in ne "") {warn("$sname had $in left over\n");}
  my @aa=grep {defined} @codons{@c};  # Slice!
  #if (grep {!defined} @aa) {die("$sname: Unknown codon in $_[1]: ");}
  return join("",@aa);
}

# Reverse complement a dna sequence
sub revcomp {
  my $out=reverse($_[0]);
  $out=~y/atcgATCG/tagcTAGC/;
  return $out;
}


exit 0;

__DATA__
--**************************************************************************
--  This is the NCBI genetic code table
--  Initial base data set from Andrzej Elzanowski while at PIR International
--  Addition of Eubacterial and Alternative Yeast by J.Ostell at NCBI
--  Base 1-3 of each codon have been added as comments to facilitate
--    readability at the suggestion of Peter Rice, EMBL
--  Later additions by Taxonomy Group staff at NCBI
--
--  Version 3.9
--     Code 14 differs from code 9 only by translating UAA to Tyr rather than
--     STOP.  A recent study (Telford et al, 2000) has found no evidence that
--     the codon UAA codes for Tyr in the flatworms, but other opinions exist.
--     There are very few GenBank records that are translated with code 14,
--     but a test translation shows that retranslating these records with code
--     9 can cause premature terminations.  Therefore, GenBank will maintain
--     code 14 until further information becomes available.
--
--  Version 3.8
--     Added GTG start to Echinoderm mitochondrial code, code 9
--
--  Version 3.7
--     Added code 23 Thraustochytrium mitochondrial code
--        formerly OGMP code 93
--        submitted by Gertraude Berger, Ph.D.
--
--  Version 3.6
--     Added code 22 TAG-Leu, TCA-stop
--        found in mitochondrial DNA of Scenedesmus obliquus
--        submitted by Gertraude Berger, Ph.D.
--        Organelle Genome Megasequencing Program, Univ Montreal
--
--  Version 3.5
--     Added code 21, Trematode Mitochondrial
--       (as deduced from: Garey & Wolstenholme,1989; Ohama et al, 1990)
--     Added code 16, Chlorophycean Mitochondrial
--       (TAG can translated to Leucine instaed to STOP in chlorophyceans
--        and fungi)
--
--  Version 3.4
--     Added CTG,TTG as allowed alternate start codons in Standard code.
--        Prats et al. 1989, Hann et al. 1992
--
--  Version 3.3 - 10/13/95
--     Added alternate intiation codon ATC to code 5
--        based on complete mitochondrial genome of honeybee
--        Crozier and Crozier (1993)
--
--  Version 3.2 - 6/24/95
--  Code       Comments
--   10        Alternative Ciliate Macronuclear renamed to Euplotid Macro...
--   15        Bleharisma Macro.. code added
--    5        Invertebrate Mito.. GTG allowed as alternate initiator
--   11        Eubacterial renamed to Bacterial as most alternate starts
--               have been found in Achea
--
--
--  Version 3.1 - 1995
--  Updated as per Andrzej Elzanowski at NCBI
--     Complete documentation in NCBI toolkit documentation
--  Note: 2 genetic codes have been deleted
--
--   Old id   Use id     - Notes
--
--   id 7      id 4      - Kinetoplast code now merged in code id 4
--   id 8      id 1      - all plant chloroplast differences due to RNA edit
--
--*************************************************************************

Genetic-code-table ::= {
 {
  name "Standard" ,
  name "SGC0" ,
  id 1 ,
  ncbieaa  "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "---M---------------M---------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Vertebrate Mitochondrial" ,
  name "SGC1" ,
  id 2 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG",
  sncbieaa "--------------------------------MMMM---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Yeast Mitochondrial" ,
  name "SGC2" ,
  id 3 ,
  ncbieaa  "FFLLSSSSYY**CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "----------------------------------MM----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
    name "Mold Mitochondrial; Protozoan Mitochondrial; Coelenterate
 Mitochondrial; Mycoplasma; Spiroplasma" ,
  name "SGC3" ,
  id 4 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "--MM---------------M------------MMMM---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Invertebrate Mitochondrial" ,
  name "SGC4" ,
  id 5 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSSSVVVVAAAADDEEGGGG",
  sncbieaa "---M----------------------------MMMM---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Ciliate Nuclear; Dasycladacean Nuclear; Hexamita Nuclear" ,
  name "SGC5" ,
  id 6 ,
  ncbieaa  "FFLLSSSSYYQQCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Echinoderm Mitochondrial; Flatworm Mitochondrial" ,
  name "SGC8" ,
  id 9 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Euplotid Nuclear" ,
  name "SGC9" ,
  id 10 ,
  ncbieaa  "FFLLSSSSYY**CCCWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Bacterial, Archaeal and Plant Plastid" ,
  id 11 ,
  ncbieaa  "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "---M---------------M------------MMMM---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Alternative Yeast Nuclear" ,
  id 12 ,
  ncbieaa  "FFLLSSSSYY**CC*WLLLSPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-------------------M---------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Ascidian Mitochondrial" ,
  id 13 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSGGVVVVAAAADDEEGGGG",
  sncbieaa "---M------------------------------MM---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 },
 {
  name "Alternative Flatworm Mitochondrial" ,
  id 14 ,
  ncbieaa  "FFLLSSSSYYY*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 } ,
 {
  name "Blepharisma Macronuclear" ,
  id 15 ,
  ncbieaa  "FFLLSSSSYY*QCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 } ,
 {
  name "Chlorophycean Mitochondrial" ,
  id 16 ,
  ncbieaa  "FFLLSSSSYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 } ,
 {
  name "Trematode Mitochondrial" ,
  id 21 ,
  ncbieaa  "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNNKSSSSVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 } ,
 {
  name "Scenedesmus obliquus Mitochondrial" ,
  id 22 ,
  ncbieaa  "FFLLSS*SYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "-----------------------------------M----------------------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 } ,
 {
  name "Thraustochytrium Mitochondrial" ,
  id 23 ,
  ncbieaa  "FF*LSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG",
  sncbieaa "--------------------------------M--M---------------M------------"
  -- Base1  TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  -- Base2  TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  -- Base3  TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
 }
}
