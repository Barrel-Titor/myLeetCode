"""
https://leetcode.com/problems/pascals-triangle-ii/
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex - 1)
        return list(map(
            lambda x, y: x + y,
            prev + [0],
            [0] + prev
        ))


class AntaresTsaoSolution:
    """
    https://leetcode.com/problems/pascals-triangle-ii/discuss/38467/Very-simple-Python-solution
    runs 30% faster than using map()
    """
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


class xiaobingzhangSolution:
    """
    https://leetcode.com/problems/pascals-triangle-ii/discuss/38420/Here-is-my-brief-O(k)-solution
    each row's [i]th index is actually the sum of [i] and [i-1] of the previous row
    """
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        # i-th row
        for i in range(1, rowIndex + 1):
            for j in range(i-1, 0, -1):
                result[j] = result[j-1] + result[j]
            result.append(1)
        return result


class LeetCodeAnimationSolution:
    """
    https://github.com/MisterBooo/LeetCodeAnimation/blob/master/notes/LeetCode%E7%AC%AC119%E5%8F%B7%E9%97%AE%E9%A2%98%EF%BC%9A%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92II.md
    杨辉三角很隐藏的规律：对于杨辉三角的第 k 行，第 (i + 1) 项是第 i 项的 ( k - i ) /( i + 1 ) 倍
    """
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        index = 1
        for i in range(rowIndex + 1):
            res.append(index)
            index *= ((rowIndex - i) / (i + 1))
        return res
