#!/usr/bin/env python
# -*- coding:utf-8 -*-

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap // 2
li = [23, 54, 67, 12, 7, 26, 54, 21]
shell_sort(li)
print(li)
