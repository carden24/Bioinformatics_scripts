import sys
import Bio
from Bio import SeqIO

filein=open(sys.argv[1],'r')
#print 'Reading ', sys.argv[1]

total_counter=0
onek_counter=0
twok_counter=0
fivek_counter=0
tenk_counter=0
twentyfivek_counter=0
fiftyk_counter=0
hundredk_counter=0
twofiftyk_counter=0
fivehundredk_counter=0

for seq_record in SeqIO.parse(filein, format="fasta"):
   len_seq=len(seq_record.seq)
   total_counter=total_counter+1
   if len_seq >= 1000:
      onek_counter=onek_counter + 1
      if len_seq >= 2500:
         twok_counter=twok_counter + 1
         if len_seq >= 5000:
            fivek_counter=fivek_counter + 1
            if len_seq >= 10000:
               tenk_counter=tenk_counter + 1
               if len_seq >= 25000:
                  twentyfivek_counter=twentyfivek_counter + 1
                  if len_seq >= 50000:
                     fiftyk_counter=fiftyk_counter + 1
                     if len_seq >= 100000:
                        hundredk_counter=hundredk_counter + 1
                        if len_seq >=250000:
                           twofiftyk_counter=twofiftyk_counter + 1
                           if len_seq >= 500000:
                              fivehundredk_counter=fivehundredk_counter + 1
                           else:
                              continue
                     else:
                        continue
                  else:
                     continue
               else:
                  continue
            else:
               continue
         else:
            continue
      else:
         continue
   else:
      continue


print 'Stats for :\t' ,sys.argv[1]
print 'Contigs:\t' , total_counter
print '>= 1kb:\t' , onek_counter
print '>= 2.5kb:\t' , twok_counter
print '>= 5kb:\t' , fivek_counter
print '>= 10kb:\t' , tenk_counter
print '>= 25kb:\t' , twentyfivek_counter
print '>= 50kb:\t' , fiftyk_counter
print '>= 100kb:\t' , hundredk_counter
print '>= 250kb:\t' , twofiftyk_counter
print '>= 500kb:\t' , fivehundredk_counter
