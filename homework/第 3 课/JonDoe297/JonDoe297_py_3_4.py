# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 8:12 PM
# @Author  : agrroc
# @File    : py_3_$.py
# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。

nums = [1, 1, 1, 4]
sum = 0
sums = []
for i in range(len(nums)):
    sum += nums[i]
    sums.append(sum)
nums = sums
print(nums)