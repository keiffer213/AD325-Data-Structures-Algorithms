import random

"""Generate a random array with a given set of elements"""
def generate_rand_array(num, lower_bound, upper_bound):
  array = []

  for _ in range(num):
    array.append(random.randint(lower_bound, upper_bound))

  # Can also approach it in this way for return
  # return [random.randint(lower_bound, upper_bound) for _ in range(num)]
  return array


""" Implementation of Insetion Sort """
def insertion_sort(array):
  n = len(array)  

  while True:
    swapped = False

    for i in range(n-1):
      if array[i] > array[i+1]:
        array[i+1], array[i] = array[i], array[i+1]
        swapped = True
    
    if swapped == False:
      break

  return array


    
if __name__ == "__main__":
  arr1 = generate_rand_array(10, 0, 100)

  print("Original Array: ", arr1)
  print("Sorted Array:\t", insertion_sort(arr1))
