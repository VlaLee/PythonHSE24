"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=array
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        result = 0
        while l <= r:
            mn = min(height[r], height[l])
            result = max(result, (r - l) * mn)

            if mn == height[l]:
                l += 1
            else:
                r -= 1

        return result
