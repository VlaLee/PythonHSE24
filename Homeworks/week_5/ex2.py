"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = {}

        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

        res = []
        for i in range(k):
            curr_max_idx = max(cnt, key=cnt.get)
            res.append(curr_max_idx)
            cnt.pop(curr_max_idx)

        return res
