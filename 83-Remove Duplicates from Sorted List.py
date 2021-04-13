"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast

            if fast.next:
                fast = fast.next
            else:
                slow.next = None
                break
        return head


class OfficialSolution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while not current and not current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
