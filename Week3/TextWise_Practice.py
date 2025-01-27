



def iter_reverse(str):
  tmp_str = ""

  for i in range(len(str)):
    tmp_str += str[-1-i]

  return tmp_str

def recur_reverse(stri):
  if (len(stri)==0):
    return ""
  stri = __recur_reverse(stri, 0, len(stri))

  return stri

def __recur_reverse(stri, idx, n):
  if idx == n:
    return ""
  temp = stri[-1-idx]
  temp1 = __recur_reverse(stri, idx+1, n)

  return temp + temp1

strings_arr =  [
  #input_string, expected_output_string
  ("", ""),
  ("K", "K"),
  ("12345", "54321"),
  ("hello", "olleh"),
  ("WeLcOmE", "EmOcLeW"),
  ("!@#$%67890", "09876%$#@!"),
]

if __name__=="__main__":
  for stri in strings_arr:
    # print(recur_reverse(stri[0]))
    # print("Pass" if recur_reverse(stri[0])==stri[1] else "Fail")
    print(iter_reverse(stri[0]))
    # print("Pass" if iter_reverse(stri[0])==stri[1] else "Fail")
