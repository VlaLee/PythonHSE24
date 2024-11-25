"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1, dic2 = {}, {}

        for i in s1:
            dic1[i] = dic1.get(i, 0) + 1

        m, n = len(s1), len(s2)

        if m > n:
            return False

        for i in range(m):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1

        for i in range(m, n):
            if dic1 == dic2:
                return True

            dic2[s2[i]] = dic2.get(s2[i], 0) + 1

            dic2[s2[i - m]] -= 1
            if dic2[s2[i - m]] == 0:
                del dic2[s2[i - m]]

        return dic1 == dic2
