
"""
By: Keiffer Tan
Assignment: Implementing and Testing a Binsary Search Tree

Overview
In this assignment, you will implement a Binary Search Tree (BST) in either Python or Java. Additionally, you'll create test cases to verify the correctness of each operation within your BST. This exercise will not only enhance your understanding of BST operations but also emphasize the importance of testing in software development.

Objectives
  - To implement the fundamental operations of a BST: insertion, search, and deletion.
  - To write test cases that validate the functionality and robustness of your BST implementation.
  - To develop skills in debugging and testing within a programming context.

"""

class TreeNode:
  """
  A node in a binary search tree.
  
  :param value: The value of the node
  """
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  """
  A binary search tree implementation.
  """
  def __init__(self, root=None):
    """
    Initializes a new binary search tree.

    :param root: The root node of the tree if it exists
    """
    self.root = root

  def search(self, value):
    """
    Searches for a value in the binary search tree.

    :param value: The value to search for
    :return: True if the value is found, False otherwise
    """
    return self._search(self.root, value)

  def _search(self, node, value):
    # Base Cases
    if node is None:
      return False
    elif node.value == value:
      return True
    
    # Recursive Cases
    # go down the tree until the value is found
    elif value < node.value:
      return self._search(node.left, value)
    else:
      return self._search(node.right, value)

  def insert(self, value):
    """
    Inserts a value into the binary search tree.

    :param value: The value to insert
    """

    # if the tree is empty, insert the value as the root
    if self.root is None:
      self.root = TreeNode(value)
    # else insert the value into the tree
    else:
      self._insert(self.root, value)

  def _insert(self, node, value):
    # if the value is less than the node value, go left
    if value < node.value:
      if node.left is None:
        node.left = TreeNode(value)
      else:
        self._insert(node.left, value)

    # if the value is greater than the node value, go right
    else:
      if node.right is None:
        node.right = TreeNode(value)
      else:
        self._insert(node.right, value)

  def delete(self, value):
    """
    Deletes a value from the binary search tree.

    :param value: The value to delete
    """
    self._delete(self.root, value)

  def _delete(self, node, value):
    # Base Case
    if node is None:
      return None

    # if value is less than node value, go left
    elif value < node.value:
      node.left = self._delete(node.left, value)

    # if value is greater than node value, go right
    elif value > node.value:
      node.right = self._delete(node.right, value)

    # if value is same as node value, delete node
    else:
      # Node with only one child or no child
      if node.left is None:
        temp = node.right
        node = None
        return temp

      elif node.right is None:  
        temp = node.left
        node = None
        return temp

      # Node with two children: Get the inorder successor (smallest in the right subtree)
      temp = self.minValueNode(node.right)

      # Copy the inorder successor's content to this node
      node.value = temp.value

      # Delete the inorder successor
      node.right = self._delete(node.right, temp.value)

    return node
      
  def minValueNode(self, node):
    """
    Finds the minimum value node in the binary search tree.

    :param node: The current node in the traversal
    :return: The minimum value node in the binary search tree
    """
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
      current = current.left

    return current

  def inorder_traversal(self):
    """
    Performs an in-order traversal of the binary search tree.

    :return: A list of values in the binary search tree in in-order traversal order
    """
    result = []
    self._inorder_traversal(self.root, result)
    return result

  def _inorder_traversal(self, node, result):
    if node is not None:
      self._inorder_traversal(node.left, result)
      result.append(node.value)
      self._inorder_traversal(node.right, result)


def construct_bst(values):
  """
  Constructs a binary search tree from a list of values.

  :param values: A list of values to insert into the binary search tree
  :return: A binary search tree with the given values
  """
  tree = BinarySearchTree()
  for value in values:
    tree.insert(value)
  return tree

if __name__ == "__main__":
  vals = [4, 2, 6, 1, 3, 5, 7, 9, 2]
  tree = construct_bst(vals)

  print(tree.inorder_traversal())
  tree.delete(4)
  print(tree.inorder_traversal())

