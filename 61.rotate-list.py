from typing import List, Optional

#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            if not cur.next:
                last = cur
            cur = cur.next
        if N == 0:
            return head
        
        k %= N
        if k == 0:
            return head
        cur = head
        for _ in range(N-k-1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        last.next = head
        return new_head
# @lc code=end

