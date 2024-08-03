from typing import List, Optional

#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(N-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[N-j-1][N-i-1]
                matrix[N-j-1][N-i-1] = tmp
        # print(matrix)
        for i in range(N//2):
            for j in range(N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[N-i-1][j]
                matrix[N-i-1][j] = tmp
        # print(matrix)
        
# @lc code=end

