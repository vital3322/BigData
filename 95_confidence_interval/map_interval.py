#!/usr/bin/env python
# coding=utf-8
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    param, value = line.split('\t')
    print '%s\t%s\t%s' % ('_', param, value)
