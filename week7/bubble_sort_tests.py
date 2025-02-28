import unittest
from bubble_sort_keiffer import bubble_sort, bubble_sort_tuple, bubble_sort_optimized, bubble_sort_tuple_optimized, generate_rand_array

class TestSelectionSort(unittest.TestCase):

  def setUp(self):
    self.arr = generate_rand_array(10, 0, 200)
    self.arr2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    self.arr3 = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]
    self.arr4 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    self.arr5 = []
    self.arr6 = [1]

  def test_sort_rand_arr(self):
    """Test sorting a randomly generated array"""
    self.assertEqual(bubble_sort(self.arr.copy()), sorted(self.arr))
    self.assertEqual(bubble_sort_optimized(self.arr.copy()), sorted(self.arr))

  def test_sort_sorted_incr(self):
    """Test sorting an already sorted array"""
    self.assertEqual(bubble_sort(self.arr2.copy()), self.arr2)
    self.assertEqual(bubble_sort_optimized(self.arr2.copy()), self.arr2)

  def test_sort_sorted_decr(self):
    """Test Sorting an array in descending order"""
    self.assertEqual(bubble_sort(self.arr3.copy()), sorted(self.arr3))
    self.assertEqual(bubble_sort_optimized(self.arr3.copy()), sorted(self.arr3))

  def test_sort_same_elements(self):
    """Test sorting an array where all elements are the same"""
    self.assertEqual(bubble_sort(self.arr4.copy()), self.arr4)
    self.assertEqual(bubble_sort_optimized(self.arr4.copy()), self.arr4)
    
  def test_sort_edge_cases(self):
    """Test sorting an empty array and an array with a single element"""
    self.assertEqual(bubble_sort(self.arr5.copy()), self.arr5)
    self.assertEqual(bubble_sort(self.arr6.copy()), self.arr6)
    self.assertEqual(bubble_sort_optimized(self.arr5.copy()), self.arr5)
    self.assertEqual(bubble_sort_optimized(self.arr6.copy()), self.arr6)
    
  def test_stability(self):
    """Test if selection sort maintains the relative order of equal elements."""
    
    arr = [(2, 'b'), (2, 'a'), (1, 'c'), (1, 'a')]
    expected = [(1, 'c'), (1, 'a'), (2, 'b'), (2, 'a')] #The order should be preserved
    
    # I'm using another version of the bubble sort that works with tuples to only compare the first value so I can ensure that order is preserved when the array of tuples is sorted
    sorted_arr = bubble_sort_tuple(arr.copy())
    # print('HERE ->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',sorted_arr)
    self.assertEqual(sorted_arr, expected)
    self.assertEqual(bubble_sort_tuple_optimized(arr.copy()), expected)
    # print(arr, bubble_sort(arr.copy()), expected)

    arr = [(4, 'd'), (1, 'b'), (1, 'a'), (2, 'c')]
    expected = [(1, 'b'), (1, 'a'), (2, 'c'), (4, 'd')]
    self.assertEqual(bubble_sort_tuple(arr.copy()), expected)
    self.assertEqual(bubble_sort_tuple_optimized(arr.copy()), expected)

    arr = [(4, 'd'), (1, 'b'), (5, 'e'), (1, 'a'), (2, 'c')]
    expected = [(1, 'b'), (1, 'a'), (2, 'c'), (4, 'd'), (5, 'e')]
    self.assertEqual(bubble_sort_tuple(arr.copy()), expected)
    self.assertEqual(bubble_sort_tuple_optimized(arr.copy()), expected)


if __name__ == "__main__":
  unittest.main()