# Binary Search Tree (BST) Implementation and Testing

## Overview
This project involves implementing a **Binary Search Tree (BST)** in Python. The BST supports fundamental operations such as:
- **Insertion** of elements
- **Searching** for an element
- **Deletion** of elements
- **In-order traversal** to retrieve elements in ascending order

Additionally, a **unit testing suite** using `unittest` is included to verify the correctness of each operation within the BST.

## Objectives
- Implement a **Binary Search Tree (BST)** with fundamental operations.
- Write **unit tests** to validate the correctness of the BST implementation.
- Gain experience in **data structures**, **debugging**, and **testing**.

## Features
- **TreeNode Class**: Represents individual nodes in the BST.
- **BinarySearchTree Class**:
  - `insert(value)`: Inserts a new value into the BST.
  - `search(value)`: Searches for a value in the BST.
  - `delete(value)`: Deletes a specified value from the BST.
  - `inorder_traversal()`: Returns the elements in ascending order.
  - `minValueNode(node)`: Finds the minimum value node in a subtree.
- **Helper Function**:
  - `construct_bst(values)`: Builds a BST from a list of values.

## File Structure
```
.
├── BST_keiffer.py      # BST Implementation
├── test_BST.py         # Unit tests using unittest
├── README.md           # Documentation
```

## Installation and Setup
Ensure you have **Python 3.x** installed.

1. Clone this repository or download the files:
   ```sh
   git clone https://github.com/your-repo/BST-implementation.git
   cd BST-implementation
   ```
2. Run the BST script:
   ```sh
   python BST_keiffer.py
   ```
3. Run the test suite:
   ```sh
   python -m unittest test_BST.py
   ```

## Example Usage
```python
from BST_keiffer import BinarySearchTree

# Create a BST instance
bst = BinarySearchTree()

# Insert values
bst.insert(10)
bst.insert(5)
bst.insert(15)

# Search for a value
print(bst.search(10))  # Output: True
print(bst.search(7))   # Output: False

# Perform in-order traversal
print(bst.inorder_traversal())  # Output: [5, 10, 15]

# Delete a node
bst.delete(10)
print(bst.inorder_traversal())  # Output: [5, 15]
```

## Testing
The project includes a test suite (`test_BST.py`) to verify BST operations. The test cases include:
- **Insertion**: Checks if values are correctly inserted.
- **Searching**: Ensures values exist or do not exist in the tree.
- **Deletion**: Validates proper removal of elements.
- **Minimum Node**: Confirms the correct smallest node is found.
- **BST Construction**: Ensures correct tree formation from a list.

To run the tests:
```sh
python -m unittest test_BST.py
```

## Author
**Keiffer Tan**

## License
This project is licensed under the MIT License.

