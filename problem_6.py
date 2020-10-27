def get_min_max(ints):
  return (kth_largest_arr(ints, 1), kth_largest_arr(ints, len(ints)))

def kth_largest_arr(arr, k):
  n = len(arr)

  if (k > 0 and k <= n):
    i = 0
    medians = []
    arr_less_p = []
    arr_equal_p = []
    arr_more_p = []

    while (i < n // 5):
      median = search_median(arr, 5 * i, 5)
      medians.append(median)
      i += 1

    if (5 * i < n):
      median = search_median(arr, 5 * i, n % 5)
      medians.append(median)

    if(len(medians) == 1):
      pivot = medians[0]
    elif(len(medians) > 1):
      pivot = kth_largest_arr(medians, len(medians) // 2)
    for element in arr:
      if element < pivot:
        arr_less_p.append(element)
      elif element > pivot:
        arr_more_p.append(element)
      else:
        arr_equal_p.append(element)
    if(k <= len(arr_less_p)):
      return kth_largest_arr(arr_less_p, k)
    elif(k > len(arr_less_p) + len(arr_equal_p)):
      return kth_largest_arr(arr_more_p, k - len(arr_less_p) - len(arr_equal_p))
    else:
      return pivot

def search_median(arr, start, size):
  tmp = []

  for i in range(start, start + size):
    tmp.append(arr[i])

  for _ in range(len(tmp)):
    for i in range(1, len(tmp), 1):
      if tmp[i] < tmp[i -1]:
        tmp[i], tmp[i -1] = tmp[i -1], tmp[i]

  return tmp[size // 2]

import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")