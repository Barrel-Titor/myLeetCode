from typing import List, Optional

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a, b = head, head
        for _ in range(k):
            if not b:
                return head
            b = b.next
        newHead = self.reverseBeforeB(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead

    def reverseBeforeB(self, head: Optional[ListNode], b: ListNode) -> ListNode:
        if not head or not head.next or head.next == b:
            return head
        last = self.reverseBeforeB(head.next, b)
        head.next.next = head
        head.next = None
        return last
# @lc code=end

