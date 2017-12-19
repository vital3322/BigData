#!/usr/bin/env python
# coding=utf-8
from operator import itemgetter
import sys


# input comes from STDIN
lines = []
for line in sys.stdin:
    lines.append(line)

mean = 0
for line in lines:
    line = line.strip()
    key, value, count = line.split('\t')
    if value == 'mean':
	mean = count
	break

for line in lines:
    line = line.strip()
    key, value, count = line.split('\t')
    if value == 'mean':
	continue
    print '%s\t%s\t%s' % (value, count, mean)
