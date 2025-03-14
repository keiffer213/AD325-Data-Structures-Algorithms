# AVL Tree Implementation and Testing

## Overview
This project involves implementing a **self-balancing AVL Tree** in Python. The AVL Tree is an enhanced **Binary Search Tree (BST)** that maintains a balanced structure using **rotations** to ensure optimal search, insertion, and deletion performance.

Additionally, a **unit testing suite** using `unittest` is included to verify the correctness of each operation within the AVL Tree.

## Objectives
- Implement an **AVL Tree** that supports:
  - Insertion
  - Deletion
  - Searching
  - In-order traversal
- Ensure the tree remains balanced through **rotations**.
- Write **unit tests** to validate AVL tree operations.
- Test the behavior of the AVL tree under various conditions.

## Features
- **TreeNode Class**:
  - Stores node value, left/right children, and height.
  - Provides methods for getting balance factor and updating height.
- **AVLTree Class**:
  - `insert(value)`: Inserts a value into the tree and balances it.
  - `delete(value)`: Deletes a value and balances the tree.
  - `search(value)`: Searches for a value in the tree.
  - `in_order_traversal()`: Retrieves elements in sorted order.
  - `min_value_node(node)`: Finds the smallest node in a subtree.
  - `_rotate_left(node)`, `_rotate_right(node)`: Performs AVL rotations.
- **Helper Function**:
  - `construct_avl(values)`: Builds an AVL tree from a list of values.

## File Structure
```
.
├── AVL_Tree_Keiffer.py    # AVL Tree Implementation
├── AVL_Tree_Tests.py      # Unit tests using unittest
├── README.md              # Documentation
```

## Installation and Setup
Ensure you have **Python 3.x** installed.

1. Clone this repository or download the files:
   ```sh
   git clone https://github.com/your-repo/AVL-Tree.git
   cd AVL-Tree
   ```
2. Run the AVL tree script:
   ```sh
   python AVL_Tree_Keiffer.py
   ```
3. Run the test suite:
   ```sh
   python -m unittest AVL_Tree_Tests.py
   ```

## Example Usage
```python
from AVL_Tree_Keiffer import AVLTree

# Create an AVL Tree instance
avl = AVLTree()

# Insert values
avl.insert(10)
avl.insert(20)
avl.insert(30)

# Search for a value
print(avl.search(10))  # Output: True
print(avl.search(5))   # Output: False

# Perform in-order traversal
print(avl.in_order_traversal())  # Output: [10, 20, 30]

# Delete a node
avl.delete(20)
print(avl.in_order_traversal())  # Output: [10, 30]
```

## Testing
The project includes a test suite (`AVL_Tree_Tests.py`) to verify AVL tree operations. The test cases include:
- **Insertion Tests**: Checks if values are correctly inserted and if rotations occur as needed.
- **Searching Tests**: Ensures the tree correctly finds existing and non-existing values.
- **Deletion Tests**: Tests deletion of leaf nodes, nodes with one child, and nodes with two children.
- **Balancing Tests**: Ensures tree remains balanced after operations.
- **Large-scale Insertion Tests**: Tests tree performance with large data sets.

To run the tests:
```sh
python -m unittest AVL_Tree_Tests.py
```

## Author
**Keiffer Tan**

## License
This project is licensed under the MIT License.

