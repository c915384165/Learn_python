#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def isOdd(int_num):
    if int_num:
        if int_num % 2 == 0:
            return True
        else:
            return False


def multi(*arg):
    a = 1
    for i in arg:
        a *= i
    return a


print(multi(1, 2, 3, 2, 4, 5, 6))
