"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-duplicate-substring/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    """
    заметим, что если есть повторяющаяся строка размера k,
    то будет повторяющаяся строка размера k - 1
    используя эту монотонность, найдем ответ бинарным поиском
    а в качестве проверки, что в строке есть повторяющаяся подстрока
    будем сравнивать их по хэшам (алгоритмом Рабина-Карпа)
    """

    def RabinKarpMatching(self, s: str, length: int) -> str:
        hashMap = {}
        n = len(s)
        q = 1610612741
        d = 26
        h = 1
        text = 0

        for i in range(length - 1):
            h = (h * d) % q

        for i in range(length):
            text = (d * text + ord(s[i])) % q

        for i in range(len(s) - length + 1):
            if text in hashMap:
                if s[i : i + length] == hashMap[text][1]:
                    hashMap[text][0] += 1
            else:
                hashMap[text] = [1, s[i : i + length]]

            if i < n - length:
                text = (d * (text - ord(s[i]) * h) + ord(s[i + length])) % q

            if text < 0:
                text = text + q

        maxim = 1
        result = ""
        for key in hashMap:
            if hashMap[key][0] > maxim:
                maxim = hashMap[key][0]
                result = hashMap[key][1]

        return result

    def longestDupSubstring(self, s: str) -> str:
        l = 0
        r = len(s)
        ans = ""
        while l <= r:
            c = (l + r) // 2
            temp = self.RabinKarpMatching(s, c)
            if len(temp) >= 1:
                ans = temp
                l = c + 1
            else:
                r = c - 1

        return ans
