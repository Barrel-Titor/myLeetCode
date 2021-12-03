"""
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self.inorder(root)
        return root
    
    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.right)

        self.sum += root.val
        root.val = self.sum

        self.inorder(root.left)