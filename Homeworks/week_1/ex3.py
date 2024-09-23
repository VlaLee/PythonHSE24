"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-ladder/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> int:
        """
        основная идея - рассмотреть переход от одного слова к другому слову
        как ребро графа между этими словами
        и найти в таком графе наименьший путь из вершины beginWord в вершину endWord
        наименьший путь можно найти поиском в ширину (BFS-ом)
        distance[word] - дистанция до вершины word от вершины beginWord
        """

        letters = "abcdefghijklmnopqrstuvwxyz"
        distance = {}
        wordList.append(beginWord)

        # переводим list в set для большей производительности
        wordList = set(wordList)

        for word in wordList:
            distance[word] = 0
        distance[endWord] = 0

        distance[beginWord] = 1
        queue = []
        queue.append(beginWord)

        # сам алгоритм BFS-а
        while len(queue):
            v = queue.pop(0)
            for i in range(len(v)):
                for symb in letters:
                    u = v[:i] + symb + v[i + 1 :]
                    if u in wordList and distance[u] == 0:
                        distance[u] = distance[v] + 1
                        queue.append(u)

        return distance[endWord]
