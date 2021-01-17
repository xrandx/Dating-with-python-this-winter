#定义阶乘函数,相当于完成n * (n-1) * ... * 1的操作
def factorial(n):
    # 输入的参数是1，直接返回1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
#调用函数
x = factorial(n)
print('%d 的阶乘为 %d.' % (n, x))