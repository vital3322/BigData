#!/usr/bin/env python
# coding=utf-8
from operator import itemgetter
import sys

Z_95 = 1.96
mean = 0
std = 0
current_count = 0

lines = []
for line in sys.stdin:
    lines.append(line)

for line in lines:
    line = line.strip()
    key, value, count = line.split('\t')
    if value == 'mean':
	mean = float(count)
	continue
    if value == 'std':
	std = float(count)
	continue

for line in lines:
    line = line.strip()
    key, value, count = line.split('\t')
    if value in ('mean', 'std'):
	continue
    # convert count (currently a string) to int
    try:
        current_count += int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
shift = Z_95 * std / (current_count ** 0.5)
interval = '%s: (%s, %s)' % ('interval', mean - shift, mean + shift)

print interval

