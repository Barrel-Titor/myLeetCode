"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        if mid - 1 >= 0:
            root.left = self.sortedArrayToBST(nums[: mid])
        if mid + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[mid+1: ])
        return root


class GoogleSolution:
    """
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35223/An-easy-Python-solution
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[: mid])
        root.right = self.sortedArrayToBST(nums[mid+1: ])
        return root
