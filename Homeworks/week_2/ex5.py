"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hashMap: {str: str} = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result: list[str] = [""]

        for digit in digits:
            temp: list[str] = []
            for s in result:
                for letter in hashMap[digit]:
                    temp.append(s + letter)
            result = temp

        return result
