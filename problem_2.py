def rotated_array_search(input_list, number):
  index = 0
  if number is None:
    return -1
  return recursive_search(input_list, number, index, True)

def recursive_search(input_list, number, index, flg=False):
  n = len(input_list)
  if n == 1:
    if input_list[0] == number:
        return index
    else:
        return -1
  pivot = n // 2

  # pivotの要素数に応じて調整
  if n > 2 and n % 2 == 0:
    pivot -= 1

  if flg:
    if number == input_list[pivot]:
      return pivot
    elif number <= input_list[-1]:
      # right side
      return recursive_search(input_list[pivot+1:], number, pivot+1)
    else:
      # left side
      return recursive_search(input_list[:pivot], number, index)
  else:
    if number == input_list[pivot]:
        return pivot + index
    if number < input_list[pivot]:
      # left
      return recursive_search(input_list[:pivot], number, pivot + index -1)
    else:
      # right
      return recursive_search(input_list[pivot:], number, index + pivot)

def linear_search(input_list, number):
  for index, element in enumerate(input_list):
    if element == number:
      return index
  return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 3])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 11])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], -1])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], None])
# Pass