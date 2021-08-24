"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from abc import abstractproperty
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ridiculous DFS
    552 ms, faster than 66.75%
    53.1 MB, less than 37.67%
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class wfei26Solution:
    """BFS
    https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36045/My-4-Line-java-solution
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        level = 1
        while queue:
            for _ in queue:
                current = queue.pop(0)
                if not current.left and not current.right:
                    return level
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level += 1
        return level


class OldCodingFarmerSolution:
    """BFS
    https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions.
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))