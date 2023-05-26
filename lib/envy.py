'''
implementation of envy

envy lets you see and modify environment variables easily
'''

import argparse
import os
import re
import sys

parser = argparse.ArgumentParser(prog = 'envy',
    description = 'envy lets you see and modify environment variables easily')

# flag for showing values
parser.add_argument('-s', action = 'store', default = [], dest = 'show',
                    help = '(s)how the values of environment variables', 
                    nargs = '*', type = str)

args = parser.parse_args()

delimeter = ';' if sys.platform == 'win32' else ':'

for var in args.show:
    if value := os.environ.get(var):
        print(var, value)
        
    
    