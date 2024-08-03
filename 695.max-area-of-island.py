from typing import List, Optional

#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.max_area = max(self.max_area, self.dfs(grid, i, j))
        return self.max_area
    
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])):
            return 0
        if grid[i][j] == 0:
            return 0
        
        grid[i][j] = 0
        return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i, j - 1)
        
# @lc code=end

