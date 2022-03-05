# __main__.py - Main module for Linked List algorithm
# ----------------------------------------------------
#
# February 2022, Tempy Charoenvasnadumrong
#
# ----------------------------------------------------

""" Main module for Linked list algorithm """


from typing import Literal, Optional


class Node:
    """Node in a linked list"""

    def __init__(self, value) -> None:
        """Initialize the node object"""
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    """Linked List Class"""

    def __init__(self, value: int) -> None:
        """Initialize the linked list object"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: int) -> Literal[True]:
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

    def prepend(self, value: int) -> Literal[True]:
        """Prepend a new node to the linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index: int, value: int) -> bool:
        """Insert a new value into a linked list with a particular value"""
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)

        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1

        return True

    def remove(self, index: int) -> None:
        """Remove a node at a particular index"""
        if index < 0 or index > self.length:
            return
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()

        prev_node = self.get(index - 1)
        temp_node = self.get(index)
        prev_node.next = temp_node.next
        self.length -= 1

    def pop(self) -> Optional[Node]:
        """Pops last node from the linked list"""

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

    def pop_first(self) -> Optional[Node]:
        """Pop first node from linked list"""

        if self.length == 0:
            return

        temp_node = self.head
        temp_node.next = None

        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            # NOTE - self.head would already be None.
            self.tail = None

        return temp_node

    def print_list(self) -> None:
        """Print the linked list"""
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def get(self, index: int) -> Optional[Node]:
        """Get the node at the specified index"""

        if index < 0 or index > self.length:
            return

        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next

        return temp_node

    def set_value(self, index: int, value: int) -> bool:
        """Sets a value inside the linked list"""

        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def reverse(self) -> None:
        """Reverse a linked list. A common interview question."""

        # Start by reversing head and tail.
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node

        # Define variables on either side of the temp_node.
        # This ensures information is contained.
        prev_node = None

        for _ in range(self.length):
            next_node = temp_node.next
            temp_node.next = prev_node

            prev_node = temp_node
            temp_node = next_node


mylinkedlist = LinkedList(0)

for i in range(1, 10):
    mylinkedlist.append(i)

# mylinkedlist.print_list()

mylinkedlist.reverse()
mylinkedlist.print_list()
