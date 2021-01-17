#-*- codeing = utf-8 -*-
#@Time : 2021-01-11 20:26
#@Author : 苏苏
#@File : 第五课.py
#@Software : PyCharm


#定义一个gcd(m, n)函数，该函数可以求出m与n的最大公约数，用辗转相除法递归实现。


def gcd(m,n):
    while n:
        r = m%n
        m = n
        n = r
    return m

print(gcd(15,25))


'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(-3))


def echo(string):
    return string + "hello"

a = "22"
print(echo(a))
print(echo("xiaoming"))

'''





