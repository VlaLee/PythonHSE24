"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/text-justification/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        """
        combs - двумерный list, в каждом массиве - слова, входящие в i-ую строку
        temp - временный list для формирования слов i-ой строки с дальнейшим добавлением в combs
        sizes - количество пробелов для i-ой строки, которые мы можем использовать
        length - временная переменная для подсчета длины i-ой строки, включая минимально необходимые пробелы
        """

        combs = []
        temp = []
        sizes = []
        length = 0

        # preprocessing
        for word in words:
            length += len(word)
            if length + len(temp) <= maxWidth:
                temp.append(word)
            else:
                sizes.append(maxWidth - length + len(word))
                combs.append(temp)
                length = len(word)
                temp = [word]

        if len(temp):
            sizes.append(maxWidth - length)
            combs.append(temp)

        # само формирование возвращаемого list-а
        result = []

        for i in range(len(combs)):
            if len(combs[i]) == 1:
                result.append(combs[i][0] + ' ' * sizes[i])
                continue

            if i == len(combs) - 1:
                result.append(' '.join(combs[i]))
                result[-1] += ' ' * (sizes[i] - len(combs[i]) + 1)
                continue

            space_size = sizes[i] // (len(combs[i]) - 1)
            extra_spaces = sizes[i] % (len(combs[i]) - 1)

            for j in range(extra_spaces):
                combs[i][j] += ' '

            result.append((' ' * space_size).join(combs[i]))

        return result