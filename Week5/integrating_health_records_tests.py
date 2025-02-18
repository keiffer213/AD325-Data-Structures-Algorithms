import unittest
from integrating_health_records_keiffer import DoublyLinkedList, PatientRecord, merge_records

class TestIntegratingHealthRecords(unittest.TestCase):

  def setUp(self):
    self.record = DoublyLinkedList()
    self.records = [
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
  
    self.health_merge_inc = DoublyLinkedList()
    self.care_plus = DoublyLinkedList()
  
  def test_appending_orders(self):
    """Test Appending patient records"""
    for i in range(len(self.records)):
      if i <= 3:
        self.health_merge_inc.append(self.records[i])
      else:
        self.care_plus.append(self.records[i])

    self.assertEqual(self.health_merge_inc.head.patient_id, 1)
    self.assertEqual(self.health_merge_inc.head.next.patient_id, 2)
    self.assertEqual(self.health_merge_inc.head.next.next.patient_id, 3)
    self.assertEqual(self.health_merge_inc.head.next.next.next.patient_id, 4)
    self.health_merge_inc.append(PatientRecord("Test", 10, 10, 10000000))
    self.assertEqual(self.health_merge_inc.head.next.next.next.next.patient_id, 10)

    self.assertEqual(self.care_plus.head.patient_id, 5)
    self.assertEqual(self.care_plus.head.next.patient_id, 6)
    self.assertEqual(self.care_plus.head.next.next.patient_id, 7)
    self.assertEqual(self.care_plus.head.next.next.next.patient_id, 8)
    self.assertEqual(self.care_plus.head.next.next.next.next.patient_id, 9)

  def test_merging_records_and_is_sorted(self):
    for i in range(len(self.records)):
      if i <= 3:
        self.health_merge_inc.append(self.records[i])
      else:
        self.care_plus.append(self.records[i])

    merged_head = merge_records(self.health_merge_inc.head, self.care_plus.head)
    
    merged_record = DoublyLinkedList(merged_head)
    # merged_record.display()

    self.assertEqual(merged_record.head.patient_id, 1)
    self.assertEqual(merged_record.head.next.patient_id, 5)
    self.assertEqual(merged_record.head.next.next.patient_id, 6)
    self.assertEqual(merged_record.head.next.next.next.patient_id, 2)
    self.assertEqual(merged_record.head.next.next.next.next.patient_id, 7)
    self.assertEqual(merged_record.head.next.next.next.next.next.patient_id, 3)
    self.assertEqual(merged_record.head.next.next.next.next.next.next.patient_id, 4)
    self.assertEqual(merged_record.head.next.next.next.next.next.next.next.patient_id, 8)
    self.assertEqual(merged_record.head.next.next.next.next.next.next.next.next.patient_id, 9)

    self.assertTrue(merged_record.is_sorted())

    

  def test_display_orders(self):
    """Test displaying Orders to the linked list"""
    for i in range(4):
      self.health_merge_inc.append(self.records[i])

    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output #Redirect the stdout from console to captured_output

    self.health_merge_inc.display()

    # Reseting stdout is important as subsequent tests may continue using StringIO
    sys.stdout = sys.__stdout__ #Reset stdout back to console (original value)
    output = captured_output.getvalue()
    self.assertIn("Keiffer Tan", output)
    self.assertIn("Kathryn Cuento", output)
    self.assertIn("Shannen Kate Tan", output)
    self.assertIn("Constantine Arhontas", output)




if __name__ == "__main__":
  unittest.main()