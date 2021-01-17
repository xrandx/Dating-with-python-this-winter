#保证较大数被较小数除
def getGreatestCommonDivisor(a, b):
    if a > b:
        return gcd(a, b)
    else:
        return gcd(b, a)

#利用辗转相除法，递归计算最大公约数
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

a = int(input())
b = int(input())
print('%d and %d 的最大公约数为 %d.' % (a, b, getGreatestCommonDivisor(a, b)))
