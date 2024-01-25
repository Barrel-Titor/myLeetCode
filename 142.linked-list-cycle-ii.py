from typing import List, Optional

#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        # Now slow and fast are at the same node in the cycle
        # Let's find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
# @lc code=end

