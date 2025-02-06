from collections import deque

# This class is an object type class
class OperationRecord:
  def __init__(self, char, op_type):
    self.char = char
    self.op_type = op_type


# Only one character will be modified (add, delete, undo) at one time/per method call
class TextOperation:
  def __init__(self):
    self.text = ""
    self.undo_stack = deque()

  # add a character to the text and add record to stack
  def add_char(self, char):
    if len(char) == 1:
      self.text += char
      self.undo_stack.append(OperationRecord(char, "add"))
    else:
      # print("The input must be a single character!")
      raise ValueError("Only a single character can be added at a time!")
  
  # Delete the last character and add record to stack
  def delete_char(self):
    if self.text:
      last_char = self.text[-1]
      self.undo_stack.append(OperationRecord(last_char, "delete"))
      self.text = self.text[:-1]
    else:
      print("No text to delete!")

  # Take the last record on the stack and undo the operation
  def undo_action(self):
    if self.undo_stack:
      last_action = self.undo_stack.pop()
      # text = "123"
      # undo_stack = [(1, "add"), (2, "add"), (3, "add")]
      # last_action = (3, "add")
      # undo -> text = "12"
      if last_action.op_type == "add":
        # We could possibly add a check to see if the last character matches the operation record
        self.text = self.text[:-1]
      # undo_stack = [(1, "add"), (2, "add"), (3, "add"), (3, "delete")]
      elif last_action.op_type == "delete":
        self.text += last_action.char
      else:
        print("Invalid undo operation from stack")
    else:
      print("No operation to undo")
  
  # Run the program, ask user for action, then execute the action, and display current state of text
  # Repeat until user exits from program
  def run(self):
    while True:
      print(f"Current Text: '{self.text}'")

      input_text = input("What operation would you like to do? add (a), delete (d), undo (u), exit(e)\t")
      if input_text == 'a':
        while True:
          add_c = input("What character would you like to add: ")
          if len(add_c) == 1:
            self.add_char(add_c)
            break
          else:
            print("Invalid input! Please type 1 character!")
      elif input_text == 'd':
        self.delete_char()
      elif input_text == 'u':
        self.undo_action()
      elif input_text == 'e':
        break
      else:
        print("Please enter a valid operation!")
      
      


if __name__ == "__main__":
  text_editor = TextOperation()
  text_editor.run()


# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement