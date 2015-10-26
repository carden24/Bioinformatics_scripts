# Usage python ./pkl_to_csv.py <dictionary.file> 

import pickle
import sys
import csv
import re

file_dict = open(sys.argv[1], 'rb')
basename = re.sub('[.](pkl)', '', sys.argv[1], re.I)
output_file = basename + ".csv"
fileout = csv.writer(open (output_file, 'w'))
dictionary_object = pickle.load(file_dict)

for key, value in dictionary_object.items():
   value2 = value[1]
   fileout.writerow([key, value2])

file_dict.close()
fileout.close()