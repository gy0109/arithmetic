#!/usr/bin/env python
# -*- coding:utf-8 -*-

def index_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

li = [23, 54, 67, 12, 7, 26, 54, 21]
index_sort(li)
print(li)