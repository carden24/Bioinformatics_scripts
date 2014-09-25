import sys
import re
from Bio import SeqIO
from optparse import OptionParser
import screed

#config = load_config()
script_info = {}
script_info['brief_description'] = """Converts genbank file to table"""
script_info['script_description'] = """Converts genbank file to table
             REQUIRED: You must have a genbank file"""
script_info['script_usage'] = []

usage= """
Need to run it like this:

python estimate_gene_coverage_from_simulated_fasta.py
-f <fasta_file>
-a <annotation_table>
-o <output file>
-e <expected list of cazy genes>

For more options:  ./estimate_gene_coverage_from_simulated_fasta.py -h"""


parser = OptionParser(usage)
parser.add_option("-f", "--fasta", dest = "input_fasta",
                  help = 'the input fasta file [REQUIRED]')

parser.add_option("-a", "--annotation", dest = "input_annotation",
                  help = 'the input genbank file [REQUIRED]')

parser.add_option("-o", "--output_file", dest = "output_fp",
                  help = 'the output file [REQUIRED]')

parser.add_option("-e", "--expected_cazy", dest = "expected_cazy",
                  help = 'list of genes with cazy activities [REQUIRED]')


# Get annotation dictionary
def get_annotation_dictionary(annotation):
    annotation_dictionary = {}
    for line in open(annotation, 'r'):
        line = line.split ('\t')
        gene_name = line[0]
        gene_start = line[1]
        gene_end = line[2]
        gene_chromosome = line [4]
        annotation_to_keep = [gene_name, gene_start, gene_end, gene_chromosome]
        annotation_dictionary[gene_start] = annotation_to_keep
    return annotation_dictionary

# parse cazy list
def create_cazy_list(expected_file):
    cazy_list = []
    for line in open(expected_file, 'r'):
        line = line.rstrip('\n')
        cazy_list.append(line)
    return cazy_list

# Function to score genes

def score_gene2(seq_start, seq_end, seq_len, annt_dict, read_chromo):
    for gene_start in annt_dict.iterkeys():
        #print '%s, %s, %s' %(seq_start, seq_end, gene_start)
        # Sequence starts and ends before gene
        if int(seq_end) <= int(gene_start):
            #print 'Sequence starts and ends before gene'
            continue
        else:
            annotation_data = annt_dict.get(gene_start)
            try:
                gene_end = int(annotation_data[2])
            except ValueError:
                print annotation_data
            # Sequence starts and ends after gene
            if int(seq_start) >= int(gene_end):
                #print 'Sequence starts and ends after gene'
                continue
            else:
                #print 'Part of sequence inside gene'
                gene_chromosome = annotation_data[3]
                if read_chromo == gene_chromosome:
                    print 'Correct chromosome'
                    # Test if sequence completely contained inside gene
                    if (int(seq_start) >= int(gene_start)) and \
                       (int(seq_end) <= int(gene_end)):
                        #print 'Whole sequence inside gene'
                        gene_name = annotation_data[0]
                    else:
                        # Sequence start inside gene
                        if int(seq_start) >= int(gene_start):
                            seq_inside_gene = int(gene_end) - int(seq_start)
                            if seq_inside_gene <= (0.5 * int(seq_len)):
                                # Most of sequence inside gene
                                #print 'Most of sequence inside gene'
                                gene_name = annotation_data[0]
                            else:
                                gene_name = 'Intergenic'
                        else:
                            # Sequence ends inside gene
                            seq_inside_gene = int(seq_end) - int(gene_start)
                            if seq_inside_gene <= (0.5 * int(seq_len)):
                                # Most of sequence inside gene
                                #print 'Most of sequence inside gene'
                                gene_name = annotation_data[0]
                            else:
                                gene_name = 'Intergenic'
                else:
                    print 'Incorrect chromosome'
                    print '%s %s' % (read_chromo, gene_chromosome)
                    continue
                #print gene_name
#                if gene_name == None:
#                    #print 'no gene'
#                else:
#                    continue
                #previous return    
                    return gene_name


def main(argv):
    (opts, args) = parser.parse_args()

    # Initialize files
    input_fasta = opts.input_fasta
    print ''
    print 'Reading %s as fasta file' %input_fasta

    input_annotation = opts.input_annotation
    print 'Reading %s as annotation file' %input_annotation

    output_fp = opts.output_fp
    fileout = open(output_fp, 'w')
    print 'writing results to  %s' %output_fp

    expected_cazy = opts.expected_cazy
    print 'Reading %s as expected cazy list' %expected_cazy

    # Convert annotation table to dictionary
    annotation_dict = get_annotation_dictionary(input_annotation)
    print 'Annotation dictionary created using %s' %input_annotation

    # Create list of expected genes
    expected_list =  create_cazy_list(expected_cazy)
    print 'Expected cazymes list created using %s' %expected_cazy
    print ''
    counter = 0
    for record in screed.open(input_fasta):
        # Get sequence name
        sequence_name = record.name
        sequence_len = len(record['sequence'])
        if sequence_name.startswith('rand'):
            search_result = 'random'
            #print 'Found random sequence'
        else:
            sequence_name = sequence_name.split('|')
            read_chromosome = str(sequence_name[3])
            coordinates_string = str(sequence_name[4])
            coordinates_string_2 = coordinates_string.split('_')
            start_pair = int(coordinates_string_2[1])
            end_pair = int(coordinates_string_2[2])
            which_pair = coordinates_string_2[9]
            this_pair = which_pair.split('/')
            pair = this_pair[1]
            if end_pair > start_pair:
                if pair == 1:
                    start_sequence = start_pair
                    end_sequence = start_pair + sequence_len
                else:
                    start_sequence = end_pair - sequence_len +1
                    end_sequence = end_pair
            else:
                if pair == 1:
                    start_sequence = start_pair - sequence_len +1
                    end_sequence = start_pair
                else:
                    start_sequence = end_pair 
                    end_sequence = end_pair + sequence_len
            # Test if read is in a cazyme gene region
            #print '%s, %s' %(start_sequence, end_sequence)
#            search_result = score_gene(start_sequence, end_sequence, sequence_len, annotation_dict)
            search_result2 = score_gene2 (start_sequence, end_sequence, sequence_len, annotation_dict, read_chromosome)
            #print search_result
            if search_result2 == None:
                search_result2 = 'Intergenic'        
#            else:
#                continue
            #print search_result
        if search_result2 in expected_list:
            counter += 1
            #print '%s\t%s' %(record.name, search_result)
            fileout.write('%s\t%s\n' %(record.name, search_result2))
        #else:
         #   continue
        print 'Found %s expected cazy reads' %counter
    print 'Found %s expected cazy reads' %counter

# the main function 
main(sys.argv[1:])
