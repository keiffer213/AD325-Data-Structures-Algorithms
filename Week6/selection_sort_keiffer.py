import random

"""Generate a random array with a given set of elements"""
def generate_rand_array(num, lower_bound, upper_bound):
  array = []

  for _ in range(num):
    array.append(random.randint(lower_bound, upper_bound))

  # Can also approach it in this way for return
  # return [random.randint(lower_bound, upper_bound) for _ in range(num)]
  return array



"""Implementation of selection sort by passing in an array"""
def selection_sort(array):
  n = len(array)

  for i in range(n):
    # Assume the current index holds the min value
    min_index = i

    # Check the rest of the array for a smaller value and store the index of the value
    for j in range(i, n):
      if array[j] <= array[min_index]:
        min_index = j

    #Swap the positions of the current [i] with the current smallest value
    array[i], array[min_index] = array[min_index], array[i]

  return array
    
if __name__ == "__main__":
  arr1 = generate_rand_array(10, 0, 1000)

  print("Original Array: ", arr1)
  print("Sorted Array:\t", selection_sort(arr1))



