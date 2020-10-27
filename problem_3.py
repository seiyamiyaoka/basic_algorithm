def rearrange_digits(input_list):
  n = len(input_list)
  left = []
  right = []

  if n <= 1:
    return input_list

  # $O(n log n)$
  quick_sort(input_list, "asc")
  # O(n)
  for i in range(1, n, 2):
    large_value = max(input_list[i-1], input_list[i])
    left.append(large_value)
    if large_value == input_list[i -1]:
      right.append(input_list[i])
    else:
      right.append(input_list[i-1])
  # O(1)
  if n % 2 is not 0:
    left.append(input_list[-1])
  # desc sort
  # O(n log n)
  quick_sort(left)
  # O(n log n)
  quick_sort(right)
  # O(n)
  return [convert_to_int(left), convert_to_int(right)]

def convert_to_int(arr):
  arr = [str(i) for i in arr]
  return int("".join(arr))

def quick_sort(items, sort_type="desc"):
  pivot_value = fastSelect(items, len(items) // 2)
  pivot_index = None
  for index, element in enumerate(items):
    if element == pivot_value:
      pivot_index = index
  sort_all(items, 0, len(items) -1, pivot_index, sort_type)

def sort_all(items, begin_index, end_index, pivot_index, sort_type):
  if end_index <= begin_index:
    return
  pivot_index = sort_a_little_bit(items, begin_index, end_index, sort_type)
  sort_all(items, begin_index, pivot_index -1, pivot_index, sort_type)
  sort_all(items, pivot_index + 1, end_index, pivot_index, sort_type)

def sort_a_little_bit(items, begin_index, pivot_index, sort_type):
  left_index = begin_index
  pivot_value = items[pivot_index]

  while(pivot_index != left_index):
    item = items[left_index]

    if sort_type == 'desc':
      if item >= pivot_value:
        left_index += 1
        continue
    else:
      if item <= pivot_value:
        left_index += 1
        continue

    items[left_index] = items[pivot_index - 1]
    items[pivot_index - 1] = pivot_value
    items[pivot_index] = item
    pivot_index -= 1
  return pivot_index

def fastSelect(arr, k):
  n = len(arr)

  if(k > 0 and k <= n):
      set_of_medians = []
      arr_less_p = []
      arr_equal_p = []
      arr_more_p = []
      i = 0

      while (i < n // 5):
        median = findMedian(arr, 5*i, 5)
        set_of_medians.append(median)
        i += 1

      if (5 * i < n):
        median = findMedian(arr, 5 * i, n % 5)

        set_of_medians.append(median)

      if(len(set_of_medians) == 1):
        pivot = set_of_medians[0]
      elif(len(set_of_medians) > 1):
        pivot = fastSelect(set_of_medians, (len(set_of_medians) // 2))

      for element in arr:
        if(element < pivot):
          arr_less_p.append(element)
        elif(element > pivot):
          arr_more_p.append(element)
        else:
          arr_equal_p.append(element)

      if(k <= len(arr_less_p)):
        return fastSelect(arr_less_p, k)
      elif(k > (len(arr_less_p) + len(arr_equal_p))):
        return fastSelect(arr_more_p, (k - len(arr_less_p) - len(arr_equal_p)))
      else:
        return pivot


def findMedian(arr, start, size):
  myList = []
  for i in range(start, start + size):
    myList.append(arr[i])

  for _ in range(len(myList)):
    for i in range(1, len(myList), 1):
      if myList[i -1] > myList[i]:
        myList[i -1], myList[i] = myList[i], myList[i -1]

  return myList[size // 2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass
test_function([[1], [1]])
# Pass
test_function([[], []])
# Pass