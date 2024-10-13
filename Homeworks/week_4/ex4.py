"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/single-number-iii/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        set_bit = xor_sum & -xor_sum

        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
