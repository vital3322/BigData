#!/usr/bin/env python
# coding=utf-8
import sys
from decimal import Decimal


for line in sys.stdin:
    line = line.strip()
    params = line.split('\t')
    if Decimal(params[2]) > Decimal(params[4]):
         print(line)
    
