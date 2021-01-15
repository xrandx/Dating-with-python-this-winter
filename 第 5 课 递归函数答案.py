#   1.  初始条件是 x, y
#   2.  辗转相除法利用的是 (a, b)的最大公约数 = (b, r)的最大公约数，于是可以利用这个降低问题规模
#       注：如果 a < b， 则 a % b = a, 即 a = a + 0 * b
#   3.  确定终止条件，如果余数为 0，就要终止，任意的x % 0 = x， 为返回值
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


#   1.  初始条件是 n，factorial(n) 得出 阶乘结果
#   2.  n! = n * (n - 1)!   降低问题规模
#   3.  确定终止条件，如果 n = 1 或者 n = 0，就返回阶乘 1
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#   1.  初始条件是 shorter, longer, k 。 divingBoard得出的是一个不重复的长度列表
#   2.  降低问题规模： 【k 个木板拼出的不同长度】 = 【k - 1 个木板拼出的不同长度 】 拼上 【长木板 】或【短木板】
#   3.  确定终止条件： 【0 块木板】 拼的长度为 0
#   注意：leetcode上这个答案过不了，因为这个题用递归会超出最大递归的深度，😂 当初看到这道题分类在【递归】下面，结果用递归做不了，是我大意了。很多时候把递归的函数改成非递归的函数，能节省更多内存。

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        if k == 0:
            return []
        else:
            total = []
            for i in self.divingBoard(shorter, longer, k - 1):
                total.append(i + shorter)
                total.append(i + longer)
            result = []
            for i in total:
                if i not in result:
                    result.append(i)
            return result


def main():
    pass


if __name__ == '__main__':
    main()
