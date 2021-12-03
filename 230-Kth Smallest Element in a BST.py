"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = 0
        self.result = 0
        self.inorder(root, k)
        return self.result
    
    def inorder(self, root, k):
        if not root:
            return
        
        self.inorder(root.left, k)

        self.rank += 1
        if self.rank == k:
            self.result = root.val
            return
        
        self.inorder(root.right, k)
