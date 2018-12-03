#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
双向链表
"""

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print(' hhah ')


    def append_to_head(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node


    def append_to_tail(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = node

    def append_to_index(self, pos, item):
        if pos <= 0:
            self.append_to_head(item)
        elif pos > (self.length() -1):
            self.append_to_tail(item)
        else:
            node = Node(item)
            count = 0
            cur = self.__head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def rm(self, item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return  False

if __name__ == '__main__':
    my = SingleLinkList()
    my.append_to_head(1)   # 头部
    my.append_to_head(2)
    my.append_to_tail(3)    # 尾部
    my.append_to_index(0, 4) # 下标
    print('length: ', my.length())
    my.travel()   # 遍历
    print(my.search(2))  # 查找节点是否存在
    print(my.search(5))
    my.rm(2)   # 删除节点
    my.travel()