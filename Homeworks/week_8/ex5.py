"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        s = set()
        left = 0
        max_sum = 0
        cur_sum = 0

        for right, num in enumerate(nums):
            while num in s:
                s.remove(nums[left])
                cur_sum -= nums[left]
                left += 1

            cur_sum += num
            s.add(num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
