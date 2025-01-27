






def manage_inventory(inventory):

  i = 0
  while i < len(inventory):

    if inventory[i] == 0 and len(inventory) > 1:
      # [3,0,1,2,3] -> [3,0,1,2,2] -> [3,0,1,1,2] -> [3,0,0,1,2]
      # print(inventory)
      j = len(inventory)-1

      while j != i+1 and j > 1:
        inventory[j] = inventory[j-1]
        j -= 1
        # print(inventory)

      if i != len(inventory)-1:
        inventory[i+1] = 0

      i += 1
    i += 1



  return inventory


inventory_data = [
  # input, expected_out
  ([], []),
  ([0], [0]),
  ([1], [1]),
  ([3,2,1], [3,2,1]),
  ([3,0,1], [3,0,0]),
  ([4,0,1,3,0,2,5,0], [4,0,0,1,3,0,0,2]),
]


if __name__ == "__main__":
  for inventory in inventory_data:
    # print(manage_inventory(inventory[0]))
    print("Pass" if manage_inventory(inventory[0])==inventory[1] else "Fail")
    # assert(manage_inventory(inventory[0])==inventory[1])
