"""
https://leetcode-cn.com/problems/unique-binary-search-trees/
"""
class Solution:
    def __init__(self) -> None:
        self.memo = dict()

    def numTrees(self, n: int) -> int:
        if self.memo.get(n):
            return self.memo[n]

        if n == 0 or n == 1:
            self.memo[0] = 1
            self.memo[1] = 1
            return 1
        
        result = 0
        for mid in range(1, n + 1):
            left_count = self.numTrees(mid - 1)
            right_count = self.numTrees(n - mid)
            result += left_count * right_count
        self.memo[n] = result
        return result