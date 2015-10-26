# load some packages
from __future__ import division
try:
    import csv
    import re
    import sys
    import os
#    import types
    import argparse
    from bs4 import *
    import html5lib
    import urllib2
    
except:
     import_exception = """ Could not load some modules """
     print import_exception 
     sys.exit(3)


# a script to parce GH5 families
what_i_do = "Get taxonomic distribution"
parser = argparse.ArgumentParser(description=what_i_do)
# add arguments to the parser
parser.add_argument('-i', dest='input_file', type=str, 
                required=True, help='a selection of input files (required)', default=None)

parser.add_argument('-o', dest='output_file', type=str, nargs='?',
               required=True, help='the output file (required)', default=None)
               

def main():
    args = vars(parser.parse_args())
    input_file = args["input_file"]
    output_handle = open(args["output_file"], "w")
    file_handle = open (input_file, "r")
    # Read hmtl
    soup = BeautifulSoup(file_handle, "html5lib")
    # Create empty result dictionary
    taxa_to_keep_track = {'Cazyme':'NN', 'All':'0', 'Archaea':'0', 'Bacteria':'0', 'Eukaryota':'0', 'unclassified':'0', 'Viruses':'0'}
    
    # Find the cazyme family
    cazy_search = soup.find_all('span', {"class":"summary"})
    cazy_search2 = re.search('(\/)([A-Z0-9]+)(.)([a-z]+)', str(cazy_search))
    cazy_search3 = cazy_search2.group(0)
    cazy_search4 = cazy_search3.split('.')
    cazy = cazy_search4[0].lstrip('\/')
    # Update result dictionary
    taxa_to_keep_track['Cazyme'] = cazy
#    print taxa_to_keep_track

    # Find the taxonomic ranks with the corresponding counts
    taxa = soup.find_all("span", {"class":"choix"})
    for item in taxa:
        count_search = re.search('(\()([0-9\s]+)(\))',str(item))
        if count_search == None:
            continue
        else:
            count = count_search.group(0)
            count = count.strip('() ')
        taxonomic_rank_search = re.search('(\>)([A-Za-z]+)(\<\/a)', str(item))
        taxonomic_rank =  taxonomic_rank_search.group(0)
        taxonomic_rank = taxonomic_rank.rstrip('a').rstrip('<\/').lstrip('>')
        if taxonomic_rank in taxa_to_keep_track.keys():
            # Update results if present in the list of desired results
            taxa_to_keep_track[taxonomic_rank] = count
        else:
            continue
    output_handle.close()    
#    print taxa_to_keep_track

    with open(args["output_file"], "wb") as fileout:
        w = csv.writer(fileout)
        w.writerow(taxa_to_keep_track.keys())
        w.writerow(taxa_to_keep_track.values())

#with open('mycsvfile.csv','wb') as f:
#    w = csv.writer(f)
#    w.writerow(somedict.keys())
#    w.writerow(somedict.values())



# Call the main function
sys.exit(main())
