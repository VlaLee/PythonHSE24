"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/?envType=problem-list-v2&envId=string
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        stack - массив "непригодных" индексов
        ответ будем искать среди разностей соседей "непригодных" индексов
        т.к. между ними - правильная скобочная последовательность
        """

        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif len(stack) > 0 and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)

        stack = [-1] + stack + [len(s)]
        ans = 0
        for i in range(len(stack) - 1):
            ans = max(ans, stack[i + 1] - stack[i] - 1)

        return ans
