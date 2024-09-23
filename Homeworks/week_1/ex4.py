"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/orderly-queue/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        заметим, что при k > 1 можно ВСЕГДА построить
        лексикографически отсортированную строку

        при k = 1 выберем наименьшую лексикографическую строку
        путем переброски текущего первого (нулевого) символа в конец строки
        """

        if k > 1:
            return "".join(sorted(s))

        ans = s
        for i in range(len(s)):
            ans = min(ans, s[i:] + s[:i])

        return ans
