"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        l = []
        seen = set()
        dna = ""
        if len(s) >= 10:
            for i in range(len(s)):
                dna = s[i : i + 10]
                if dna in seen:
                    if dna not in l:
                        l.append(dna)
                seen.add(dna)
        return l
