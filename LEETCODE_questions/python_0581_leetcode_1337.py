'''
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
'''


from typing import List
from heapq import heapify, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:


        scoreList = []

        for i in range(len(mat)):

            l = mat[i]

            for j in range(len(l)):
                if l[j] == 0:
                    scoreList.append(j * 1000 + i)
                    break
            else:
                scoreList.append(len(l) * 1000 + i)

        heapify(scoreList)

        resultList = []

        for _ in range(k):
            x = heappop(scoreList)
            resultList.append(x % 1000)

        return resultList

