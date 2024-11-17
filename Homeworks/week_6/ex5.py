"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ws = 0
        d = {}
        freq = 0
        maxlen = 0
        for we in range(len(s)):
            c = s[we]
            d[c] = d.get(c, 0) + 1
            freq = max(freq, d[c])
            if we - ws + 1 - freq > k:
                leftchar = s[ws]
                d[leftchar] -= 1
                if d[leftchar] == 0:
                    del d[leftchar]
                ws += 1
            maxlen = max(maxlen, we - ws + 1)

        return maxlen
