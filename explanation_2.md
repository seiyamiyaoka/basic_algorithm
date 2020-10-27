# Search in a Rotated Sorted Array

## About data structure and algorithm

It uses recursive processing to cut the target value in half.

## About Order complexity
$O(log n)$

The Order complexity is $O(log n)$
This is because the value is halved each time the process is executed.

## About Space complexity

- rotated_array_search(input_list, number)
  - $O(n)$.
- recursive_search(input_list, number, index, flg=False)
  - $O(n)$. input_list is an array. I'm passing a reference without holding a new array.

## About implementation

In the first data split, the last value is used to determine whether the desired value is on the right or left side of pivot.
This is because the values in the array are rotated sorted.

From the second time onward, it is not rotated sorted, so execute a general quick select based on pivot.