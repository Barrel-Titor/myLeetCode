"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA, currB = headA, headB
        prevA = prevB = 'head'
        table = dict()
        while currA or currB:
            if currA:
                if not table.get(currA):
                    table[currA] = prevA
                else:
                    return currA
                prevA = currA
                currA = currA.next
            
            if currB:
                if not table.get(currB):
                    table[currB] = prevB
                else:
                    return currB
                prevB = currB
                currB = currB.next
        return None


class myfavcatSolution:
    """https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!

    I found most solutions here preprocess linkedlists to get the difference in len.
    Actually we don't care about the "value" of difference, we just want to make sure two pointers reach the intersection node at the same time.

    We can use two iterations to do that. 
    In the first iteration, we will reset the pointer of one linkedlist to the head of another linkedlist after it reaches the tail node. 
    In the second iteration, we will move two pointers until they points to the same node. 
    Our operations in first iteration will help us counteract the difference. 
    So if two linkedlist intersects, the meeting point in second iteration must be the intersection point. 
    If the two linked lists have no intersection at all, then the meeting pointer in second iteration must be the tail node of both lists, which is null
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # boundary check
        if not headA or not headB:
            return None
        
        a, b = headA, headB

        # if a and b have diffenrent len, then we'll stop the loop after second iteration
        while a != b:
            # at the end of first iteration, we reset the pointer to the head of another linkedlist
            a = a.next if a else headB
            b = b.next if b else headA

        return a