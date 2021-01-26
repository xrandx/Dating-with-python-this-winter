#-*- codeing = utf-8 -*-
#@Time : 1/16/21 10:36 PM
#@Author : 苏苏
#@File : 第六课作业.py
#@Software : PyCharm


'''
请定义一个 Queue 类，基于 list 实现如下的方法：

    queue = Queue()
    queue.enqueue()  # 将任意对象从队尾入队
    queue.dequeue()  #  使队头对象出队
    queue.size()  # 返回队列的长度(int)
    queue.capcity() #   返回队列的容量(int)
    queue.is_full() #   队列是否已满(bool)
    queue.is_empty()    #   队列是否为空 (bool)
'''

class Queue():
    def __init__(self,capcity):
        self.capcity = capcity
        self.rear = -1
        self.front = -1
        self.queue = []

    def enqueue(self,item):
        if self.is_full():
            print('queue is full')
            return
        self.queue.append(item)
        return

    def dequeue(self,item):
        if self.is_empty():
            print('queue is empty')
            return
        self.queue.pop
        return

    def is_full(self):
        return  self.rear - self.front == self.capcity

    def is_empty(self):
        return self.rear == self.front

    def size(self):
        return len.queue









