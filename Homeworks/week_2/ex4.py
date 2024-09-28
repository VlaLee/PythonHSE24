"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        matchingList = [0] * 1000
        ans = 0

        while l < len(s):
            while r < len(s):
                if not matchingList[ord(s[r])]:
                    ans = max(ans, r - l + 1)
                    matchingList[ord(s[r])] = 1
                    r += 1
                else:
                    break
            matchingList[ord(s[l])] = 0
            l += 1

        return ans
