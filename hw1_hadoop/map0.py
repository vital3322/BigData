#!/usr/bin/env python
# coding=utf-8
import sys
from decimal import Decimal    

# input comes from STDIN (standard input)
for line in sys.stdin:
    row = line.strip('').split()
    antiNucleus = int(row[0].strip(','))
    eventFile = int(row[1].strip(','))
    prodTime = Decimal(row[10].strip(','))
    Pt = float(row[11].strip(','))
    print('%s\t%s\t%s\t%s' % (antiNucleus, eventFile, prodTime, Pt))
