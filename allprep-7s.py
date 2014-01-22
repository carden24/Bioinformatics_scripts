#! /usr/bin/env python
import os, sys, math
#Meric Lieberman
#UCD Genome Center

#This version of allprep uses a sliding window approach to trimming
#it uses a window of 5 to check that average quality for that window
#does not drop below 20, new min length is 35


#Note: Naming convention must be used as specified, 
#all sequence files must be in illumina 1.5+ format
#to be correctly converted to sanger fastq

#use: allprep.py barcode_file.txt [a] [t] [s] [u]
#[a] runall
#[t] output thrown out
#[s] single ended
#[u] do not use T's in barcode
#requires a barcode file with name "prefix"-barcodes
#in the barcodes file is a line for each lane, tab separated 
#in the form: lanenum<Tab>barcode1-libNum1<Tab>barcode2-libNum2<tab>...<Tab>barcodeLast-LibNumLast<EOL>
#sample lane string:
#1\tAACCC-1\tCCATC-6\tGATGT-11\tGTGAG-16'

#Flags for run all tests, single ended, 'T's or not added to barcode
#and throw out rejects to a file
runall = 0
sin = 0
ts = 0
th = 0
if 'a' in sys.argv or 'A' in sys.argv or "all" in sys.argv or "runall" in sys.argv:
   runall = 10
if 't' in sys.argv or 'T' in sys.argv:
   th = 1
if 's' in sys.argv or 'S' in sys.argv:
   sin = 1
if 'u' in sys.argv or 'U' in sys.argv:
   ts = 1
   
#reverse complement
def comp(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'R': 'R', 'Y': 'Y', 'S': 'S', 'W': 'W', 'M': 'M', 'K': 'K'}
    complseq = [complement[base] for base in seq]
    return complseq

def rev(seq):
    seq = list(seq)
    seq.reverse()
    return ''.join(comp(seq))

#Adapter to look for
solAd1 = "AGATCGGAAG"
solB = "AGATCGGAAGAGC"

#counter for progress, ns is for remove 'N'
counter = 0
ns = 1
#get file prefix
prefix = sys.argv[1].split("-barcode")[0]
 
def run(lane):
   #libs hold open file handlers for each barcode, is a dictionary of barcode to file
   #codes is the barcodes for the given lane
   counter = 0
   libs = {}

   codes = []
   if ts == 0:
      codes = map(lambda x:rev(str.upper(x.split('-')[0]))+'T',lane.split('\t')[1:])
   else:
      codes = map(lambda x:rev(str.upper(x.split('-')[0])),lane.split('\t')[1:])
   #get barcode length
   bar = len(codes[0])
   #open a output file for each library
   for x in map(lambda x:x.split('-'),lane.split('\t')[1:]):
      libs[str.upper(x[0])]=open("lib"+x[1]+".fq",'w')
   
   print codes
   #print libs   
   #open paired file
   f = open(prefix+'-'+lane.split('\t')[0]+'-1.txt')
   r = open(prefix+'-'+lane.split('\t')[0]+'-2.txt')
   #if specified open output file
   if th == 1:
      out = open("lane_"+lane.split('\t')[0]+"_rem.txt",'w')
   count = 0
   #get file size
   for x in f:
      count+=1  
   f.seek(0)
   
   #assume fastq format, get 4 lines at a time
   for j in range(count/4):
      #output-status
      if j % 100000 == 8:
         print("Lane: "+lane.split('\t')[0]+"   Done: "+str(int(100*float(j)/(float(count)/4))) + '%   #Cut: '+str(counter))
      #open everything and convert to fatsq format 
      test = 0      
      name = f.readline()
      seq = f.readline()
      sname = f.readline()
      sname = "+\n"
      qualt = f.readline()
      qual = "".join(map((lambda x: chr(ord(x)-31)),qualt[:-1]))+'\n'
      sum1 = 0
      name2 = r.readline()
      seq2 = r.readline()
      sname2 = r.readline()
      sname2 = "+\n"
      qual2t = r.readline()
      qual2 = "".join(map((lambda x: chr(ord(x)-31)),qual2t[:-1]))+'\n'
      sum2 = 0
      #trim barcode and mae sure paired ends match
      if test <= runall:
         barF = seq[:bar]
         seq = seq[bar:]
         qual = qual[bar:]
         barR = seq2[:bar]
         seq2 = seq2[bar:]
         qual2 = qual2[bar:]
         name = name[:-1]+"_"+barF+'\n'
         name2 = name2[:-1]+"_"+barR+'\n'

         #barcodes must be equal and in the accepted list
         if barF != barR:
            test = 1
            sname = sname[:-1]+'\tMB\n'       
         if barF not in codes:
            #print barF,codes
            test = 2 
            sname = sname[:-1]+'\tB\n'
      # no 'N's
      if ns == 1:
         if 'N' in seq:
            test = 3 
            sname = sname[:-1]+'\tN\n'
         if 'N' in seq2:
            test = 3  
            sname2 = sname2[:-1]+'\tN\n'    
   
      #check for main type of adapter contamination and trim as needed
      if test <= runall:
         if rev(barF[:-1])+solB in seq:
            t1 = seq[:seq.index(rev(barF[:-1])+solB)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'
         if rev(barR[:-1])+solB in seq2:
            t2 = seq2[:seq2.index(rev(barR[:-1])+solB)]
            l2 = len(t2)          
            seq2 = t2+'\n'
            qual2 = qual2[:l2]+'\n'         
      #check for secondary adapter contam, trim as needed
      if test <= runall:
         if solAd1 in seq:
            t1 = seq[:seq.index(solAd1)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'         
         #if single == 0:
         if solAd1 in seq2:
            t2 = seq2[:seq2.index(solAd1)]
            l2 = len(t2)          
            seq2 = t2+'\n'
            qual2 = qual2[:l2]+'\n'  
            
      #calculate avg quality and trim if lower then threshold (20)
      if test <= runall:
         quals = map(lambda x: ord(x)-33, qual[:-1])
         for x in range(len(quals)-4):
            cut = quals[x:x+5]
            ave = float(sum(cut))/5.0
            if ave < 20.0:
               qual = qual[:x]+'\n'
               seq = seq[:x]+'\n'
               break
         quals2 = map(lambda x: ord(x)-33, qual2[:-1])
         for x in range(len(quals2)-4):
            cut2 = quals2[x:x+5]
            ave2 = float(sum(cut2))/5.0
            if ave2 < 20.0:
               qual2 = qual2[:x]+'\n'
               seq2 = seq2[:x]+'\n'
               break
#         for x in range(len(qual[:-1])):
#            print ord(qual[x])-33		     
#            if ord(qual[x])-33 < 20:
#         	  qual = qual[0:x] + '\n'
#         	  seq = seq[0:x] + '\n'
#         	  break		
#            sum1+= ord(qual[x])-33
#         for x in range(len(qual2[:-1])):
#         	if ord(qual2[x])-33 < 20:
#         		qual2 = qual2[0:x] + '\n'
#         		seq2 = seq2[0:x] + '\n'
#         		break
#         	sum2+= ord(qual2[x])-33

         
         	

      
      #check that chopped length is not too small
      if len(seq) < 36 or len(qual) < 36:
         test = 4
         sname = sname[:-1]+'\tL\n'  
      if len(seq2)< 36 or len(qual2) < 36:
         test = 4
         sname2 = sname2[:-1]+'\tL\n'  
         
      #th is to output thrown out sequences
      if test == 0:
         #using the dictionary, lookup the file handler using barcode and write out
         if ts == 0:
            libs[rev(barF[:-1])].write(name+seq+sname+qual+name2+seq2+sname2+qual2)		   
         else:
            libs[rev(barF)].write(name+seq+sname+qual+name2+seq2+sname2+qual2)
      else:
         counter+=1
         if th == 1:
            out.write(name+seq+sname+qual+name2+seq2+sname2+qual2)	
   f.close()
   r.close()
   #close all lib files
   if th ==1:
      out.close()
   for f in libs:
      libs[f].close()

def run1(lane):
   #libs hold open file handlers for each barcode, is a dictionary of barcode to file
   #codes is the barcodes for the given lane
   #beginning is same as above
   counter = 0
   libs = {}

   codes = []
   if ts == 0:
      codes = map(lambda x:rev(str.upper(x.split('-')[0]))+'T',lane.split('\t')[1:])
   else:
      codes = map(lambda x:rev(str.upper(x.split('-')[0])),lane.split('\t')[1:])
   #print "HI2", codes
   bar = len(codes[0])
   for x in map(lambda x:x.split('-'),lane.split('\t')[1:]):
      libs[str.upper(x[0])]=open("lib"+x[1]+".fq",'w')

   print codes
   #print libs   
   #open single file and output file
   f = open(prefix+'-'+lane.split('\t')[0]+'.txt')
   if th == 1:
      out = open("lane_"+lane.split('\t')[0]+"_rem.txt",'w')
   count = 0
   #count file size
   for x in f:
      count+=1  
   f.seek(0)
   #for every 4 lines in a fastq file
   for j in range(count/4):
      if j % 100000 == 8:
         print("Lane: "+lane.split('\t')[0]+"   Done: "+str(int(100*float(j)/(float(count)/4))) + '%   #Cut: '+str(counter))
      #open everything and convert to fatsq format 
      test = 0      
      name = f.readline()
      seq = f.readline()
      sname = f.readline()
      sname = "+\n"
      qualt = f.readline()
      qual = "".join(map((lambda x: chr(ord(x)-31)),qualt[:-1]))+'\n'
      #sum = 0
   
      #trim barcode and mae sure paired ends match
      if test <= runall:
         barF = seq[:bar]
         seq = seq[bar:]
         qual = qual[bar:]
         name = name[:-1]+"_"+barF+'\n'
  
         #barcode must be accepted
         if barF not in codes:
            #print barF,codes
            test = 2 
            sname = sname[:-1]+'\tB\n'
      #no 'N's
      if ns == 1:
         if 'N' in seq:
            test = 3 
            sname = sname[:-1]+'\tN\n'

      #check for main type of adapter contamination and trim as needed
      if test <= runall:
         if rev(barF[:-1])+solB in seq:
            t1 = seq[:seq.index(rev(barF[:-1])+solB)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'
      
      #check for secondary adapter contam, trim as needed
      if test <= runall:
         if solAd1 in seq:
            t1 = seq[:seq.index(solAd1)]
            l1 = len(t1)          
            seq = t1+'\n'
            qual = qual[:l1]+'\n'         
      #check average quality of read and trim if needed
      if test <= runall:
         quals = map(lambda x: ord(x)-33, qual[:-1])
         for x in range(len(quals)-4):
            cut = quals[x:x+5]
            ave = float(sum(cut))/5.0
            if ave < 20.0:
               qual = qual[:x]+'\n'
               seq = seq[:x]+'\n'
               break
			

      #check that chopped length is not too small
      if len(seq) < 36 or len(qual) < 36:
         test = 4
         sname = sname[:-1]+'\tL\n'  

      #th is to output thrown out sequences
      if test == 0:
         #using the dictionary, lookup the file handler using barcode and write out
         if ts == 0:
            libs[rev(barF[:-1])].write(name+seq+sname+qual)
         else:
            libs[rev(barF)].write(name+seq+sname+qual)		   
      else:
         counter+=1
         if th == 1:
            out.write(name+seq+sname+qual)	
   #close all files
   f.close()
   if th == 1:
      out.close()
   for f in libs:
      libs[f].close()


#read in the barcode file
f = open(sys.argv[1])
bars = []
#bars[] will have one line with all relevant infor per line as specified
for x in f:
   bars.append(x[:-1])
f.close()

for lane in bars:
   if sin == 0:
      run(lane)
   else:
      run1(lane)







