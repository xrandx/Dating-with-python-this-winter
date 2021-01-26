"""
请定义一个 Queue 类，基于 list 实现如下的方法：

    items = Queue()
    items.enqueue()  # 将任意对象从队尾入队
    items.dequeue()  #  使队头对象出队
    items.size()  # 返回队列的长度(int)
    items.capacity() #   返回队列的容量(int)
    items.is_full() #   队列是否已满(bool)
    items.is_empty()    #   队列是否为空 (bool)
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.rear = 0
        self.front = 0
        self.items = [None] * capacity

    def enqueue(self, item):
        if self.is_full():
            print('queue is full')
            return False
        else:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            return True

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            tmp = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return tmp

    def size(self):
        return (self.rear - self.front) % self.capacity

    def capacity(self):
        return self.capacity

    def is_full(self):
        #   用一个空间区分是否为满
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:
            return False

    def is_empty(self):
        if self.rear == self.front:
            return True
        else:
            return False

    def show(self):
        print(self.items)


if __name__ == '__main__':
    q = Queue(5)
    q.show()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(23)
    q.enqueue(10)

    q.show()

    q.dequeue()
    q.show()
    q.dequeue()
    q.show()
    q.enqueue(23)
    q.enqueue(10)
    q.show()
    q.enqueue(10)
    q.dequeue()
    q.show()

    q.dequeue()
    q.show()

    q.dequeue()
    q.show()

    q.dequeue()
    q.show()

    q.dequeue()





