"""
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        # move left subtree to right
        root.right = root.left
        root.left = None
        # combine original right subtree after original left subtree
        p = root
        while p.right:
            p = p.right
        p = tmp