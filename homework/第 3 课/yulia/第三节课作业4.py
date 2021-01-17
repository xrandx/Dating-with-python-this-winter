#-*- codeing = utf-8 -*-
#@Time : 2021-01-08 20:45
#@Author : 苏苏
#@File : 第三节课作业4.py
#@Software : PyCharm


class Solution:
    def runningSum(self, nums):
        if not nums:
            return[]
        for i in range(1,len(nums)):
            nums[i]=nums(i)+nums[i-1]
        return nums
