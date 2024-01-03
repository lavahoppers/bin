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

# flag for showing all environment variables. 
parser.add_argument('-ls', '--list', action = 'store_true', default = False, 
                    dest = 'list',  
                    help = '(l)i(s)t all the environment variables')

parser.add_argument('-f', '--find', action = 'store', default = None, 
                    dest = 'find',
                    help = '(f)ind all environment variables that contain '
                    'a string', type = str)

parser.add_argument('-fs', '--find-show', action = 'store', default = None, 
                    dest = 'find_show',
                    help = '(f)ind and (s)how all environment variables that '
                    'contain a string', type = str)

args = parser.parse_args()

delimeter = ';' if sys.platform == 'win32' else ':'

# Showing the values of environment variables
for var in args.show:
    if value := os.environ.get(var):
        split = value.split(delimeter)
        _sorted = sorted(split)
        print(f'{var.upper()}:')
        for item in _sorted:
            print(f'    {item}')
    
# List all the enviornment variables    
if args.list:
    for key in os.environ.keys():
        print(key)
    
if pat := args.find:
    matched = [ k for k in os.environ.keys() if  (pat.lower() in k.lower()) ]
    for item in matched:
        print(item, end=' ')
        
if pat := args.find_show:
    matched = [ k for k in os.environ.keys() if  (pat.lower() in k.lower()) ]
    for item in matched:
        value = os.environ.get(item)
        split = value.split(delimeter)
        _sorted = sorted(split)
        print(f'{item.upper()}:')
        for item in _sorted:
            print(f'    {item}')