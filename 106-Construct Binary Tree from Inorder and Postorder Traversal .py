"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        
        root = TreeNode(postorder[-1])
        root_index_inorder = inorder.index(root.val)
        left_size = root_index_inorder

        root.left = self.buildTree(
            inorder[: left_size], postorder[: left_size]
        )
        root.right = self.buildTree(
            inorder[left_size + 1: ], postorder[left_size: -1]
        )

        return root


class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        return self.buildTreeHelper(inorder, postorder, 0, n-1, 0, n-1)

    def buildTreeHelper(
        self, inorder, postorder,
        in_low, in_high,
        post_low, post_high
    ) -> TreeNode:
        if in_low > in_high or post_low > post_high:
            return

        root = TreeNode(postorder[post_high])
        root_index_inorder = inorder.index(root.val)
        left_size = root_index_inorder - in_low

        root.left = self.buildTreeHelper(
            inorder, postorder,
            in_low, root_index_inorder - 1,
            post_low, post_low + left_size - 1
        )

        root.right = self.buildTreeHelper(
            inorder, postorder,
            root_index_inorder + 1, in_high,
            post_low + left_size, post_high - 1
        )

        return root
