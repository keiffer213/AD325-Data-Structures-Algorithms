import unittest
from patient_health_record_keiffer import HealthRecordNode, SinglyLinkedList, is_health_record_symmetric

class TestHealthRecordSymmetry(unittest.TestCase):
  def setUp(self):
    self.record_list = SinglyLinkedList()
    self.records_non_symmetric = [
      HealthRecordNode("1/24/24", 125),
      HealthRecordNode("1/25/24", 115),
      HealthRecordNode("1/26/24", 132),
      HealthRecordNode("1/27/24", 119),
      HealthRecordNode("1/28/24", 105),
      HealthRecordNode("1/29/24", 110),
    ]
    self.records_symmetric = [
      HealthRecordNode("1/24/24", 125),
      HealthRecordNode("1/25/24", 115),
      HealthRecordNode("1/26/24", 110),
      HealthRecordNode("1/27/24", 110),
      HealthRecordNode("1/28/24", 115),
      HealthRecordNode("1/29/24", 125),
    ]
    self.records_symmetric_odd = [
      HealthRecordNode("1/24/24", 125),
      HealthRecordNode("1/25/24", 115),
      HealthRecordNode("1/26/24", 110),
      HealthRecordNode("1/26/24", 105),
      HealthRecordNode("1/27/24", 110),
      HealthRecordNode("1/28/24", 115),
      HealthRecordNode("1/29/24", 125),
    ]  

  def test_appending_records(self):
    """Test appending patient record"""
    for record in self.records_non_symmetric:
      self.record_list.append(record)
    
    self.assertEqual(self.record_list.head.heart_rate, 125)
    self.assertEqual(self.record_list.head.next.heart_rate, 115)
    self.assertEqual(self.record_list.head.next.next.heart_rate, 132)
    self.assertEqual(self.record_list.head.next.next.next.heart_rate, 119)
    self.assertEqual(self.record_list.head.next.next.next.next.heart_rate, 105)
    self.assertEqual(self.record_list.head.next.next.next.next.next.heart_rate, 110)


  def test_record_non_symmetric_even(self):
    """Test patient record symmetry for even amount - FALSE NOT SYMMETRIC"""
    for record in self.records_non_symmetric:
      self.record_list.append(record)
    
    self.assertFalse(is_health_record_symmetric(self.record_list))


  def test_record_symmetric_even(self):
    """Test patient record symmetry for even amount - TRUE"""
    for record in self.records_symmetric:
      self.record_list.append(record)
    
    self.assertTrue(is_health_record_symmetric(self.record_list))



  def test_record_symmetric_odd(self):
    """Test patient record symmetry for odd amount - TRUE"""
    for record in self.records_symmetric_odd:
      self.record_list.append(record)
    self.assertTrue(is_health_record_symmetric(self.record_list))





if __name__ == "__main__":
  unittest.main()