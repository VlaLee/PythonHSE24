"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game-ii/?envType=problem-list-v2&envId=array
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [100000] * n
        dp[0] = 0

        for i in range(n):
            for j in range(0, nums[i] + 1):
                if i + j >= n:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]
