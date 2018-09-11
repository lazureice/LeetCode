# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        hk = head.next
        west = hk.next
        while hk != west:
            if west is None or west.next is None:
                return None
            hk = hk.next
            west = west.next.next

        hk = head
        while hk != west:
            hk = hk.next
            west = west.next
        return hk
