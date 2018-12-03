#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
非递归方式实现
"""
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint -1
        return False


def binary_sort_by_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_sort_by_recursion(alist[:midpoint], item)
            else:
                return binary_sort_by_recursion(alist[midpoint+1:], item)

li = [23, 54, 67, 12, 7, 26, 54, 21]
# print(binary_search(li, 3))
# print(binary_search(li, 5))
print(binary_sort_by_recursion(li,3))
print(binary_sort_by_recursion(li, 5))