"""
https://leetcode.com/problems/same-tree/
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p and q:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right):
                    return True
                else:
                    return False


class OfficialSolution1:
    """Recursion
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


class OfficialSolution2:
    """Queue
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            # both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        
        return True


class lxnnSolution:
    """Stack
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            elif p or q:
                return False
        return True

'''
The 2 solutions in the analysis are not the same. (Yours and the first one are indeed similar, the second one is different.) When you use a stack, which is a last in first out data structure, the nodes are traversed in depth first order, meaning you go from parent to child all the way down to a leaf node and only then return to process children left behind, so that when processing a tree, one of its sub-trees is fully processed first, before starting to process the other one. And you are right that it does not matter if the stack behavior is achieved by using recursion or implemented iteratively by using the stack data structure as you did. The second solution uses a queue, which is a first in first out data structure. When using it the nodes are traversed in breadth first order, meaning the tree is processed layer by layer, and the traversal does not go deeper into any of the sub-trees before all nodes from the previous layer (nodes of one layer have the same height relative to the root of the tree) are traversed.

By using a queue, we are doing BFS and by using a stack we are doing DFS.
Now the difference is, if we have been told to solve the problem with BFS then queue makes sense but if there are no constraints then using a stack makes sense because although space complexity of both approaches are same, BFS incurs more space because queue in python is internally implement using LL which as more memory footprint then a stack which is just a normal list or dynamic array.
'''