"""
https://leetcode.com/problems/balanced-binary-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


class benlongSolution:
    """bottom up O(N) solution
    https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better

    you can optimize by returning -1 before checking the right side of the tree if dfsHeight(root.left) returns -1. This could save a lot of time if the tree is heavily skewed right.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfsHeight(root.left)
        if left == -1:
            return -1

        right = self.dfsHeight(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
