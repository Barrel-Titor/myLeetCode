"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.memo = dict()

    def generateTrees(self, n: int, offset: int=0) -> List[TreeNode]:
        """
        长度为n的数组，所有可能的BST，结构是同构的
        例: [1, 2]和[2, 3]，所有可能的BST，结构完全一致，数字不同
        参考解法三: https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-7/
        """
        if self.memo.get(n):
            if offset == 0:
                return self.memo[n]
            else:
                for root in self.memo[n]:
                    q = deque()
                    q.append(root)
                    while q:
                        node = q.popleft()
                        if node:
                            q.append(node.left)
                            q.append(node.right)
                            node.val += offset
        
        if n == 0:
            return [None]

        result = []
        for mid in range(1, n + 1):
            left_trees = self.generateTrees(mid - 1, offset=offset)
            right_trees = self.generateTrees(n - mid, offset=mid + offset)

            root = TreeNode(mid)
            for left in left_trees:
                for right in right_trees:
                    root.left = left
                    root.right = right
                    result.append(root)
        self.memo[n] = result
        return result


if __name__ == '__main__':
    s = Solution()
    print(len(s.generateTrees(0)))