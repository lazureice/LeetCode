# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # q = p = ListNode(0)
        # p.next = head
        p = head
        if head is None:
            return None

        while p.next:
            tem = p.next
            if tem.val == val:
                p.next = tem.next
            else:
                p = p.next

        # return head
        # head也有可能被删
        # return q.next

        # 这样也行
        if head.val == val:
            head = head.next
        return head
