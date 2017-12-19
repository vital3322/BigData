#!/usr/bin/env python
# coding=utf-8
import sys
#mean_data = open('mean.txt').read()
#mean = mean_data.split()[1]
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    value, count = line.split('\t')
    print '%s\t%s' % ('_', value.strip(',') + '\t' + str(count))
    #print '%s\t%s' % ('_', value.strip(',') + '\t' + str(count) + '\t' + str(mean))
