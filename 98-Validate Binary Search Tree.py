"""
https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)

    def helper(self, root, min, max):
        if not root:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.helper(root.left, min, root) \
            and self.helper(root.right, root, max)