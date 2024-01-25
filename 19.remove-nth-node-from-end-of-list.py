from typing import List, Optional

#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        x = self.findKthFromEnd(dummy, n + 1)
        x.next = x.next.next
        return dummy.next
    
    def findKthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        for _ in range(k):
            fast = fast.next
        slow = head
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
        
# @lc code=end

