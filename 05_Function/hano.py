#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
著名的汉诺塔问题求解
"""

count = 0


def hano(begin, mid, end, n):
    """"""
    if isinstance(n, int):
        global count
        if n == 1:
            print("{3}:{0}->{1}, {2}".format(begin, end, n, count))
            count += 1
        else:
            hano(begin, end, mid, n-1)
            print("{3}:{0}->{1}, {2}".format(begin, end, n, count))
            count += 1
            hano(mid, begin, end, n-1)


hano('A', 'B', 'C', 3)
