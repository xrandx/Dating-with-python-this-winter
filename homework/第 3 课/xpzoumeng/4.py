##4
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if i >= 1:
                nums[i] += nums[i - 1]
        return nums
        