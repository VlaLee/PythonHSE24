"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/distinct-subsequences/description/?envType=problem-list-v2&envId=string&difficulty=HARD
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n: int = len(s)
        m: int = len(t)
        dp: list[list] = [[j for j in range(m + 1)] for i in range(n + 1)]

        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
        for j in range(1, m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]
