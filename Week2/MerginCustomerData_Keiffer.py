







def combine_data(c_data1, c_data2):
  for i in range(len(c_data1)):
    if c_data1[i] == 0:
      c_data1[i] = c_data2[i - len(c_data2)]

  return sorted(c_data1)


customer_data = [
  # cust_data1, cust_data2, expected_output
  ([], [], []),
  ([103], [], [103]),
  ([2, 5, 0, 0], [8, 1], [1, 2, 5, 8]),
  ([0, 0, 0, 0, 0], [25, 176, 3, 8, 1], [1, 3, 8, 25, 176]),
  ([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, 0, 0, 0, 0], [99, 97, 5, 55, 25, 15, 155], [1, 2, 3, 4, 5, 5, 6, 7, 15, 25, 55, 97, 99, 155]),
]


if __name__=="__main__":
  for customer in customer_data:
    print("Returned: ", combine_data(customer[0], customer[1]), "\t Expected: ", customer[2])
    print("Pass" if combine_data(customer[0], customer[1])==customer[2] else "Fail")
    assert combine_data(customer[0], customer[1])==customer[2]
