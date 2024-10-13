"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
