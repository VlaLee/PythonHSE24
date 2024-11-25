"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        s1 = "".join([chr(i) for i in nums1])
        s2 = "".join([chr(j) for j in nums2])
        c = 0
        l, r = 0, 1
        while r < len(nums1) + 1:
            if s1[l:r] in s2:
                c = max(len(s1[l:r]), c)
                r += 1
            else:
                l += 1
        return c
