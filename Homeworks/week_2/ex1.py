"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/shortest-palindrome/description/?envType=problem-list-v2&envId=string&difficulty=HARD
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse: str = s[::-1]

        for i in range(len(s)):
            if s.startswith(reverse[i:]):
                return reverse[:i] + s

        return s + reverse
