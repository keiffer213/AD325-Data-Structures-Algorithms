



# def iter_reverse(stri):
#   temp_str = ""

#   for i in range(len(stri)):
#     temp_str += stri[-1 - i]

#   return temp_str

def recur_reverse(stri):
  if (len(stri)==0):
    return ""

  stri1 = __recur_reverse(stri, 0, len(stri))  

  return stri1

def __recur_reverse(stri, idx, n):
  if idx == n:
    return ""

  return stri[-1 - idx] + __recur_reverse(stri, idx+1, n)



strings_arr = [
  #input_string, expected_output_string
  ("", ""),
  ("K", "K"),
  ("12", "21"),
  ("1234567", "7654321"),
  ("Hello", "olleH"),
  ("WeLcOmE", "EmOcLeW"),
  ("!@#$%67890", "09876%$#@!"),
]

if __name__ == "__main__":
  for stri in strings_arr:
    # print(stri[0], " ", stri[1])
    # print("Pass" if iter_reverse(stri[0])==stri[1] else "Fail")
    # print(recur_reverse(stri[0]))
    print("Pass" if recur_reverse(stri[0])==stri[1] else "Fail")
    assert(recur_reverse(stri[0])==stri[1])
    
