#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
单向循环链表
"""

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item)
            cur = cur.next
        print(' hhah ')


    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head = node


    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() -1):
            self.append(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def rm(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.item == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head


    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return  False

if __name__ == '__main__':
    my = SingleLinkList()
    my.add(1)   # 头部
    my.add(2)
    my.add(3)    # 尾部
    my.insert(0, 4) # 下标
    print('length: ', my.length())
    my.travel()   # 遍历
    print(my.search(2))  # 查找节点是否存在
    print(my.search(5))
    my.rm(2)   # 删除节点
    my.travel()