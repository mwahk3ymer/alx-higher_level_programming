#!/usr/bin/python3

import sys

argv = sys.argv[1:]
num_args = len(argv)

print("Number of argument(s): {}".format(num_args), end='')

if num_args == 0:
    print(".")
else:
    print(":", end='\n')
    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
