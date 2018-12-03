#!/usr/bin/env python
# -*- coding:utf-8 -*-

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2
    l = merge_sort(alist[:num])
    r = merge_sort(alist[num:])
    return merge(l, r)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

li = [23, 54, 67, 12, 7, 26, 54, 21]
print(merge_sort(li))