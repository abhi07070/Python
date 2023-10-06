# python 29acceptAgruFromCMD.py

# import sys
# name = sys.argv[1]

# print("hello " + name)

import argparse 

parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)

parser.add_argument('-c','--color',metavar='color',
required=True,help='The color to search for')

args = parser.parse_args()

print(args.color)
