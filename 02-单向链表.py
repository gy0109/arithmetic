#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
单项链表
"""

class SingleNode(object):
    """
    节点类型
    """
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        # 判断是否为空
        return self.__head == None

    def length(self):
        # 静态鼠标移动的次数
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历   可取多种值,,,,
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print(' hhah ')


    def append_to_head(self, item):
        node = SingleNode(item)      # 取节点
        node.next = self.__head
        self.__head = node


    def append_to_tail(self, item):
        node = SingleNode(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def append_to_index(self, pos, item):
        if pos <= 0:
            self.append_to_head(item)
        elif pos > (self.length()-1):
            self.append_to_tail(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def rm(self, item):
        cur = self.__head
        prev = None
        while cur != None:
            if cur.item == item:
                if not prev:
                    self.__head = cur.next
                else:
                    prev.next = cur.next
                break
            else:
                prev = cur
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