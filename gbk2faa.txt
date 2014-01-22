#!/usr/bin/perl

print "\n**********************************************************";
print "\n*    gbk2faa.pl , CopyRight @ cail, Fudan University.    *";
print "\n*    Convert a file in current dir please enter 1,       *";
print "\n*    Convert all files in current dir please enter 2.    *";
print "\n**********************************************************";
print "\nPlease enter your choice (1 or 2) : ";
my $choice=<STDIN>;
print "\nGOOD LUCK!\n\n";
chop($choice);

if($choice==1){
	print "Please input the ACCESSION ID of the files : ";
	my $input=<STDIN>;
	chop($input);
	my $filename=$input.".gbk";
	my $output='';
	$output=$input.".faa";
	gbk2faa($filename,$output);
}
elsif($choice==2){
	my $dir = ".";
	opendir(DIR0, $dir) or die "Can't open $dir: $!\n";
	while (defined(my $filename = readdir(DIR0))) {
		next unless $filename =~ /\.gbk$/;
		my $output=substr($filename,0,9).".faa";
		print "$filename -> $output\n";
		gbk2faa($filename,$output);
	}
}
else{
	print "The program does not support this request. SORRY.";
}

exit;
	
sub gbk2faa{
	
	my ($origianl_file,$out_file)=@_;
	my $o=''; #organism
	my $d=''; #total sequence
	my $d1='NONE'; #db_xref:"GI
	my $d2='NONE'; #protein_id
	my $d3='NONE'; #product, protein name
	my $d4='NONE'; #amino acid sequence
	my $d4t=''; #temp of d4

	my $gbk='';
	my @GenBankFile=();
	my @draft=();

	# Get the GenBank data into an array from a file
	@GenBankFile=get_file_data($origianl_file);

	# Extract the sequence
	foreach my $line (@GenBankFile) {
		if($line =~/^FEATURES/) {
			$true=1;
		}
		if($true) {
			chop($line);
			$gbk.=$line;
			$true++;
		}
	}
	
	$gbk=~s/                     (\/)/\n$1/g;
	$true=0;
	@draft=split(/\n/,$gbk);
	
	foreach my $line (@draft){
		if($line=~/^\/product="/) {
			$line=~s/^\/product="(.*)"/$1/g;
			$line=~s/-                     /-/g;
			$line=~s/                     / /g;
			$d3=$line;
        }
        elsif($line=~/^\/organism="/) {
			$line=~s/^\/organism="(.*)"/$1/g;
			$o=$line;
        }
		elsif($line=~/^\/protein_id="/) {
			$line=~s/^\/protein_id="(.*)"/$1/g;
			$d2=$line;
        }
		elsif($line=~/^\/db_xref="GI:/) {
			$line=~s/^\/db_xref="GI:(.*)"/$1/g;
			$d1=$line;
        }
		elsif($line=~/^\/translation="/) {
			$line=~s/^\/translation="(.*)".*/$1/g;
			$line=~s/\s*//g;
			$d4t=$line;
			$d4='';
			my $i=0;
			while($i<length($d4t)) {
				$d4.=substr($d4t,$i,70)."\n";
				$i+=70;
			}
			$true++;
			if($true>0) {
					$d=$d.">cl|".$d1."|man|".$d2."| ".$d3." [".$o."]\n".$d4;
					$d1='NONE';#it is better to use CDS.
					$d2='NONE';
					$d3='NONE';
					$d4='NONE';
			}
#			print "$true\n"; #number of protein found
        }
	}

	open(FAA,">$out_file");
	print FAA $d;
	close FAA;
	return 1;
}

sub get_file_data{
	
	my ($file)=@_;
	use strict;
	use warnings;

	# Initialize variables
	my @filedata=();
	unless(open(GET_FILE_DATA,$file)) {
		print STDERR "Cannot open file \"$file\"\n\n";
		exit;
	}
	@filedata=<GET_FILE_DATA>;
	close GET_FILE_DATA;
	return @filedata;
}