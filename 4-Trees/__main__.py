# __main__.py - Main module for Tree Data Structure
# ----------------------------------------------------
#
# March 2022, Tempy Charoenvasnadumrong
#
# ----------------------------------------------------

""" Main module for tree data structure """


class Node:
    """Node for a tree"""

    def __init__(self, value) -> None:
        """A node constructor"""
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary search tree class"""

    def __init__(self) -> None:
        """Creaters an empty tree"""
        self.root = None
        # NOTE - not keeping track of the length!

    def insert(self, value) -> None:
        """Insert a node into a binary search tree"""
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        temp_node = self.root
        while True:
            if new_node == temp_node.value:
                # A duplicate cannot be analysed in a tree
                return
            if new_node.value < temp_node.value:
                if temp_node.left is None:
                    temp_node.left = new_node
                    return
                temp_node = temp_node.left
            else:
                if temp_node.right is None:
                    temp_node.right = new_node
                    return
                temp_node = temp_node.right

    def contains(self, value) -> bool:
        """Check if the value is in the tree."""

        temp_node = self.root
        while temp_node is not None:

            if value < temp_node.value:
                temp_node = temp_node.left
            elif value > temp_node.value:
                temp_node = temp_node.right
            else:
                return True
        return False

    def min_value(self, current_node) -> Node:
        """Get the node with the minimum value from the specified node"""
        temp_node = current_node

        while temp_node.left is not None:
            temp_node = temp_node.left
        return temp_node


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(4)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.right.right.value)
print(my_tree.contains(5))

print(my_tree.min_value(my_tree.root.right).value)
