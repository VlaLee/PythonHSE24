"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def numSubarraysAtMostSum(self, nums: list[int], goal: int) -> int:
        i = 0
        su = 0
        res = 0
        n = len(nums)
        for j in range(n):
            su += nums[j]
            while i <= j and su > goal:
                su -= nums[i]
                i += 1
            res += j - i + 1
        return res

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.numSubarraysAtMostSum(
            nums, goal
        ) - self.numSubarraysAtMostSum(nums, goal - 1)
