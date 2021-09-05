"""
https://leetcode.com/problems/linked-list-cycle/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        passed = []
        current = head
        while current.next:
            if current in passed:
                return True
            else:
                passed.append(current)
                current = current.next
        return False


class fabrizio3Solution:
    """https://leetcode.com/problems/linked-list-cycle/discuss/44489/O(1)-Space-Solution

    1. Use two pointers, walker and runner.
    2. walker moves step by step. runner moves two steps at time.
    3. if the Linked List has a cycle walker and runner will meet at some point.
    """
    def hasCycle(self, head: ListNode) -> bool:
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False