from collections import deque

class Operation:
  def __init__(self, op_type, char):
   self.op_type = op_type
   self.char = char

class TextOperation:
  def __init__(self):
    self.text = ""
    self.undo_stack = deque()

  # Add a character
  def add_char(self, char):
    if len(char) == 1:
      self.text += char
      self.undo_stack.append(Operation("add", char))
    else: 
      raise ValueError("Only a single character can be added at a time.")

  # Remove character and add it to the undo_stack
  def delete_char(self):
    if self.text:
      self.undo_stack.append(Operation(("delete"), self.text[-1]))
      self.text = self.text[:-1]
    else:
      print("Nothing to delete!")

  # Undo the delete operation
  def undo_action(self):
    if self.undo_stack:
      last_operation = self.undo_stack.pop()
      if last_operation.op_type == "add":
        self.text = self.text[:-1]
      elif last_operation.op_type == "delete":
        self.text += last_operation.char
    else:
      print("Nothing to undo!")
  
  def run(self):
    while True:
      print(f"Currenty Text: '{self.text}'")

      input_text = input("What operation would you like to do? add (a), delete (d), undo (u), exit (e)\t")
      if input_text == 'a':
        while True:
          add_char = input("Type the char you would like to add: ")
          if len(add_char) == 1:
            self.add_char(add_char)
            break
          else:
            print("Invalid input. Please enter exactly one character.")
      elif input_text == 'd':
        self.delete_char()
      elif input_text == 'u':
        self.undo_action()
      elif input_text == 'e':
        print("Exiting Editor.")
        break
      else:
        print("Unkown input, please try again!")
      
      


if __name__=="__main__":
  text_editor = TextOperation()
  text_editor.run()

