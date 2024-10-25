"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/k-diff-pairs-in-an-array/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l <= r:
                c = (l + r) // 2
                if nums[c] == nums[i] + k and i != c:
                    ans.add((nums[c], nums[i]))
                    break
                if nums[c] > nums[i] + k:
                    r = c - 1
                else:
                    l = c + 1

        return len(ans)
