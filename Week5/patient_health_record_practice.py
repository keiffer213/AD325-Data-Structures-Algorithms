from collections import deque

class HealthRecordNode:
  def __init__(self, date, heart_rate):
    self.date = date
    self.heart_rate = heart_rate
    self.next = None

  def __str__(self):
    return f"Date: {self.date}, Heart Rate: {self.heart_rate}"

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

  # Rather than storing length manually, best to dynammy retrieve the length of the linked list

def is_health_record_symmetric(health_record):
  # For even lists
  stack = deque()
  pointer = health_record.head

  for _ in range(health_record.length//2):
    stack.append(pointer.heart_rate)
    pointer = pointer.next
  
  if health_record.length % 2 == 1:
    pointer = pointer.next

  while pointer is not None:
    hr = stack.pop()
    if hr != pointer.heart_rate:
      return False
    pointer = pointer.next
    
  return True



if __name__=="__main__":
  heart_rate_1 = HealthRecordNode("1/24/24", 125)
  heart_rate_2 = HealthRecordNode("1/25/24", 115)
  heart_rate_3 = HealthRecordNode("1/26/24", 132)
  heart_rate_4 = HealthRecordNode("1/27/24", 119)
  heart_rate_5 = HealthRecordNode("1/28/24", 105)
  heart_rate_6 = HealthRecordNode("1/29/24", 110)

  keiffer_record = SinglyLinkedList(heart_rate_1)
  keiffer_record.append(heart_rate_2)
  keiffer_record.append(heart_rate_3)
  keiffer_record.append(heart_rate_4)
  keiffer_record.append(heart_rate_5)
  keiffer_record.append(heart_rate_6)

  record = keiffer_record.head
  for _ in range(keiffer_record.length):
    print(record)
    record = record.next

  print("Keiffer: ",is_health_record_symmetric(keiffer_record))

  heart_rate_1 = HealthRecordNode("1/24/24", 125)
  heart_rate_2 = HealthRecordNode("1/25/24", 115)
  heart_rate_3 = HealthRecordNode("1/26/24", 105)
  heart_rate_4 = HealthRecordNode("1/27/24", 105)
  heart_rate_5 = HealthRecordNode("1/28/24", 115)
  heart_rate_6 = HealthRecordNode("1/29/24", 125)

  kat_record = SinglyLinkedList(heart_rate_1)
  kat_record.append(heart_rate_2)
  kat_record.append(heart_rate_3)
  kat_record.append(heart_rate_4)
  kat_record.append(heart_rate_5)
  kat_record.append(heart_rate_6)

  print("Kat: ", is_health_record_symmetric(kat_record))


# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement