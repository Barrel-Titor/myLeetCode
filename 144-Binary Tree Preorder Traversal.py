"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result


class pavelshlykSolution:
    """https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45266/Accepted-iterative-solution-in-Java-using-stack.

    iterative solution in Java using stack.
    Note that in this solution only right children are stored to stack.
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        rights = []
        node = root
        while node:
            list.append(node.val)
            if node.right:
                rights.append(node.right)

            node = node.left
            if not node and rights:
                node = rights.pop()
        return list


class fabrizio3pavelshlykSolution:
    """https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45468/3-Different-Solutions

    Iterative method with Stack
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        tovisit = []
        tovisit.append(root)

        while tovisit:
            visiting = tovisit.pop()
            result.append(visiting.val)
            if visiting.right:
                tovisit.append(visiting.right)
            if visiting.left:
                tovisit.append(visiting.left)
        
        return result


class clueSolution:
    """https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45273/Very-simple-iterative-Python-solution

    Very simple iterative Python solution
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result