# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        hk = west = head
        for i in range(n):
            hk = hk.next
        if not hk:
            return head.next
        while hk.next:
            hk = hk.next
            west = west.next
        west.next = west.next.next
        return head
