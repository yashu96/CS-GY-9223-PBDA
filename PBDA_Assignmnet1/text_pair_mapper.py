#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import string
import sys

def read_input(file):
    for line in file:
        for word in line:
            x= word.format(u"\u263a")
            if x in string.punctuation:
                line=line.replace(x," ")
            else:
                line=line.replace(x,x.lower())
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for i in range(len(words)):
            print ('%s\t%s' % (words[i:i+2],1))

if __name__ == "__main__":
    main()
