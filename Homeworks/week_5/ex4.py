"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/contiguous-array/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        ans = 0
        cnt = 0
        cntToIndex = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1

            if cnt in cntToIndex:
                ans = max(ans, i - cntToIndex[cnt])
            else:
                cntToIndex[cnt] = i

        return ans
