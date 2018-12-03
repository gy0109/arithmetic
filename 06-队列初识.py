#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue('hello')
    q.enqueue('word')
    q.enqueue('word')
    print(q.size())
    print(q.dequeue())
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())

