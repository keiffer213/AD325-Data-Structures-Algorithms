








def manage_inventory(inventory1):
  # print("input ", inventory1)
  i = 0

  while i < len(inventory1):
    if inventory1[i] == 0 and len(inventory1) > 1:
      j = len(inventory1)-1
      while j != i+1 and j > 1:
        inventory1[j] = inventory1[j-1]
        # print(inventory1, j, i)
        j -= 1
      if i != len(inventory1)-1:
        inventory1[i+1] = 0
      i += 1
    i += 1 #increment so it doesn't go over duplicated 0

  # print("Inside Function: ", inventory1)
  return inventory1


inventories_data = [  # input, exprected_output
  ([], []),
  ([0], [0]),
  ([1], [1]),
  ([3,2,1], [3,2,1]),
  ([3,0,1], [3,0,0]),
  ([4,0,1,3,0,2,5,0], [4,0,0,1,3,0,0,2])
]

if __name__=="__main__":
  for inventory in inventories_data:
    # print("Before Function: ", inventory[0])

    # IMPORTANT ***** Can only call manage_inventory once because it is changing the actual array in inventory[0] so by calling it multiple times, you're changing the actual data over and over again which makes the test fail. Passing in the reference to the array rather than passing the values array, can pass a copy instead of reference if want to in future

    # print(manage_inventory(inventory[0]), inventory[1], manage_inventory(inventory[0]) == inventory[1])
    print("Pass" if manage_inventory(inventory[0]) == inventory[1] else "Fail")