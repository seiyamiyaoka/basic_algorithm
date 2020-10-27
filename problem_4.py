def sort_012(input_list):
  if len(input_list) < 1:
    return []
  front_next_position = 0
  end_position = len(input_list) -1
  front_index = 0

  while front_index <= end_position:
    if input_list[front_index] == 0:
      input_list[front_index] = input_list[front_next_position]
      input_list[front_next_position] = 0
      front_index += 1
      front_next_position += 1
    elif input_list[front_index] == 2:
      input_list[front_index] = input_list[end_position]
      input_list[end_position] = 2
      end_position -= 1
    else:
      front_index += 1
  return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass
test_function([0, 0, 1, 0, 1])
# Pass
test_function([])
# Pass
test_function([1])
# Pass