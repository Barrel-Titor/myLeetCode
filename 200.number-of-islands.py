from typing import List, Optional

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        self.visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    result += 1
                    self.dfs(grid, i, j)
        return result
    
    def dfs(self, grid: List[List[str]], i: int, j: int):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])):
            return
        if grid[i][j] == '0':
            return
        if self.visited[i][j]:
            return
        
        self.visited[i][j] = True
        for d in directions:
            self.dfs(grid, i + d[0], j + d[1])
        
        
# @lc code=end

