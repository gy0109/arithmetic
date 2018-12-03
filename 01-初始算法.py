#!/usr/bin/env python
# -*- coding:utf-8 -*-

from timeit import Timer

def my_fn1():
    l = []
    for i in range(1000):
        l += [i]

def my_fn2():
    l = []
    for i in range(1000):
        l.append(i)

def my_fn3():
    l =[i for i in range(1000)]

def my_fn4():
    l = list(range(1000))


timer1 = Timer('my_fn1()', 'from __main__ import my_fn1')
print('concat', timer1.timeit(number=1000), 'seconds')
timer2 = Timer('my_fn2()', 'from __main__ import my_fn2')
print('append', timer2.timeit(number=1000), 'seconds')
timer3 = Timer('my_fn3()', 'from __main__ import my_fn3')
print('comprehension', timer3.timeit(number=1000), 'seconds')
timer4 = Timer('my_fn4()', 'from __main__ import my_fn4')
print('list range', timer4.timeit(number=1000), 'seconds')



x =range(2000000000)
pop_zero = Timer('x.pop(0)', 'from __main__ import x')
print('pop_zero', pop_zero.timeit(number=1000), 'seconds')
x1 =range(2000000000)
pop_end = Timer('x1.pop()', 'from __main__ import x1')
print('pop_end', pop_zero.timeit(number=1000), 'seconds')


