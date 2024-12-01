"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dq = deque()
        result = float("inf")

        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return result if result != float("inf") else -1
