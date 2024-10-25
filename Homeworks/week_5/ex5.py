"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-word-in-dictionary/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        visited = {""}
        res = ""

        for word in words:
            if word[:-1] in visited:
                visited.add(word)
                if len(word) > len(res):
                    res = word

        return res
