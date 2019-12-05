#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
著名的汉诺塔问题求解：
使用递归方法+分支+函数方式
"""
count = 0


def hano(begin, mid, end, n):
    """
     begin: 开始的柱子 （type = str)
     mid: 中间的柱子 （type=str)
     end: 最后的柱子 （type=str)
     n: 塔的层数 （type=int）
     """
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
