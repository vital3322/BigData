#!/usr/bin/env python
# coding=utf-8
import sys
from decimal import Decimal    

# input comes from STDIN (standard input)
for line in sys.stdin:
    row = line.strip().split()
    antiNucleus = int(row[0])
    prodTime = Decimal(row[2])
    print('%s\t%s' % (antiNucleus, prodTime))
