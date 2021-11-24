"""
https://leetcode-cn.com/problems/find-duplicate-subtrees/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.freq_table = dict()
        self.result = []
        # self.result = set()

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.traverse(root)
        return self.result
        # return list(self.result)
    
    def traverse(self, root) -> str:
        """
        use string to show the pre-order of a tree
        record these strings in freq_table
        compare strings to show whether there are duplicate subtrees
        """
        if not root:
            return '#'
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        subtree = str(root.val) + ',' + left + ',' + right

        # get frequency of subtree from freq_table
        freq = self.freq_table.get(subtree, 0)

        # duplicate subtree
        if freq == 1:
            # avoid the same structure appears in result for many times
            self.result.append(root)
        # if freq:
        #     self.result.add(root)
        
        self.freq_table[subtree] = freq + 1

        return subtree