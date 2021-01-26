# -*- coding: utf-8 -*-
# @Time    : 2021/1/1818 3:36 PM
# @Author  : agrroc
# @File    : JonDoe297_py_6_1.py

# 请定义一个 Queue 类，基于 list 实现如下的方法：
# 队列只允许在后端（称为rear）进行插入操作，在前端（称为front）进行取出操作。
# 队列的容量是它能容纳元素的多少，队列的大小是元素已经占用的空间多少。
#
# queue = Queue()
# queue.enqueue()  # 将任意对象从队尾入队
# queue.dequeue()  # 使队头对象出队
# queue.size()  # 返回队列的长度(int)
# queue.capcity()  # 返回队列的容量(int)
# queue.is_full()  # 队列是否已满(bool)
# queue.is_empty()  # 队列是否为空 (bool)

class Queue():

    # 初始化队列
    def __init__(self):
        self.list = [None] * 100
        self.front = 0
        self.rear = 0
        self.size = 0

    def __len__(self):
        return len(self.list)

    # 返回队列的容量(int)
    def capcity(self):
        return self.__len__()

    # 队列是否已满(bool)
    def is_full(self):
        return (self.rear + 1) % len(self.list) == self.front

    # 队列是否为空 (bool)
    def is_empty(self):
        return self.size == 0

    # 返回队列的长度(int)
    def size(self):
        # 获取队列元素个数
        return self.size

    # 将任意对象从队尾入队
    def enqueue(self, item):
        # if self.is_full():
        #     print("is full")
        self.list[self.rear] = item
        self.rear = (self.rear + 1) % len(self.list)
        self.size += 1

    # 使队头对象出队
    def dequeue(self, item):
        result = self.list[self.front]
        self.list[self.front] = None
        self.front = (self.front + 1) % len(self.list)
        self.size -= 1

    def main(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        print('queue：size = {0} , capacity = {1}\n'.format(queue.size,
        queue.capcity()))
        print('is_empty：', queue.is_empty())
        print('is_full：', queue.is_full())
        for i in range(10):
            queue.dequeue(i)
        print('queue：size = {0} , capacity = {1}\n'.format(queue.size, queue.capcity()))
        print('is_empty：', queue.is_empty())
        print('is_full：', queue.is_full())


queue = Queue()
queue.main()
