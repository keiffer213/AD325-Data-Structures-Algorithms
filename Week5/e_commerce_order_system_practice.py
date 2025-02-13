
class Order:
  def __init__(self, order_id, cust_id, order_details):
    self.order_id = order_id
    self.cust_id = cust_id
    self.order_details = order_details
    self.next = None

  def __str__(self):
    return f"Order ID: {self.order_id} \nCustomer ID: {self.cust_id} \nOrder Details: {self.order_details}"

class SinglyLinkedList:
  def __init__(self, head = None):
    self.head = head
    self.length = 1 if head else 0

  def append(self, node):
    if self.head is None:
      self.head = node
      self.length = 1
      return

    last_node = self.head

    while last_node.next is not None:
      last_node = last_node.next

    last_node.next = node
    self.length += 1

  def reverse(self):
    prev = None
    current = self.head

    while current is not None:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node

    self.head = prev


  def display(self):
    display_pointer = self.head

    while display_pointer is not None:
      print(display_pointer)
      display_pointer = display_pointer.next

  # def delete_node(self, index):
  #   if index <= 0 or index > self.length:
  #     print("Invalid node to delete")
  #     return

  #   elif index == 1:
  #     if self.length == 1:
  #       self.head = None
  #     else:
  #       self.head = self.head.next
  #   else:
  #     prev_node = self.head

  #     for _ in range(index-1):
  #       prev_node = prev_node.next
      
  #     target_node = prev_node.next

  #     if target_node.next == None:
  #       prev_node.next = None
  #     else:
  #       prev_node.next = target_node.next

  #     self.length -= 1


if __name__=="__main__":
  order_system = SinglyLinkedList()
  order_system.append(Order(1, 11, "A partridge in a pear tree"))
  order_system.append(Order(2, 22, "Two french hens"))
  order_system.append(Order(3, 33, "Three french hens"))
  order_system.append(Order(4, 44, "Four calling birds"))
  order_5 = Order(5, 55, "Five golden rings")
  order_system.append(order_5)

  order_system.display()

  order_system.reverse()
  order_system.display()

# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement