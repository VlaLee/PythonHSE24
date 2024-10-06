"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for i in range(n)] * n

        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]
