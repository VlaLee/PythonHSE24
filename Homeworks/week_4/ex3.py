"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result = 0
        table = [0] * len(nums)

        for r in range(2, len(nums)):
            diff1 = nums[r] - nums[r - 1]
            diff2 = nums[r - 1] - nums[r - 2]

            if diff1 == diff2:
                table[r] = table[r - 1] + 1
                result += table[r - 1] + 1

        return result
