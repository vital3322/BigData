#!/usr/bin/env python
# coding=utf-8
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    value, count, mean = line.split('\t')
    print '%s\t%s\t%s\t%s' % ('std', value.strip(','), count, mean)
