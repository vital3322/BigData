#!/usr/bin/env python
# coding=utf-8
import sys

current_elem = None
eventFile_set = None
elem = None

for line in sys.stdin:
    line = line.strip()
    params = line.split('\t')
    antiNucleus = int(params[0])
    eventFile = int(params[1])
    elem = antiNucleus
    if current_elem == elem:
	eventFile_set.add(eventFile)
    else:
        if current_elem is not None:
            print ('%s\t%s' % (str(current_elem), len(eventFile_set)))
        eventFile_set = set()
	eventFile_set.add(eventFile)
        current_elem = elem

if current_elem == elem:
    print ('%s\t%s' % (str(current_elem), len(eventFile_set)))
