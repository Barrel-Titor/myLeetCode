"""
https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            if i != 0:
                row.append(1)
            triangle.append(row)
        return triangle


class FirstOfHisName7Solution:
    """
    https://leetcode.com/problems/pascals-triangle/discuss/38141/My-concise-solution-in-Java
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])
        return result


class sherlock321Solution:
    """
    https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.

    explanation: Any row can be constructed using the offset sum of the previous row. Example:
    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
    """
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            res += [list(map(
                lambda x, y: x + y,
                res[-1] + [0],
                [0] + res[-1]
            ))]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(5))
