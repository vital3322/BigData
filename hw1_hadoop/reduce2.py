#!/usr/bin/env python
# coding=utf-8
import sys
from decimal import Decimal


# input comes from STDIN
lines = []
for line in sys.stdin:
    lines.append(line.strip())

means = {}
for line in lines:
    params = line.split('\t')
    if len(params) == 4 and params[3] == 'mean':
	means[int(params[1])] = Decimal(params[2])


for line in lines:
    params = line.split('\t')
    if len(params) == 4 and params[3] == 'mean':
        continue  
    print('%s\t%s' % ('\t'.join(params[1:]),means[int(params[1])]))


