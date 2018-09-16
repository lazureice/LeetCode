# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if not head.next:
            return head
        evenhead = even = head.next

        while even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
            even.next = odd.next
            even = even.next
                
        odd.next = evenhead
        return head


def test(s):

    g = (int(x) for x in s.split('->'))

    head = ListNode(0)
    tail = head
    for i in g:
        tail.next = node = ListNode(i)
        tail = tail.next
    soln=Solution()
    soln.oddEvenList(head.next)
    while(head):
        print(head.val)
        head = head.next


s = '1->2->3->4->5'
test(s)
