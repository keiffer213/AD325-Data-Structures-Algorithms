from collections import deque

class PatientRecord:
  def __init__(self, patient_name, patient_id, age, ssn):
    self.patient_name = patient_name
    self.patient_id = patient_id
    self.age = age
    self.ssn = ssn
    self.next = None
    self.prev = None

  def __str__(self):
    return f"Patient ID: {self.patient_id} \tPatient Name: {self.patient_name} \nAge: {self.age} \nSSN: {self.ssn}"

class DoublyLinkedList:
  def __init__(self, head = None):
    self.head = head
    self.tail = head
    self.length = 1 if head else 0

  def append(self, node):
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
    self.length += 1

  def display(self):
    current = self.head
    while current is not None:
      print(current)
      current = current.next

  def is_sorted(self):
    current = self.head

    while current and current.next:
      if current.ssn > current.next.ssn:
        return False
      current = current.next
    return True


def merge_records(head1, head2):
  if head1 is None: 
    return head2
  if head2 is None:
    return head1

  new_head = PatientRecord("", 0, 0, 0)
  tail = new_head

  while head1 and head2:
    if head1.ssn < head2.ssn:
      tail.next, head1.prev = head1, tail
      head1 = head1.next
    else:
      tail.next, head2.prev = head2, tail
      head2 = head2.next
    tail = tail.next

  tail.next = head1 if head1 else head2

  return new_head.next

records = [
  PatientRecord("Keiffer Tan", 1, 29, 10000000),
  PatientRecord("Kathryn Cuento", 2, 28, 10000011),
  PatientRecord("Shannen Kate Tan Mao", 3, 28, 10000022),
  PatientRecord("Constantine Arhontas", 4, 29, 10000033),
  PatientRecord("Sofia Navarro Gamboa", 5, 27, 10000004),
  PatientRecord("Tim Valencia", 6, 33, 10000005),
  PatientRecord("Venea Omandac", 7, 30, 10000016),
  PatientRecord("Christian Omandac", 8, 32, 10000057),
  PatientRecord("Charmaine Tan", 9, 33, 10000077),
]

if __name__=="__main__":
  health_merge_inc = DoublyLinkedList()
  care_plus = DoublyLinkedList()

  for i in range(len(records)):
    if i <= 3:
      health_merge_inc.append(records[i])
    else:
      care_plus.append(records[i])

  # health_merge_inc.display()
  # print("\n\n")
  # care_plus.display()

  merged_head = merge_records(health_merge_inc.head, care_plus.head)
  
  merged_record = DoublyLinkedList(merged_head)
  merged_record.display()

  print(merged_record.is_sorted())

  # for record in records:
  #   print(record)


# Video Submission:
# 1. Test Cases
# 2. Time & Space Complexity
# 3. Refinement