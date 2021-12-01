"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class preorderCodec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        result = str(root.val) + ',' + left + ',' + right
        return result

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(',')
        return self.desHelper(nodes)
    
    def desHelper(self, nodes: list):
        if not nodes:
            return

        node = nodes.pop(0)
        if node == '#':
            return
        
        root = TreeNode(int(node))
        root.left = self.desHelper(nodes)
        root.right = self.desHelper(nodes)

        return root


class postorderCodec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        self.serHelper(root, result)
        return ','.join(result)
    
    def serHelper(self, root: TreeNode, result: list):
        if not root:
            result.append('#')
            return
        
        self.serHelper(root.left, result)
        self.serHelper(root.right, result)
        result.append(str(root.val))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(',')
        return self.desHelper(nodes)
    
    def desHelper(self, nodes: list):
        if not nodes:
            return
        
        node = nodes.pop()
        if node == '#':
            return

        root = TreeNode(int(node))
        root.right = self.desHelper(nodes)
        root.left = self.desHelper(nodes)

        return root


class BFSCodec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        
        result = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append('#')
        
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        nodes = data.split(',')
        q = deque()

        if nodes[0] == '#':
            return
        root = TreeNode(int(nodes[0]))
        q.append(root)

        i = 0
        while i < len(nodes) and q:
            parent = q.popleft()

            i += 1
            left = nodes[i]
            if left != '#':
                parent.left = TreeNode(int(left))
                q.append(parent.left)

            i += 1
            right = nodes[i]
            if right != '#':
                parent.right = TreeNode(int(right))
                q.append(parent.right)
        
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))