#!/usr/bin/python
import numpy as np
import sys, os, re, getopt
import timeit
import glob
import fileinput

start = timeit.default_timer()

Usage = '''
Usage:  
./dbCAN_HMM_Genomes.py -c <directory_containing_dbCAN_files> [required] -e <specify_file_extension> [required] -f <input_format> [optional] -d <directory_containing_fasta_input> [optional]

Example:
./dbCAN_HMM_Genomes.py -c ~/CAZy/ -e .gbk -d ~/Genomes/Assembled/Fasta/ -f genbank

DEPENDENCIES: 	i)EMBOSS (v. 6.6.0 or any version contianing \"transeq\") - Must be in PATH
		ii) dbCAN files: dbCAN-fam-HMMs.txt, hmmscan-parser.sh & all.hmm.ps.len. (Note: one must have run \"hmmpress dbCAN-fam-HMMs.txt\" to format db in advance of this script)
		(FOR THE MOHN LAB: These files are available in z:/data/CAZY_dbCAN)
		iii) HMMR v.3.0 - Must be in PATH

REQUIRED ARGUMENTS:
		-c	the folder containing the script and HMMer database downloaded from http://csbl.bmb.uga.edu/dbCAN/download.php
	
		-e	the file extension of the input files (i.e. .txt, .fna, .faa, .gbk, .embl etc.)

		-d 	input directory (the directory containing your sequence data)

		-o	output directory

OPTIONAL ARGUEMENTS:

		-f	specify what format the sequence input is in. Options: faa, gff, gff2, embl, genbank, ddbj, refseqp, pir, swissprot, dasgff.
			(not specified will assume .fna)

		-h 	usage

UTILITY:
The script translates the NUCLEIC ACID sequence in all 6 reading frames, passes this information to dbCAN's HMM predictor for CAZymes and returns your output.
'''

if len(sys.argv)<2:
	print Usage
	sys.exit(2)

# Store input and output file names
PATH=''
CAZy=''
Format=''
Extension=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"d:c:f:h:e:o:")
 
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-d':
        PATH= a
    if o == '-c':
        CAZy =a
    if o == '-f':
        Format= a
    else:
	Format = "fasta"
    if o == '-h':
        print Usage
    if o == '-o':
        OUTPUT= a
    if o == '-e':
        Extension= a

genome_list = []

if PATH:
	for files in os.listdir(PATH):
		if re.search(r'.+'+Extension,files):
			files = re.sub(" ","\ ",files)
			genome_list.append(files)

else:
	for files in os.listdir("."):
		if re.search(r'.+'+Extension,files):
			files = re.sub(" ","\ ",files)
			genome_list.append(files)

if len(OUTPUT)>0:
        if os.path.exists('./' + OUTPUT):
                print "\nOutput Folder Exists - Caution: Files May Be Re-Written"
        else:
                os.mkdir(OUTPUT)
else:
        print Usage
        sys.exit(2)

if len(PATH)<0:
        print Usage
        sys.exit(2)

print 'The following genomes will be annotated:\n'

for n in genome_list:
	print "- "+n
print "\n"

HEADER = "Query Sequence_Reading Frame"+"\t"+"CAZy HMM Hit"+"\t"+"E-value"+"\t"+"HMM Sequence Start"+"\t"+"HMM Sequence End"+"\t"+"Query Sequence (Yours) Start"+"\t"+"Query Sequence End"+"\t"+"Percent Coverage"

os.system(' '.join([
	"cp",
	CAZy+"hmmscan-parser.sh",
	"./"
]))

os.system(' '.join([
	"cp",
	CAZy+"all.hmm.ps.len",
	"./"
]))

if Format == "faa" or Extension == ".faa":
	for n in genome_list:
		os.system(' '.join([
			"hmmscan",
			CAZy+"dbCAN-fam-HMMs.txt",
			PATH+"/"+n+" > ./temp.out"
			]))
	
		os.system(' '.join([
			"sh",
			"hmmscan-parser.sh ./temp.out >",
			OUTPUT+"/"+re.sub(Extension, '', n)+".temp"
			]))

		##ADD HEADER INFO	
		TouchUp = open(OUTPUT+"/"+re.sub(Extension, '', n)+".CAZyhits", "w")
		TouchUp.write(HEADER+"\n")

		##FILL IN LINES FROM HMM SCAN OUTPUT	
		for lines in open(OUTPUT+"/"+re.sub(Extension, '', n)+".temp", "r"):
			TouchUp.write(lines)

		TouchUp.close()

		print OUTPUT+"/"+re.sub(Extension, '', n)+".CAZyhits"+" Has Been Created"

		os.system("rm "+OUTPUT+"/"+re.sub(Extension, '', n)+".temp")	#Clean up

else:
	for n in genome_list:
		os.system(' '.join([
			"transeq",
			PATH+"/"+n,				#Open file from PATH
			"./"+re.sub(Extension, '', n)+".faa",	#Output as .faa
			"-frame 6",
			"-sformat",
			Format
		]))

		os.system(' '.join([
			"hmmscan",
			CAZy+"dbCAN-fam-HMMs.txt",
			"./"+re.sub(Extension, '', n)+".faa > ./temp.out"
			]))
	
		os.system(' '.join([
			"sh",
			"hmmscan-parser.sh ./temp.out >",
			OUTPUT+"/"+re.sub(Extension, '', n)+".CAZyhits"
			]))

		##ADD HEADER INFO	
		TouchUp = open(OUTPUT+"/"+re.sub(Extension, '', n)+".CAZyhits", "w")
		TouchUp.write(HEADER+"\n")

		##FILL IN LINES FROM HMM SCAN OUTPUT	
		for lines in open(OUTPUT+"/"+re.sub(Extension, '', n)+".temp", "r"):
			TouchUp.write(lines)

		TouchUp.close()

		print OUTPUT+"/"+re.sub(Extension, '', n)+".CAZyhits"+" Has Been Created"

		os.system("rm "+OUTPUT+"/"+re.sub(Extension, '', n)+".temp")	#Clean up
		os.system("rm "+"./"+re.sub(Extension, '', n)+".faa")	#Clean up the .faa

os.system("rm temp.out")
os.system("rm hmmscan-parser.sh")
os.system("rm all.hmm.ps.len")

stop = timeit.default_timer()

print "This operation took " + str(stop - start) + " seconds.\n"

print "Annotations files ending in \".CAZyhits\" have been created in \""+OUTPUT+"\" directory.\n"

