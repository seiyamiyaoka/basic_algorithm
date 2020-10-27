# Rearrange Array Elements

## About data structure and algorithm

I am using quicksort using the median of medians.

## About Order complexity
$O(n log n)$

The Order complexity is $O(n log n)$.
First of all, the quick_sort function is used to sort the array in ascending order.

This function uses the median of the median to find the pivot. I use bubble sort to find the median, but since the maximum number of elements is 5, the amount of calculation is considered to be $O(1)$.

The total amount of calculation is

$O(3(n log n) + 2n + 1)$
Therefore
$O(n log n)$

## About Space complexity

- rearrange_digits(input_list)
  - $O(n)$. This is to store the elements of input_list in the `left` and `right` variables. The number of elements is n.
- convert_to_int(arr)
  - $O(n)$. This is because the number of elements in arr is n.
- quick_sort(items, sort_type="desc")
  - $O(n)$. This is because the pivot_value variable and pivot_index take an integer or None value.
- sort_all(items, begin_index, end_index, pivot_index, sort_type)
  - $O(n)$. This function uses space to hold the pivot_index. The number of executions is required until end_index <= begin_index is reached, so n times are required.
- sort_a_little_bit(items, begin_index, pivot_index, sort_type)
  - $O(n)$.
- fastSelect(arr, k)
  - $O(n^2)$.
- findMedian(arr, start, size)
  - $O(n)$.
## About implementation

First, sort the array in ascending order.
Compare adjacent numbers and assign the result to a variable.

The total is maximized by sorting the values assigned to each variable in descending order.