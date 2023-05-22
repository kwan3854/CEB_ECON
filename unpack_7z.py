'''
Hypothetical command-line tool for searching a
collection of files for one or more text patterns.
'''
import argparse
from pyunpack import Archive

parser = argparse.ArgumentParser(description ='Unpack 7z files')

parser.add_argument('-i','--input', type=str,  help ='Packed file')
parser.add_argument('-o','--output', type=str,	 help ='output file')

args = parser.parse_args()
print('input '+args.input)
print('output '+args.output)

Archive(args.input).extractall(args.output)

print('#### Finished Unpacking the Files #######')