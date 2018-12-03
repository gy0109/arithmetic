#!/usr/bin/env python
# -*- coding:utf-8 -*-

def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [23, 54, 67, 12, 7, 23, 54, 21]
bubble_sort(li)
print(li)