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


# https://labuladong.github.io/algo/di-ling-zh-bfe1b/shuang-zhi-0f7cc/#%E5%90%88%E5%B9%B6-k-%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8
class labuladongSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        if not lists:
            return
        
        dummy = ListNode()
        p = dummy
        pq = []

        # According to the heapq documentation, the way to customize the heap order 
        # is to have each element on the heap to be a tuple, 
        # with the first tuple element being one that accepts normal Python comparisons.
        
        # The extra index is to avoid clashes when the evaluated key value is a draw 
        # and the stored value is not directly comparable,
        # otherwise heapq could fail with TypeError
        index = 0
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, index, head))
                index += 1
        
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node
            if node.next:
                node = node.next
                heapq.heappush(pq, (node.val, index, node))
                index += 1
            p = p.next
        
        return dummy.next