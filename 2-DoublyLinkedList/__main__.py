# __main__.py - Main module for Doubly Linked List algorithm
# ----------------------------------------------------
#
# March 2022, Tempy Charoenvasnadumrong
#
# ----------------------------------------------------

""" Main module for Doubly Linked list algorithm """

from pickle import TRUE
from typing import Optional, Union


class Node:
    """Node in a linked list"""

    def __init__(self, value: int) -> None:
        """Initialize the node object"""
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoublyLinkedList:
    """Doubly linked list class"""

    def __init__(self, value) -> None:
        """Initialiase a doubly linked list class"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def _check_no_node_case(self) -> bool:
        """
        Check the case where there are no nodes in
        doubly linked list.
        """
        if self.head is None:
            assert self.length == 0
            assert self.tail is None
            return False
        return True

    def append(self, value) -> bool:
        """Append a new node to the end of a doubly linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Union[Node, None]:
        """
        Pop the last item of the doubly linked list.
        3 cases are handled.
        """
        # 1) There is nothing in the list
        if not self._check_no_node_case():
            return None

        # 2) Single edge cases will need their heads and tails set to None
        # as this should now be an empty list
        temp_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # 3) There are more than 2 nodes are the generic case
            self.tail = self.tail.prev
            self.tail.next = None
            temp_node.prev = None
        self.length -= 1
        return temp_node

    def prepend(self, value: int) -> bool:
        """Add a node to the start of the doubly linked list"""
        new_node = Node(value)
        if self.head is None:
            assert self.tail is None
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Union[None, Node]:
        """Pop the first node in the doubly linked list"""
        if not self._check_no_node_case():
            return None
        temp_node = self.head

        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp_node.next = None
        self.length -= 1
        return temp_node

    def get(self, index: int) -> Optional[Node]:
        """Get a node at the specified index"""
        if not self._check_no_node_case():
            return None

        if index > self.length - 1 and index < 0:
            return None

        if index < self.length / 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_node = temp_node.prev
        return temp_node

    def set_value(self, index: int, value: int) -> bool:
        """Set the value of a certain node at the specified index"""
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        """Insert a node at a particular index"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.prev = prev_node

        next_node.prev = new_node
        new_node.next = next_node

        self.length += 1
        return True

    def remove(self, index) -> None:
        """Remove a node at a certain index"""
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp_node = self.get(index)
        temp_node.next.prev = temp_node.prev
        temp_node.prev.next = temp_node.next

        temp_node.next = None
        temp_node.prev = None
        self.length -= 1

        return True

    def print_list(self) -> None:
        """Print the doubly linked list"""
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


mylist = DoublyLinkedList(7)
mylist.prepend(8)
mylist.append(2)
mylist.append(3)
print(mylist.get(0).value)
print("--------------")

mylist.print_list()
print("--------------")
mylist.set_value(2, 17)
mylist.print_list()
print("--------------")
mylist.insert(4, 69)
mylist.remove(3)
print("--------------")

mylist.print_list()
