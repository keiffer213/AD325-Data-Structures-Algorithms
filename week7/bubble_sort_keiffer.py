import random

"""Generate a random array with a given set of elements"""
def generate_rand_array(num, lower_bound, upper_bound):
  array = []

  for _ in range(num):
    array.append(random.randint(lower_bound, upper_bound))

  # Can also approach it in this way for return
  # return [random.randint(lower_bound, upper_bound) for _ in range(num)]
  return array

"""Simplest Bubble Sort implementation without optimizations."""
def bubble_sort(arr):
    n = len(arr)

    # Nested loops to traverse the array n*n times
    for _ in range(n - 1): 
        for i in range(n - 1): 
            if arr[i] > arr[i + 1]:  
                # If the previous index is larger, then swap spots
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

"""Simplest Bubble Sort implementation without optimizations for tuple input stability testing."""
def bubble_sort_tuple(arr):
    n = len(arr)

    # Nested loops to traverse the array n*n times
    for _ in range(n - 1):  
        for i in range(n - 1):  
            if arr[i][0] > arr[i + 1][0]:  
                # If the previous index is larger, then swap spots
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


""" Implementation of Bubble Sort Optimized with early stopping"""
def bubble_sort_optimized(array):
  n = len(array)  

  # iterate through array until no swaps are made
  while True:
    swapped = False

    for i in range(n - 1):
      if array[i] > array[i+1]:
        # If the previous index is larger, then swap spots
        array[i+1], array[i] = array[i], array[i+1]
        swapped = True # flag that a swap has been made 
    
    # Break if there are no swaps made to reduce amount of iterations 
    if swapped == False:
      break

  return array

""" Implementation of Bubble Sort optimization w/ tuple input to test stability """
def bubble_sort_tuple_optimized(array):
  n = len(array)  

  # iterate through array until no swaps are made
  while True:
    swapped = False

    for i in range(n - 1):
      if array[i][0] > array[i+1][0]:
        # If the previous index is larger, then swap spots
        array[i+1], array[i] = array[i], array[i+1]
        swapped = True # flag that a swap has been made 
    
    # Break if there are no swaps made to reduce amount of iterations 
    if swapped == False:
      break

  return array


    
if __name__ == "__main__":
  arr1 = generate_rand_array(10, 0, 100)

  print("Original Array: ", arr1)
  print("Sorted Array:\t", bubble_sort(arr1))



