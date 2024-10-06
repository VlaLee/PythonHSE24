"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=problem-list-v2&envId=array
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        ansl, ansr = -1, -1

        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                ansl = c
                r = c - 1
            if nums[c] < target:
                l = c + 1
            if nums[c] > target:
                r = c - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                ansr = c
                l = c + 1
            if nums[c] < target:
                l = c + 1
            if nums[c] > target:
                r = c - 1

        return [ansl, ansr]
