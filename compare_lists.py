import sys
from optparse import OptionParser

script_info = {}
script_info['brief_description'] = """Compares two lists"""
script_info['script_description'] = """Compares two lists
             REQUIRED: You must have two lists"""
script_info['script_usage'] = []

usage= """
Need to run it like this:

compare_lists.py
-1 <list 1>
-2 <list2>
-o <output file>
"""


parser = OptionParser(usage)
parser.add_option("-1", "--list1", dest = "list_one",
                  help = 'first list file [REQUIRED]')

parser.add_option("-2", "--list2", dest = "list_two",
                  help = 'second list file [REQUIRED]')

parser.add_option("-o", "--output_file", dest = "output_fp",
                   help = 'the output file [REQUIRED]')


def create_list(list_file):
    final_list = []
    for line in open(list_file, 'r'):
        line = line.rstrip('\n')
        line1 = line.split('\t')
        line2 = line1[0]
        final_list.append(line2)
    final_set = set(final_list)
    return final_set


def main(argv):
    (opts, args) = parser.parse_args()

    # Initialize files
    list_one = opts.list_one
    list_two = opts.list_two

    print ''
    print 'Comparing %s and %s' %(list_one, list_two)

    output_fp = opts.output_fp
    fileout = open(output_fp, 'w')
    print 'writing results to  %s' %output_fp

    set_one = create_list(list_one)
    set_two = create_list(list_two)
    one_and_two = set_one & set_two
    one_not_two = set_one - set_two
    two_not_one = set_two - set_one

    #print '%s names found in %s' %(len(set_one), list_one)
    #print '%s names found in %s' %(len(set_two), list_two)
    #print '%s found only in %s' %(len(one_not_two), list_one)
    #print '%s found only in %s' %(len(two_not_one), list_two)
    #print '%s found in common' %(len(one_and_two))
    print '%s, %s, %s, %s, %s, %s, %s\n' %(list_one, list_two, len(set_one), len(set_two), len(one_not_two), len(two_not_one), len(one_and_two))
    fileout.write('%s, %s, %s, %s, %s, %s, %s\n' %(list_one, list_two, len(set_one), len(set_two), len(one_not_two), len(two_not_one), len(one_and_two)))
    fileout.close()

#    fileout.write('%s\t%s\n' %(record.name, search_result))

# the main function 
main(sys.argv[1:])
