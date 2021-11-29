"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""
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


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))