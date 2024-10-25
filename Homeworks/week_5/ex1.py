"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/ugly-number-ii/description/?envType=problem-list-v2&envId=hash-table
"""

from sortedcontainers import SortedSet


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = SortedSet()
        s.add(1)
        for i in range(0, n + 1):
            s.add(s[i] * 2)
            s.add(s[i] * 3)
            s.add(s[i] * 5)

        return s[n - 1]
