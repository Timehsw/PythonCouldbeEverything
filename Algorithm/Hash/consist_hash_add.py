# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/8/31.
'''

from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
NEW_NODES = 101


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
new_ring = []

for n in range(NODES):
    ring.append(_hash(n))
    ring.sort()

print ring

for n in range(NEW_NODES):
    new_ring.append(_hash(n))
    new_ring.sort()
print new_ring
change = 0

for item in range(ITEMS):
    h = _hash(item)
    n = bisect_left(ring, h) % NODES
    new_n = bisect_left(new_ring, h) % NEW_NODES
    if new_n != n:
        change += 1

print("Change: %d\t(%0.2f%%)" % (change, change * 100.0 / ITEMS))