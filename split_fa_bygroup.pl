#!/usr/local/bin/perl

$group_num = 10;
($fasta_file,$group_num,$normal) = @ARGV;

$seq_sum = `cat $fasta_file | grep ">" | wc -l`;
$seq_sum =~ /(\d+)/;
$seq_sum = $1;

if ($fasta_file =~ /^(.*\/)([^\/^\.]+)\.([^\/]+)$/) 
{
	$dir = $1;
	$pre = $2; 
	$post = $3;
}
elsif($fasta_file =~ /^([^\/^\.]+)\.([^\/]+)$/)
{
	$dir = "./";
	$pre = $1; 
	$post = $2;
}
else { die"the infile should is *.*\n"; }

if(defined($normal)) 
{
	$pre = "leaf"; 
	$post = "fa";
}
print "$pre.$post	$seq_sum\n";

$each = int($seq_sum/$group_num);
open(IN,$fasta_file);
$seq_num = 0;
$out_num = 0;
while(<IN>)
{
	if(/^\>/) 
	{ 
		if ($seq_num % $each == 0 && $out_num < $group_num) 
		{ 
			if($seq_num == $each) { print "$pre\_$out_num\.$post	$seq_num\n"; }
			close(OUT);
			$out_num++;
			$seq_num = 0;
			open(OUT,">$pre\_$out_num\.$post");
		}
		$seq_num++;
	}
	print OUT;
}

print "$pre\_$out_num\.$post	$seq_num\n";
close(IN);
