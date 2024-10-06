"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/first-missing-positive/?envType=problem-list-v2&envId=array
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
