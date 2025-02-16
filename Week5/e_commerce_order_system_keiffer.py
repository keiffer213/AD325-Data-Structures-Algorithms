




class Order:
  def __init__(self, order_id, customer_id, order_details):
    self.order_id = order_id
    self.customer_id = customer_id
    self.order_details = order_details
    self.next = None
  
  def __str__(self):
    return f"Order ID: {self.order_id} \nCustomer ID: {self.customer_id} \nOrder Details: {self.order_details}"

class SinglyLinkedList:
  def __init__(self, head = None):
    self.head = head
    self.length = 1 if head else 0

  def append(self, node):
    if self.head is None:
      self.head = node
    else:
      last_node = self.head

      while last_node.next is not None:
        last_node = last_node.next
      
      last_node.next = node
    self.length += 1

  def display(self):
    display_pointer = self.head

    while display_pointer is not None:
      print(display_pointer)
      display_pointer = display_pointer.next
    
  def reverse(self):
    prev = None
    current = self.head

    while current is not None:
      next_node = current.next
      current.next = prev
      prev = current 
      current = next_node
    self.head = prev


orders = [
  Order(1, 11, "A partridge in a pear tree"),
  Order(2, 22, "Two french hens"),
  Order(3, 33, "Three french hens"),
  Order(4, 44, "Four calling birds"),
  Order(5, 55, "Five golden rings"),
]

if __name__=="__main__":

  test_orders = SinglyLinkedList()
  for order in orders:
    test_orders.append(order)

  test_orders.display()
  test_orders.reverse()
  test_orders.display()


# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement