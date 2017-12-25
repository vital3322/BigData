#!/usr/bin/env python
# coding=utf-8
import sys  

# input comes from STDIN (standard input)
for line in sys.stdin:
    row = line.strip().split()
    antiNucleus = int(row[0])
    eventFile = int(row[1])
    print('%s\t%s' % (antiNucleus, eventFile))
