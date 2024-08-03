from typing import List, Optional

#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i, j)
        
        result = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j] == 1:
                    result += 1
                    self.dfs(grid2, i, j)
        return result
    
    def dfs(self, grid: List[List[int]], i: int, j: int):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])):
            return
        if grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            self.dfs(grid, i + d[0], j + d[1])
# @lc code=end

