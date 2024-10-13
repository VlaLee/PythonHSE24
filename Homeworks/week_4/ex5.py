"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/single-number-iii/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        minval = 1e9
        minpos = -1
        ptrol = 0
        for i in range(len(gas)):
            ptrol += gas[i] - cost[i]
            if ptrol < minval:
                minval = ptrol
                minpos = i
        if ptrol >= 0:
            return (minpos + 1) % len(gas)
        return -1
