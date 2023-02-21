# https://leetcode.com/problems/partition-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(), ListNode()
        p, p1, p2 = head, dummy1, dummy2

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next

        p1.next = dummy2.next
        p2.next = None
        return dummy1.next
