"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/count-primes/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        d = [0] * n

        if n:
            d[0] = 1
        if n > 1:
            d[1] = 1

        for i in range(2, n):
            if not d[i]:
                for j in range(i * i, n, i):
                    d[j] = 1

        return len([x for x in d if not x])
