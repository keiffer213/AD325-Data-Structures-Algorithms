


def analyze_financial_growth(arr):

  for i in range(len(arr)):
    arr[i] = arr[i] ** 2
  
  return sorted(arr)
    


growth_percentage = [
  ([], []),
  ([0], [0]),
  ([-5, -2, 0, 3, 10], [0, 4, 9, 25, 100]),
  ([-8, -3, 2, 4, 12], [4, 9, 16, 64, 144]),
]

if __name__ == "__main__":
  for one in growth_percentage:
    # print(analyze_financial_growth(one[0]), " == ", one[1])
    # print("Pass" if analyze_financial_growth(one[0]) == one[1] else "Fail")
    assert(analyze_financial_growth(one[0]) == one[1])
  

