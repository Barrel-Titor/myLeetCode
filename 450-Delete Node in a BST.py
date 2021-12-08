"""
https://leetcode-cn.com/problems/delete-node-in-a-bst/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == key:
            # 1. deleted node has no child
            if not (root.left or root.right):
                return

            # 2. deleted node has one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 3. deleted node has two children
            # switch deleted node and the min node (leftmost node) in right subtree
            # and then follow situation 1 and 2
            min_node = self.getMinNode(root.right)
            root.right = self.deleteNode(root.right, min_node.val)
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    def getMinNode(self, root):
        node = root
        while node.left:
            node = node.left
        return node