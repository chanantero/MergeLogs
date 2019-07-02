import sys
import getopt
from merger import merge_logs

output_filename = 'mixed_log.txt'
prefix_1 = None
prefix_2 = None

options, remainder = getopt.getopt(sys.argv[1:], 'o:', ['output=', 
                                                         'prefix1=',
                                                         'prefix2=',
                                                         ])

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt == '--prefix1':
        prefix_1 = arg
    elif opt == '--prefix2':
        prefix_2 = arg

log_1 = remainder[0]
log_2 = remainder[1]

print("log_1 = ", log_1)
print("log_2 = ", log_2)
print("log_output = ", output_filename)
print("prefix_1 = ", prefix_1)
print("prefix_2 = ", prefix_2)

