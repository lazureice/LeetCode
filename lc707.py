class Node(object):
    """docstring for Node"""

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = Node(val)

        new_node.next = self.head.next
        self.head.next = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new_node = Node(val)
        if self.length == 0:
            self.head.next = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.length:
            return
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)
        node = self.head
        new_node = Node(val)
        while index:
            node = node.next
            index -= 1
        new_node.next = node.next
        node.next = new_node
        self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.length:
            return
        node = self.head
        for i in range(index):
            node = node.next
        if index == self.length - 1:
            self.tail = node

        node.next = node.next.next
        self.length -= 1

