#!/usr/bin/python
import sys, os, re, getopt, glob, numpy as np
import timeit
import fileinput

start = timeit.default_timer()

Usage = """
Usage:  ./CAZy_compile_post_annotation.py -d ~/GENOME/CAZyANNOTATIONS/ 

OPTIONAL ARGUMENTS:

                -d	the folder containing \"pangenome_matrix_t0.tab\" and all folders output by \"parse_pangenome_matrix.pl\"
		
		-b <V>	Enter DEBUG MODE - prints debugging information AND saves large dicitionaries in cPickle binary format for faster loading
		
		-h	prints usage

ANALYSIS ARGUMENTS:

		-e	maximum E-value : will pool all hits with > specified maximum and label them \"Above E-value\"

		-c	minimum coverage : will pool all hits with < specified minimum coverage and label them \"Below Coverage\"

		-m	pool counts based on generalize family names (i.e. AA, GH, GT... etc)	
"""

if len(sys.argv)<2:
        print Usage
        sys.exit()

# Store input and output file names
DIRECTORY=''
E_VALUE=''
COVERAGE=''
POOL=''
Debug=''
Help=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"d:e:c:b:h:m:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-d':
        DIRECTORY= a
    if o == '-e':
        E_VALUE= a
    if o == '-m':
        POOL= a
    if o == '-c':
        COVERAGE= a
    if o == '-b':
        Debug= a
    if o == '-h':
        Help = a

if Debug:
	print "You are in Debugging Mode"

FILE_Name = []
FILE_Name_SPACED_OUT = []

if DIRECTORY:
	for files in glob.glob(DIRECTORY+"/*.CAZyhits"): 
		Foo = re.sub('.CAZyhits', '', files)
		FILE_Name.append(re.sub(DIRECTORY,'',Foo))

	if Debug:
		print "I found a directory"
		print FILE_Name
else:
	for files in glob.glob("./*.CAZyhits"): 
		Foo = re.sub('.CAZyhits', '', files)
		FILE_Name.append(re.sub("./",'',Foo))
		DIRECTORY = './'
	if Debug:
		print "I used current directory"
		print FILE_Name

##ENSURE VALUE FOR E_VALUE AND COVERAGE
if not E_VALUE or not COVERAGE:
	if not E_VALUE:
		E_VALUE = 'Not Set'
	if not COVERAGE:
		COVERAGE = 'Not Set'

if Debug:
	print "Coverage set to: "+COVERAGE
	print "E-value set to: "+E_VALUE

#Open file to write to
output = open("./Compiled CAZy Output.tsv", "w")
output.write("Source\tCAZyme\tCount\tE-value cutoff: "+E_VALUE+"\tCoverage cutoff: "+COVERAGE+"\n")

if not POOL: 
	if np.size(FILE_Name)<2:
		if Debug:
			print "You processing only one file entitled: "+FILE_Name+'.CAZyhits'

		COUNT_DICT = {}
		SPACED_Name = re.sub(" ", "\ ", FILE_Name)

		with open(DIRECTORY+"/"+SPACED_Name+'.CAZyhits', "r") as f:
			next(f) #SKIPS FIRST LINE

			for line in f:
				line = line.split()
				CAZyme = line [1]
				CAZyme = re.sub(".hmm","",CAZyme)
				e_value = line[2]
				coverage= line[7]
	
				if Debug:
					print "You just wrote to file: "+CAZyme

				if E_VALUE != 'Not Set':
					if float(e_value) > float(E_VALUE):
						CAZyme = "Above E-value"				

				if COVERAGE != "Not Set":
					if float(coverage) < float(COVERAGE):
						if CAZyme != "Above E-value":
							CAZyme = "Below Coverage"
				
				if not COUNT_DICT.has_key(CAZyme):
					COUNT_DICT[CAZyme] = 0
				COUNT_DICT[CAZyme] = COUNT_DICT[CAZyme] + 1
			
		if Debug:
			print COUNT_DICT

		for key, value in COUNT_DICT.iteritems():
			output.write(FILE_Name+"\t"+key+"\t"+str(value)+"\n")


	else:
		for CURRENT_FILE in FILE_Name:
			if Debug:
				print "You are currently processing: "+CURRENT_FILE

			COUNT_DICT = {}
			SPACED_Name = re.sub(" ", "\ ", CURRENT_FILE)
	
			with open(DIRECTORY+"/"+CURRENT_FILE+'.CAZyhits', "r") as f:
				next(f) #SKIPS FIRST LINE

				for line in f:
					line = line.split()
					CAZyme = line [1]
					CAZyme = re.sub(".hmm","",CAZyme)
					e_value = line[2]
					coverage= line[7]
		
					if Debug:
						print "You just wrote to file: "+CAZyme

					if E_VALUE != 'Not Set':
						if float(e_value) > float(E_VALUE):
							CAZyme = "Above E-value"				

					if COVERAGE != "Not Set":
						if float(coverage) < float(COVERAGE):
							if CAZyme != "Above E-value":
								CAZyme = "Below Coverage"
			
					if not COUNT_DICT.has_key(CAZyme):
						COUNT_DICT[CAZyme] = 0
					COUNT_DICT[CAZyme] = COUNT_DICT[CAZyme] + 1
			
			if Debug:
				print COUNT_DICT

			for key, value in COUNT_DICT.iteritems():
				output.write(CURRENT_FILE+"\t"+key+"\t"+str(value)+"\n")
		
else: 
	if np.size(FILE_Name)<2:
		if Debug:
			print "You processing only one file entitled: "+FILE_Name+'.CAZyhits'

		COUNT_DICT = {}
		SPACED_Name = re.sub(" ", "\ ", FILE_Name)

		with open(DIRECTORY+"/"+SPACED_Name+'.CAZyhits', "r") as f:
			next(f) #SKIPS FIRST LINE

			for line in f:
				line = line.split()
				CAZyme = line [1]
				CAZyme = re.sub(".hmm","",CAZyme)
				e_value = line[2]
				coverage= line[7]
	
				if Debug:
					print "You just wrote to file: "+CAZyme

				if E_VALUE != 'Not Set':
					if float(e_value) > float(E_VALUE):
						CAZyme = "Above E-value"				

				if COVERAGE != "Not Set":
					if float(coverage) < float(COVERAGE):
						if CAZyme != "Above E-value":
							CAZyme = "Below Coverage"
			
				if not COUNT_DICT.has_key(CAZyme):
					COUNT_DICT[CAZyme] = 0
				COUNT_DICT[CAZyme] = COUNT_DICT[CAZyme] + 1
			
		if Debug:
			print COUNT_DICT

		POOL_COUNT = {}
		for key, value in COUNT_DICT.iteritems():
			if re.search("CBM", key):
				XX = 'CBM'

			elif re.search("Above E-value", key):
				XX = 'Above E-value'

			elif re.search("Below Coverage", key):
				XX = 'Below Coverage'

			else:
				XX = key[0:2]

			if not POOL_COUNT.has_key(XX):
                        	POOL_COUNT[XX] = 0
                        POOL_COUNT[XX] = POOL_COUNT[XX] + value

		if Debug:
			print POOL_COUNT

		for key, value in POOL_COUNT.iteritems():
			output.write(FILE_Name+"\t"+key+"\t"+str(value)+"\n")

	else:
		for CURRENT_FILE in FILE_Name:
			if Debug:
				print "You are currently processing: "+CURRENT_FILE

			COUNT_DICT = {}
			SPACED_Name = re.sub(" ", "\ ", CURRENT_FILE)

			with open(DIRECTORY+"/"+CURRENT_FILE+'.CAZyhits', "r") as f:
				next(f) #SKIPS FIRST LINE

				for line in f:
					line = line.split()
					CAZyme = line [1]
					CAZyme = re.sub(".hmm","",CAZyme)
					e_value = line[2]
					coverage= line[7]
		
					if Debug:
						print "You just wrote to file: "+CAZyme

					if E_VALUE != 'Not Set':
						if float(e_value) > float(E_VALUE):
							CAZyme = "Above E-value"				

					if COVERAGE != "Not Set":
						if coverage < COVERAGE:
							if CAZyme != "Above E-value":
								CAZyme = "Below Coverage"
			
					if not COUNT_DICT.has_key(CAZyme):
						COUNT_DICT[CAZyme] = 0
					COUNT_DICT[CAZyme] = COUNT_DICT[CAZyme] + 1
			
			if Debug:
				print COUNT_DICT

			POOL_COUNT = {}
			for key, value in COUNT_DICT.iteritems():
				if re.search("CBM", key):
					XX = 'CBM'

				elif re.search("Above E-value", key):
					XX = 'Above E-value'

				elif re.search("Below Coverage", key):
					XX = 'Below Coverage'
				else:
					XX = key[0:2]
	
				if not POOL_COUNT.has_key(XX):
                        		POOL_COUNT[XX] = 0
	                        POOL_COUNT[XX] = POOL_COUNT[XX] + value

			if Debug:
				print POOL_COUNT

			for key, value in POOL_COUNT.iteritems():
				output.write(CURRENT_FILE+"\t"+key+"\t"+str(value)+"\n")

output.close()

stop = timeit.default_timer()

print "This operation took " + str(stop - start) + " seconds."
