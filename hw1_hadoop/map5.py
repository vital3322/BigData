#!/usr/bin/env python
# coding=utf-8
import sys    

# input comes from STDIN (standard input)
for line in sys.stdin:
    row = line.strip().split()
    antiNucleus = int(row[0])
    Pt = float(row[3])
    print('%s\t%s' % (antiNucleus, Pt))
