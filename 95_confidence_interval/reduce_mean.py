#!/usr/bin/env python
# coding=utf-8
from operator import itemgetter
import sys

current_elem = None
current_count = 0
current_sum_part = 0
elem = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    elem, sum_part, count = line.split('\t')

    # convert count (currently a string) to int
    try:
        sum_part = int(sum_part)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_elem == elem:
        current_sum_part += sum_part
        current_count += count
    else:
        if current_elem:
            # write result to STDOUT
            print '%s\t%s' % (elem, 1.0 * current_sum_part / current_count or 1.0)
        current_sum_part += sum_part
        current_count += count
        current_elem = elem

# do not forget to output the last word if needed!
if current_elem == elem:
    print '%s\t%s' % (elem, 1.0 * current_sum_part / current_count or 1.0)

