



def analyze_financial_growth(arr):

  for i in range(len(arr)):
    arr[i] = arr[i]*arr[i]

  return sorted(arr)


growth_percentages = [
  ([], []),
  ([0], [0]),
  ([-5, -2, 0, 3, 10], [0, 4, 9, 25, 100]),
  ([-8, -3, 2, 4, 12], [4, 9, 16, 64, 144]),
  ([-12, -16, -5, 3, -6, -22, -40], [9, 25, 36, 144, 256, 484, 1600])
]

if __name__=="__main__":
  for one in growth_percentages:
    # analyze_financial_growth(one[0])
    print("Pass" if analyze_financial_growth(one[0]) == one[1] else "Fail")

    # Time complexity of O(nlogn) because of sorted(arr)