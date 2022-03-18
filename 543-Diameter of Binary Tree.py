"""
https://leetcode-cn.com/problems/diameter-of-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.diameter
        
    def depth(self, root: TreeNode):
        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        self.diameter = max(left + right, self.diameter)

        return max(left, right) + 1
