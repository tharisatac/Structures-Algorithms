# __main__.py - Main module for Stack & Queue Data Structure
# ----------------------------------------------------
#
# March 2022, Tempy Charoenvasnadumrong
#
# ----------------------------------------------------

""" Main module for Stack & Queue Data Structure Implementation """


class Node:
    """Node for a stack or queue"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Stack Data Structure"""

    def __init__(self, value) -> None:
        """Constructor"""
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value) -> None:
        """Push a node onto the top of the stack"""
        new_node = Node(value)
        if self.top is None:
            assert self.height == 0
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self) -> Node:
        """Pops and returns the top node"""
        if self.top is None:
            assert self.height == 0
            return

        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        self.height -= 1
        return temp_node

    def print_stack(self):
        """Prints the stack"""
        temp_node = self.top
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


class Queue:
    """A queue data structure"""

    def __init__(self, value) -> None:
        """Constructor for queue data structure"""
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value) -> None:
        """Adds a node to the queue"""
        new_node = Node(value)
        if self.first is None:
            assert self.last is None
            assert self.length == 0
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self) -> None:
        """Remove a node from the start of the queue"""
        if self.first is None:
            assert self.last is None
            assert self.length == 0
            return

        temp_node = self.first
        if self.length == 1:
            self.last = None
            self.first = None
        else:
            self.first = self.first.next
            temp_node.next = None

        self.length -= 1
        return temp_node

    def print_queue(self):
        """Prints the queue"""
        temp_node = self.first
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next


myq = Queue(1)
myq.enqueue(2)
myq.print_queue()
print(myq.dequeue().value)
print(myq.dequeue().value)
print(myq.dequeue().value)
