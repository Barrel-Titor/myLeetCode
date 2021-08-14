"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        mid = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + mid + right


class OfficialSolution1:
    '''Recursive Approach'''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root: Optional[TreeNode], res: List[int]):
        if root:
            if root.left:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right:
                self.helper(root.right, res)


class OfficialSolution2:
    '''Iterating method using Stack'''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


class OfficialSolution3:
    '''Morris Traversal

    While current is not NULL,
    If current does not have left child
        a. Add current’s value
        b. Go to the right, i.e., current = current.right
    Else
        a. In current's left subtree, make current the right child of the rightmost node
        b. Go to this left child, i.e., current = current.left
    '''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return []
