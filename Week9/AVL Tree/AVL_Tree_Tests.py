import unittest
from AVL_Tree_Keiffer import AVLTree, construct_avl, TreeNode

class TestAVLTree(unittest.TestCase):

  def setUp(self):
    """
    setup for each test
    """
    self.tree = AVLTree()
    self.vals = [4, 8, 6, 1, 3, 5, 7, 9, 2]

  def test_insert(self):
    """
    test for adding a node to the binary tree

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for val in self.vals:
      self.tree.insert(val)

    node = self.tree.root
    self.assertEqual(node.value, 4)
    self.assertEqual(node.left.value, 2)
    self.assertEqual(node.right.value, 6)
    self.assertEqual(node.left.left.value, 1)
    self.assertEqual(node.left.right.value, 3)
    self.assertEqual(node.right.left.value, 5)
    self.assertEqual(node.right.right.value, 8)
    self.assertEqual(node.right.right.left.value, 7)
    self.assertEqual(node.right.right.right.value, 9)

  def test_search(self):  
    """
    test for searching for a value in the binary tree
    """
    val = [5, 6, 12, 52, 5, 1]
    for v in val:
      self.tree.insert(v)

    self.assertTrue(self.tree.search(5))
    self.assertTrue(self.tree.search(6))
    self.assertTrue(self.tree.search(12))
    self.assertTrue(self.tree.search(52))
    self.assertTrue(self.tree.search(5))
    self.assertTrue(self.tree.search(1))
    self.assertFalse(self.tree.search(0))
    self.assertFalse(self.tree.search(7))

  def test_delete(self):
    """
    test for deleting a node from the binary tree
    """
    for val in self.vals:
      self.tree.insert(val)

    self.tree.delete(4)
    self.assertFalse(self.tree.search(4))

    self.tree.delete(1)
    self.assertFalse(self.tree.search(1))

    self.tree.delete(9)
    self.assertFalse(self.tree.search(9))

    self.assertTrue(self.tree.search(2))
    self.assertTrue(self.tree.search(6))
    self.assertTrue(self.tree.search(3))
    self.assertTrue(self.tree.search(5))
    self.assertTrue(self.tree.search(7))
    self.assertTrue(self.tree.search(8))

    self.tree.delete(8)
    self.assertFalse(self.tree.search(8))

  def test_min_val_node(self):
    """
    test for finding the minimum value node in the binary tree
    """
    vals = [21, 15, 10, 30, 25, 22, 35, 5, 20]
    for val in vals:
      self.tree.insert(val)

    self.assertEqual(self.tree.min_value_node(self.tree.root).value, 5)

  def test_construct_avl(self):
    """
    test for constructing a binary search tree from a list of values
    """
    tree = construct_avl(self.vals)
    self.assertEqual(tree.root.value, 4)
    self.assertEqual(tree.root.left.value, 2)
    self.assertEqual(tree.root.right.value, 6)
    self.assertEqual(tree.root.left.left.value, 1)
    self.assertEqual(tree.root.left.right.value, 3)
    self.assertEqual(tree.root.right.left.value, 5)
    self.assertEqual(tree.root.right.right.value, 8)
    self.assertEqual(tree.root.right.right.left.value, 7)
    self.assertEqual(tree.root.right.right.right.value, 9)

  def test_balance_after_insert(self):
    """
    test for balancing the tree after inserting a node
    """
    vals = [10, 20, 30, 40, 50, 25]  # Forces rotations
    for val in vals:
        self.tree.insert(val)

    self.assertTrue(-1 <= self.tree.root.get_balance() <= 1)

  def test_delete_node_with_one_child(self):
    """
    test for deleting a node with one child

             20
           /   \
          10    30
            \   / 
             15 25

    """
    vals = [20, 10, 30, 25, 15]
    for val in vals:
        self.tree.insert(val)
    
    # check where each number is
    self.assertEqual(self.tree.root.value, 20)
    self.assertEqual(self.tree.root.left.value, 10)
    self.assertEqual(self.tree.root.left.right.value, 15)
    self.assertEqual(self.tree.root.right.value, 30)
    self.assertEqual(self.tree.root.right.left.value, 25)

    self.tree.delete(30)
    self.assertTrue(self.tree.search(10))
    self.assertFalse(self.tree.search(30)) # check 30 was deleted and 
    self.assertEqual(self.tree.root.value, 20)
    self.assertEqual(self.tree.root.right.value, 25) # check 25 is the right child of the root

  def test_delete_node_with_two_children(self):
    """
    test for deleting a node with two children

            20
          /   \
        10    30
          \   / \
            15 25 35

    """
    vals = [20, 10, 30, 25, 15, 35]
    for val in vals:
      self.tree.insert(val)

    # check where each number is
    self.assertEqual(self.tree.root.value, 20)
    self.assertEqual(self.tree.root.left.value, 10)
    self.assertEqual(self.tree.root.left.right.value, 15)
    self.assertEqual(self.tree.root.right.value, 30)
    self.assertEqual(self.tree.root.right.left.value, 25)
    self.assertEqual(self.tree.root.right.right.value, 35)

    self.tree.delete(30)
    self.assertTrue(self.tree.search(10))
    self.assertFalse(self.tree.search(30)) # check 30 was deleted and 
    self.assertEqual(self.tree.root.value, 20)
    self.assertEqual(self.tree.root.right.value, 35) # check 35 is the right child of the root
    self.assertEqual(self.tree.root.right.left.value, 25)

  def test_large_scale_insertion(self):
    """
    test for inserting a large number of values into the binary tree
    """
    import random
    values = random.sample(range(1, 10000), 1000) # Insert 1000 random numbers
    for val in values:
      self.tree.insert(val)

    # check root is balanced
    self.assertTrue(-1 <= self.tree.root.get_balance() <= 1)


if __name__ == "__main__":
  unittest.main()