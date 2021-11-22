"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """BFS
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        queue.append(root)
        # outer loop controls the number of layer
        while len(queue) > 0:
            # traverse nodes in each layer
            layer = deque()
            while len(queue) > 0:
                node = queue.popleft()
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
                # add links
                if len(queue) > 0:
                    node.next = queue[0]
            queue = layer
        return root


class OfficialSolution1:
    """BFS
    https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class OfficialSolution2:
    """use established next pointer of former layers
    https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
    """
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # establish pointers of (N+1)-th layer when traversing N-th layer
        leftmost = root
        # exists (N+1)-th layer
        while leftmost.left:
            # head is in N-th layer
            head = leftmost
            
            while head:
                # connect 2 children of head
                head.left.next = head.right

                # connect head.right and head.next.left
                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left
        
        return root
