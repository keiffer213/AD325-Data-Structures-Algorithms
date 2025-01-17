

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:  
        if num > max_num:
            max_num = num
    return max_num

def find_max_efficiently(numbers):
    return max(numbers)

numArr = [0, 1, 2, 3, 5, 7,9, 22, 5, 4, 6, 101, 1, 2, 12, 42]
print("find_max", find_max(numArr))
print("Efficient", find_max_efficiently(numArr))
