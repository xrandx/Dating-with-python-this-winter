#-*- codeing = utf-8 -*-
#@Time : 2021-01-08 20:26
#@Author : 苏苏
#@File : 第三节课作业3.py
#@Software : PyCharm

#左旋转字符串


class Solution:
    def reverseLeftWords(self,s:str,n:int) ->str:
        res = ""
        for i in range(n,len(s)):
            res += s[i]
        for i in range(n):
            res +=s[i]
            return res


'''

class Solution(object):
 def reverseLeftWords(self,s,n):
     return s[n:] +s[0:n]

'''