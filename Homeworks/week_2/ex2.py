"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/regular-expression-matching/description/?envType=problem-list-v2&envId=string&difficulty=HARD
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp: {tuple: bool} = {}

        def recursiveCall(i: int, j: int) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match: bool = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = max(
                    recursiveCall(i, j + 2), match and recursiveCall(i + 1, j)
                )
                return dp[(i, j)]

            if match:
                dp[(i, j)] = recursiveCall(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return recursiveCall(0, 0)
