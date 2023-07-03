from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.partition(lists, 0, len(lists) - 1)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        p, p1, p2 = dummy, l1, l2

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next

    def partition(self, lists, start_index, end_index):
        if start_index == end_index:
            return lists[start_index]
        elif start_index < end_index:
            middle_index = (start_index + end_index) // 2
            lists1 = self.partition(lists, start_index, middle_index)
            lists2 = self.partition(lists, middle_index + 1, end_index)
            return self.mergeTwoLists(lists1, lists2)
        else:
            return
