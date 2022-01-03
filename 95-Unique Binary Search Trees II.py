"""
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.memo = dict()
        self.memo[0] = [None]

    def generateTrees(self, n: int, offset: int=0) -> List[TreeNode]:
        """
        长度为n的数组，所有可能的BST，结构是同构的
        例: [1, 2]和[2, 3]，所有可能的BST，结构完全一致，数字不同
        failed，输出很诡异
        """
        if self.memo.get(n):
            if offset == 0:
                return self.memo[n]
            else:
                result = self.memo[n]
                for root in result:
                    q = deque()
                    q.append(root)
                    while q:
                        node = q.popleft()
                        if node:
                            q.append(node.left)
                            q.append(node.right)
                            node.val += offset
                return result

        result = []
        for mid in range(1, n + 1):
            left_trees = self.generateTrees(mid - 1, offset=offset)
            right_trees = self.generateTrees(n - mid, offset=mid + offset)

            root = TreeNode(mid + offset)
            for left in left_trees:
                for right in right_trees:
                    root.left = left
                    root.right = right
                    result.append(root)
        self.memo[n] = result
        return result


class labuladongSolution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        1、穷举 root 节点的所有可能。
        2、递归构造出左右子树的所有合法 BST。
        3、给 root 节点穷举所有左右子树的组合。
        """
        if n == 0:
            return []
        return self.build(1, n)
    
    def build(self, lo, hi) -> List[TreeNode]:
        if lo > hi:
            return [None]
        
        result = []
        # 1、穷举 root 节点的所有可能。
        for mid in range(lo, hi + 1):
            # 2、递归构造出左右子树的所有合法 BST。
            left_trees = self.build(lo, mid - 1)
            right_trees = self.build(mid + 1, hi)

            # 3、给 root 节点穷举所有左右子树的组合。
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(mid)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result


class dpSolution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-7/
        [1, 2]与[99, 100]同构，动态规划解法
        """
        dp = [[] for _ in range(n+1)]
        dp[0] = [None]

        # 长度为 len，从 1 到 n
        for len in range(1, n + 1):
            dp[len] = []
            # 将不同数字作为根节点
            for mid in range(1, len + 1):
                left_size = mid - 1
                right_size = len - mid
                for left in dp[left_size]:
                    for right in dp[right_size]:
                        root = TreeNode(mid)
                        root.left = left
                        root.right = self.clone(right, mid)
                        dp[len].append(root)
        
        return dp[n]

    def clone(self, root, offset):
        if not root:
            return None
        
        node = TreeNode(root.val + offset)
        node.left = self.clone(root.left, offset)
        node.right = self.clone(root.right, offset)
        return node


if __name__ == '__main__':
    s = Solution()
    print(len(s.generateTrees(0)))