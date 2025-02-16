import unittest
from e_commerce_order_system_keiffer import Order, SinglyLinkedList

class TestOrderProcessing(unittest.TestCase):

  def setUp(self):
    self.order_system = SinglyLinkedList()
    self.orders = [
      Order(1, 11, "A partridge in a pear tree"),
      Order(2, 22, "Two french hens"),
      Order(3, 33, "Three french hens"),
      Order(4, 44, "Four calling birds"),
      Order(5, 55, "Five golden rings"),
    ]
    self.order1 = Order(1, 11, "A partridge in a pear tree")
    self.order2 = Order(2, 22, "Two french hens")
    self.order3 = Order(3, 33, "Three french hens")
    self.order4 = Order(4, 44, "Four calling birds")
    self.order5 = Order(5, 55, "Five golden rings")
  
  def test_append_orders(self):
    """Test Adding Orders to the linked list"""
    self.order_system.append(self.order1)
    self.order_system.append(self.order2)
    self.order_system.append(self.order3)

    # validate order
    self.assertEqual(self.order_system.head.order_id, 1)
    self.assertEqual(self.order_system.head.next.order_id, 2)
    self.assertEqual(self.order_system.head.next.next.order_id, 3)
    self.assertEqual(self.order_system.length, 3)
    
    self.order_system.append(self.order4)
    self.order_system.append(self.order5)
    self.assertEqual(self.order_system.head.next.next.next.order_id, 4)
    self.assertEqual(self.order_system.head.next.next.next.next.order_id, 5)
    self.assertEqual(self.order_system.length, 5)

  def test_reverse_orders(self):
    """Test reversing Orders to the linked list"""
    self.order_system.append(self.order1)
    self.order_system.append(self.order2)
    self.order_system.append(self.order3)

    self.order_system.reverse()

    self.assertEqual(self.order_system.head.order_id, 3)
    self.assertEqual(self.order_system.head.next.order_id, 2)
    self.assertEqual(self.order_system.head.next.next.order_id, 1)
    self.assertEqual(self.order_system.length, 3)

  def test_display_orders(self):
    """Test displaying Orders to the linked list"""
    self.order_system.append(self.order1)
    self.order_system.append(self.order2)
    self.order_system.append(self.order3)

    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output #Redirect the stdout from console to captured_output

    self.order_system.display()

    # Reseting stdout is important as subsequent tests may continue using StringIO
    sys.stdout = sys.__stdout__ #Reset stdout back to console (original value)
    output = captured_output.getvalue()
    self.assertIn("Order ID: 1", output)
    self.assertIn("Order ID: 2", output)
    self.assertIn("Order ID: 3", output)


if __name__ == "__main__":
  unittest.main()
