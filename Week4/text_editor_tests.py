import unittest
from text_editor_keiffer import *

class TestTextOperation(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of TextOperation for each test."""
        self.editor = TextOperation()

    def test_add_single_character(self):
        """Test adding a valid single character."""
        self.editor.add_char('a')
        self.assertEqual(self.editor.text, 'a')
        self.assertEqual(len(self.editor.undo_stack), 1)
        self.assertEqual(self.editor.undo_stack[-1].op_type, "add")
        self.assertEqual(self.editor.undo_stack[-1].char, 'a')

    def test_add_invalid_character(self):
        """Test adding an invalid character (e.g., multiple characters or empty input)."""
        with self.assertRaises(ValueError):
            self.editor.add_char("ab")  # Invalid input: multiple characters

        with self.assertRaises(ValueError):
            self.editor.add_char("")  # Invalid input: empty string

        self.assertEqual(self.editor.text, "")  # Ensure text remains unchanged
        self.assertEqual(len(self.editor.undo_stack), 0)  # Ensure undo stack is unchanged

    def test_undo_after_add(self):
        """Test undoing a single add operation."""
        self.editor.add_char('a')
        self.assertEqual(self.editor.text, 'a')
        self.editor.undo_action()
        self.assertEqual(self.editor.text, '')  # Undo should remove the added character
        self.assertEqual(len(self.editor.undo_stack), 0)  # Undo stack should be empty

    def test_undo_after_delete(self):
        """Test undoing a delete operation."""
        self.editor.add_char('a')
        self.editor.add_char('b')
        self.editor.delete_char()
        self.assertEqual(self.editor.text, 'a')  # Text after delete
        self.editor.undo_action()
        self.assertEqual(self.editor.text, 'ab')  # Text restored after undo
        self.assertEqual(len(self.editor.undo_stack), 2)  # Undo stack should reflect previous add

if __name__ == "__main__":
  unittest.main()