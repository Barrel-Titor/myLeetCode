from typing import List, Optional

#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        for i in range(m):
            self.dfs(grid, i, 0)
            self.dfs(grid, i, n - 1)
        
        for j in range(n):
            self.dfs(grid, 0, j)
            self.dfs(grid, m - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 1
        return result
    
    def dfs(self, grid: List[List[int]], i: int, j: int):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])):
            return
        if grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        for d in directions:
            self.dfs(grid, i + d[0], j + d[1])
# @lc code=end

