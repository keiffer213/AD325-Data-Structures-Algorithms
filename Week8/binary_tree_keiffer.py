from collections import deque


class TreeNode:
  """ 
  TreeNode class, represents a node in a binary tree 

  :param value: The value of the node
  """
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BinaryTree:
  """ 
  Binary Tree Class 
  Initialize a binary tree with the given node as the root, if there is one.

  :param node: The root of the binary tree
  """
  def __init__(self, node = None):
    self.root = node

  def add_node(self, value):
    """
    Adds a new node with the given value to the binary tree. 
    The node is added in a level-order manner, filling each level 
    from left to right. If the tree is empty, the new node becomes 
    the root of the tree.
    
    :param value: The value to be added to the tree.
    """

    new_node = TreeNode(value)

    # If the tree is empty, the new node becomes the root
    if not self.root:
      self.root = new_node
      return

    # Otherwise, the new node is added in a level-order manner
    queue = deque([self.root])
    while queue:
      node = queue.popleft()

      # Insert node as left node if left node is empty
      if not node.left:
        node.left = new_node
        return
      else:
         queue.append(node.left)

      # Insert node as right right now if left node exists and right node is empty
      if not node.right:
        node.right = new_node
        return
      else:
        queue.append(node.right)

  def get_depth(self):
    """
    Returns the depth of the binary tree
    """
    return self.__get_depth(self.root)
  
  def __get_depth(self, node):
    """
    Private method to find depth of the binary tree recursively
    """
    if not node:
      return 0
    return 1 + max(self.__get_depth(node.left), self.__get_depth(node.right))

  def preorder_traversal(self):
    """
    Traverses through the binary tree in pre-order fashion
    """
    result = []
    self.__pre_order_traversal(self.root, result)
    return result

  def __pre_order_traversal(self, node, result):
    """
    Private method to traverse through the binary tree in pre-order fashion
    Pre-order traversal: Visit the root, then the left subtree, then the right subtree

    :param node: The current node in the traversal
    :param result: A list to store the values of the nodes
    """
    if node:
      # print(node.value, end=' ')
      result.append(node.value)
      self.__pre_order_traversal(node.left, result)
      self.__pre_order_traversal(node.right, result)


  def inorder_traversal(self):
    """
    Traverses through the binary tree in in-order fashion
    """
    result = []
    self.__inorder_traversal(self.root, result)
    return result

  def __inorder_traversal(self, node, result):
    """
    Private method to traverse through the binary tree in in-order fashion
    In-order traversal: Visit the left subtree, then the root, then the right subtree
    
    :param node: The current node in the traversal
    :param result: A list to store the values of the nodes
    """
    if node:
      self.__inorder_traversal(node.left, result)
      # print(node.value, end=' ')
      result.append(node.value)
      self.__inorder_traversal(node.right, result)


  def postorder_traversal(self):
    """
    Traverse through the binary tree in post-order fashion
    """
    result = []
    self.__postorder_traversal(self.root, result)
    return result

  def __postorder_traversal(self, node, result):
    """
    Private method to traverse through the binary tree in post-order fashion
    Post-order traversal: Visit the left subtree, then the right subtree, then the root

    :param node: The current node in the traversal
    :param result: A list to store the values of the nodes
    """
    if node:
      self.__postorder_traversal(node.left, result)
      self.__postorder_traversal(node.right, result)
      # print(node.value, end=' ')
      result.append(node.value)


  def levelorder_traversal(self, node):
    """
    Traverses through the binary tree in level-order fashion
    Level-order traversal: Visit the nodes from left to right at each level

    :param node: The current node in the traversal
    """
    if not node:
      return []

    queue = deque([node])
    result = []

    while queue:
      current = queue.popleft()
      result.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

    return result


def construct_tree(size):
  """
  Function to construct a binary tree

  :param size: The size of the binary tree
  """
  tree = BinaryTree()
  for i in range(size):
    tree.add_node(i)
  return tree


if __name__ == "__main__":

  node1 = TreeNode(1)
  node2 = TreeNode(2)
  node3 = TreeNode(3)
  node4 = TreeNode(4)
  node5 = TreeNode(5)
  node6 = TreeNode(6)
  node7 = TreeNode(7)

  node1.left, node1.right = node2, node3
  node2.left, node2.right = node4, node5
  node3.left, node3.right = node6, node7

  btree = BinaryTree(node1)
  # print(btree.preorder_traversal())
  # print(btree.inorder_traversal())
  print(btree.postorder_traversal())


  node1 = TreeNode(1)
  node2 = TreeNode(2)
  node3 = TreeNode(3)
  node4 = TreeNode(4)
  node5 = TreeNode(5)
  node6 = TreeNode(6)
  node7 = TreeNode(7)

  node1.left, node1.right = node6, node7
  node6.left, node6.right = node3, node5
  node7.left, node7.right = node4, node2
  btree = BinaryTree(node1)

  print(btree.levelorder_traversal(btree.root))