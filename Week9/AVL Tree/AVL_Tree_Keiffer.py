
"""
By: Keiffer Tan
Assignment: Implementing and Testing AVL Tree

Objective:
Implement the AVL Tree data structure in Python or Java. Your implementation should support insertion, deletion, and search operations. After completing the implementation, you will also need to create test cases to ensure your AVL Tree handles various scenarios and edge cases efficiently and correctly.

"""

class TreeNode:
  """
  A node in an AVL tree.
  
  :param value: The value of the node
  :param left: The left child of the node
  :param right: The right child of the node
  """
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    self.height = 1

  def update_height(self):
    """
    Updates the height of a node in the tree.
    """
    self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

  @staticmethod
  def get_height(node):
    """
    Gets the height of a node in the tree.
    
    :param node: The node to get the height of
    :return: The height of the node
    """
    if not node:
      return 0
    return node.height

  def get_balance(self):
    """
    Gets the balance factor of a node in the tree.
    
    :param node: The node to get the balance factor of
    :return: The balance factor of the node
    """
    return self.get_height(self.left) - self.get_height(self.right)

class AVLTree:
  """
  An AVL Tree implementation.
  
  :param root: The root node of the tree if it exists
  """
  def __init__(self, root=None):
    """
    Initializes a new binary search tree.
    
    :param root: The root node of the tree if it exists
    """
    self.root = root


  def insert(self, value):
    """
    Inserts a value into the binary search tree.
    
    :param value: The value to insert
    """
    self.root = self._insert(self.root, value)

  def _insert(self, node, value):
    if node is None:
      return TreeNode(value)
    
    if value < node.value:
      node.left = self._insert(node.left, value)
    else:
      node.right = self._insert(node.right, value)

    node.update_height()
    balance = node.get_balance()

    # Left Left Case
    if balance > 1 and value < node.left.value:
      return self._rotate_right(node)

    # Right Right Case
    if balance < -1 and value > node.right.value:
      return self._rotate_left(node)

    # Left Right Case
    if balance > 1 and value > node.left.value:
      node.left = self._rotate_left(node.left)
      return self._rotate_right(node)

    # Right Left Case
    if balance < -1 and value < node.right.value:
      node.right = self._rotate_right(node.right)
      return self._rotate_left(node)

    return node


  def delete(self, value):
    """
    Deletes a value from the binary search tree.
    
    :param value: The value to delete
    """
    self.root = self._delete(self.root, value)

  def _delete(self, node, value):
    if node is None:
      return node
    
    # if value is less than node value, go left
    if value < node.value:
      node.left = self._delete(node.left, value)

    # if value is greater than node value, go right
    elif value > node.value:
      node.right = self._delete(node.right, value)
    
    # if value is same as node value, delete node
    else:
      if not node.left:
        return node.right
      elif not node.right:
        return node.left
      
      temp = self.min_value_node(node.right)
      node.value = temp.value
      node.right = self._delete(node.right, temp.value)

    node.update_height()
    balance = node.get_balance()

    # Balancing the node
    # Left Left Case
    if balance > 1 and node.left.get_balance() >= 0:
      return self._rotate_right(node)

    # Right Right Case
    if balance < -1 and node.right.get_balance() <= 0:
      return self._rotate_left(node)

    # Left Right Case
    if balance > 1 and node.left.get_balance() < 0:
      node.left = self._rotate_left(node.left)
      return self._rotate_right(node)

    # Right Left Case
    if balance < -1 and node.right.get_balance() > 0:
      node.right = self._rotate_right(node.right)
      return self._rotate_left(node)

    return node

  def min_value_node(self, node):
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


  def in_order_traversal(self):
    """
    Performs an in-order traversal of the binary search tree.
    
    :return: A list of values in the binary search tree in in-order traversal order
    """
    result = []
    self._in_order_traversal(self.root, result)
    return result

  def _in_order_traversal(self, node, result):
    if node is not None:
      self._in_order_traversal(node.left, result)
      result.append(node.value)
      self._in_order_traversal(node.right, result)

  def _rotate_left(self, node):
    """
    Rotates a node to the left in the tree.
    
    :param node: The node to rotate
    :return: The new root of the tree
    """
    y = node.right
    T2 = y.left
    y.left = node
    node.right = T2
    node.update_height()
    y.update_height()
    return y

  def _rotate_right(self, node):
    """
    Rotates a node to the right in the tree.
    
    :param node: The node to rotate
    :return: The new root of the tree
    """
    x = node.left
    T2 = x.right
    x.right = node
    node.left = T2
    node.update_height()
    x.update_height()
    return x



def construct_avl(values):
  """
  Constructs an AVL tree from a list of values.

  :param values: A list of values to insert into the AVL tree
  :return: An AVL tree with the given values
  """
  tree = AVLTree()
  for value in values:
    tree.insert(value)
  return tree


if __name__ == "__main__": 
  vals = [4, 2, 6, 1, 3, 5, 7, 9, 2]
  tree = construct_avl(vals)

  print(tree.in_order_traversal())
  tree.delete(4)
  print(tree.in_order_traversal())
