"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return

        # preorder: root, left, right
        # inroder:  left, root, right
        root = TreeNode(preorder[0])

        # split inorder into left subtree and right subtree
        left_size = inorder.index(root.val)

        root.left = self.buildTree(preorder[1: left_size + 1], inorder[: left_size])
        root.right = self.buildTree(preorder[left_size + 1:], inorder[left_size + 1:])

        return root



class Solution2:
    def __init__(self) -> None:
        self.count = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        return self.buildTreeHelper(preorder, inorder, 0, n-1, 0, n-1)

    def buildTreeHelper(
            self, preorder, inorder, 
            pre_low, pre_high, 
            in_low, in_high
        ) -> TreeNode:
        if pre_low > pre_high or in_low > in_high:
            return

        # printIndent(self.count)
        # self.count += 1
        # print('pre: {} - {}, in: {} - {}'.format(
        #     pre_low, pre_high, in_low, in_high
        # ))
        
        root = TreeNode(preorder[pre_low])
        root_index_inorder = inorder.index(root.val)
        left_size = root_index_inorder - in_low

        root.left = self.buildTreeHelper(
            preorder, inorder,
            pre_low + 1, pre_low + left_size,
            in_low, root_index_inorder - 1
        )
        root.right = self.buildTreeHelper(
            preorder, inorder,
            pre_low + left_size + 1, pre_high,
            root_index_inorder + 1, in_high
        )

        # printIndent(self.count)
        # self.count -= 1
        # print('return Tree')

        return root


def printIndent(n):
    for i in range(n):
        print('    ', end='')


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    ret = Solution2().buildTree(preorder, inorder)
