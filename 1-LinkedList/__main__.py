# __main__.py - Main module for Linked List algorithm
# ----------------------------------------------------
#
# February 2022, Tempy Charoenvasnadumrong
#
# ----------------------------------------------------

""" Main module for Linked list algorithm """


class Node:
    """Node in a linked list"""

    def __init__(self, value) -> None:
        """Initialize the node object"""
        self.value = value
        self.next = None


class LinkedList:
    """Linked List Class"""

    def __init__(self, value) -> None:
        """Initialize the linked list object"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> None:
        """Appends a new node to the linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value) -> None:
        pass

    def insert(self, value) -> None:
        pass

    def pop(self) -> None:
        """Remove last note from the linked list"""

        if self.length == 0:
            return

        temp_node = self.head
        pre_node = self.head
        # Iterate until we find the node prior to the tail
        while temp_node.next:
            pre_node = temp_node
            temp_node = temp_node.next

        self.tail = pre_node
        self.tail.next = None
        self.length -= 1

        # If there's nothing left in the linked list then reset.
        if self.length == 0:
            self.tail = None
            self.head = None

        return temp_node

    def print_list(self):
        """Print the linked list"""
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


mylinkedlist = LinkedList(4)
mylinkedlist.print_list()
