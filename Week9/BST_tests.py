import unittest
from BST_keiffer import BinarySearchTree, construct_bst, TreeNode

class TestBinarySearchTree(unittest.TestCase):

  def setUp(self):
    """
    setup for each test
    """
    self.tree = BinarySearchTree()
    self.vals = [4, 2, 6, 1, 3, 5, 7, 9, 2]

  def test_insert(self):
    """
    test for adding a node to the binary tree
    """
    for val in self.vals:
      self.tree.insert(val)

    node = self.tree.root
    self.assertEqual(node.value, 4)
    self.assertEqual(node.left.value, 2)
    self.assertEqual(node.right.value, 6)
    self.assertEqual(node.left.left.value, 1)
    self.assertEqual(node.left.right.value, 3)
    self.assertEqual(node.left.right.left.value, 2)
    self.assertEqual(node.right.left.value, 5)
    self.assertEqual(node.right.right.value, 7)
    self.assertEqual(node.right.right.right.value, 9)

  def test_search(self):
    """
    test for searching for a value in the binary tree
    """
    for val in self.vals:
      self.tree.insert(val)

    self.assertTrue(self.tree.search(4))
    self.assertTrue(self.tree.search(2))
    self.assertTrue(self.tree.search(6))
    self.assertTrue(self.tree.search(1))
    self.assertTrue(self.tree.search(3))
    self.assertTrue(self.tree.search(5))
    self.assertTrue(self.tree.search(7))
    self.assertTrue(self.tree.search(9))
    self.assertFalse(self.tree.search(8))
    self.assertFalse(self.tree.search(0))

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

  def test_minValueNode(self):
    """
    test for finding the minimum value node in the binary tree
    """
    vals = [21, 15, 10, 30, 25, 22, 35, 5, 20]
    for val in vals:
      self.tree.insert(val)

    self.assertEqual(self.tree.minValueNode(self.tree.root).value, 5)

  def test_construct_bst(self):
    """
    test for constructing a binary search tree from a list of values
    """
    tree = construct_bst(self.vals)
    self.assertEqual(tree.root.value, 4)
    self.assertEqual(tree.root.left.value, 2)
    self.assertEqual(tree.root.right.value, 6)
    self.assertEqual(tree.root.left.left.value, 1)
    self.assertEqual(tree.root.left.right.value, 3)
    self.assertEqual(tree.root.left.right.left.value, 2)
    self.assertEqual(tree.root.right.left.value, 5)
    self.assertEqual(tree.root.right.right.value, 7)
    self.assertEqual(tree.root.right.right.right.value, 9)
      


if __name__ == "__main__":
  unittest.main()