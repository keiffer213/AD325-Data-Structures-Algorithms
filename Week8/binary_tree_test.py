import unittest
from binary_tree_keiffer import TreeNode, BinaryTree, construct_tree

class TestSelectionSort(unittest.TestCase):

  def setUp(self):
    """
    setup for each test
    """
    self.tree = construct_tree(10)
    self.tree2 = construct_tree(0)
    self.tree3 = construct_tree(1000)

  def test_TreeNode(self):
    """
    test for TreeNode creationg
    """
    node = TreeNode(0)
    self.assertEqual(node.value, 0)
    self.assertEqual(node.left, None)
    self.assertEqual(node.right, None)

  def test_BinaryTree_initialize(self):
    """
    test for binary tree initialization
    """
    tree = BinaryTree()
    self.assertEqual(tree.root, None)
    self.assertEqual(tree.get_depth(), 0)

    tree = BinaryTree(TreeNode(0))
    self.assertEqual(tree.root.value, 0)
    self.assertEqual(tree.get_depth(), 1)

  def test_add_node(self):
    """
    test for adding a node to the binary tree
    """
    tree = BinaryTree()
    tree.add_node(0)
    self.assertEqual(tree.root.value, 0)
    self.assertEqual(tree.get_depth(), 1)

    tree.add_node(1)
    self.assertEqual(tree.root.left.value, 1)
    self.assertEqual(tree.get_depth(), 2)

    tree.add_node(2)
    self.assertEqual(tree.root.right.value, 2)
    self.assertEqual(tree.get_depth(), 2)

    tree.add_node(3)
    self.assertEqual(tree.root.left.left.value, 3)
    self.assertEqual(tree.get_depth(), 3)

    tree.add_node(4)
    self.assertEqual(tree.root.left.right.value, 4)

  def test_construct_tree(self):
    """
    test for tree construction
    """
    self.assertEqual(self.tree.root.value, 0)
    self.assertEqual(self.tree.root.left.value, 1)
    self.assertEqual(self.tree.root.right.value, 2)
    self.assertEqual(self.tree.root.left.left.value, 3)
    self.assertEqual(self.tree.root.left.right.value, 4)
    self.assertEqual(self.tree.root.right.left.value, 5)
    self.assertEqual(self.tree.root.right.right.value, 6)
    self.assertEqual(self.tree.root.left.left.left.value, 7)
    self.assertEqual(self.tree.root.left.left.right.value, 8)
    self.assertEqual(self.tree.root.left.right.left.value, 9)
    self.assertEqual(self.tree.get_depth(), 4)

    self.assertEqual(self.tree2.root, None)
    self.assertEqual(self.tree2.get_depth(), 0)

    self.assertEqual(self.tree3.root.value, 0)
    self.assertEqual(self.tree3.get_depth(), 10)

                #             0
                #           /   \
                #         1       2
                #       /  \     /  \
                #     3     4   5    6
                #   /\    / 
                #  7  8  9  

  def test_preorder_traversal(self):
    """Pre-order traversal: Visit the root, then the left subtree, then the right subtree"""
    self.assertEqual(self.tree.preorder_traversal(), [0, 1, 3, 7, 8, 4, 9, 2, 5, 6])
    self.assertEqual(self.tree2.preorder_traversal(), [])

  def test_inorder_traversal(self):
    """In-order traversal: Visit the left subtree, then the root, then the right subtree"""
    self.assertEqual(self.tree.inorder_traversal(), [7, 3, 8, 1, 9, 4, 0, 5, 2, 6])
    self.assertEqual(self.tree2.inorder_traversal(), [])

  def test_postorder_traversal(self):
    """Post-order traversal: Visit the left subtree, then the right subtree, then the root"""
    self.assertEqual(self.tree.postorder_traversal(), [7, 8, 3, 9, 4, 1, 5, 6, 2, 0])
    self.assertEqual(self.tree2.postorder_traversal(), [])

  def test_levelorder_traversal(self):
    """Level-order traversal: Visit the nodes from left to right at each level"""
    self.assertEqual(self.tree.levelorder_traversal(self.tree.root), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    self.assertEqual(self.tree2.levelorder_traversal(self.tree2.root), [])

  



if __name__ == "__main__":
  unittest.main()