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
    else: 
      current = self.head
      while current.next is not None:
        current = current.next

      current.next = node
    self.length += 1


def is_health_record_symmetric(health_record):
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


records_non_symmetric = [
  HealthRecordNode("1/24/24", 125),
  HealthRecordNode("1/25/24", 115),
  HealthRecordNode("1/26/24", 132), 
  HealthRecordNode("1/27/24", 119),
  HealthRecordNode("1/28/24", 105),
  HealthRecordNode("1/29/24", 110),
]

records_symmetric = [
  HealthRecordNode("1/24/24", 125),
  HealthRecordNode("1/25/24", 115),
  HealthRecordNode("1/26/24", 110),
  HealthRecordNode("1/27/24", 110),
  HealthRecordNode("1/28/24", 115),
  HealthRecordNode("1/29/24", 125),
]

if __name__=="__main__":
  health_record = SinglyLinkedList()
  for record in records_symmetric:
    health_record.append(record)

  current = health_record.head
  for _ in range(health_record.length):
    print(current)
    current = current.next

  print(is_health_record_symmetric(health_record))

# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement