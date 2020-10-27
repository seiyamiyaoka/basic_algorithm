# Max and Min in a Unsorted Array

## About data structure and algorithm

It uses a quick select algorithm that uses the median of the median.
Divide the data using the optimal median as a pivot.

Compare the value of k with the number of elements of less, less + equal to see which array has the desired value.

Once you have identified the array that has the desired value, search recursively.

## About Order complexity
$O(n)$.

Loop n times to divide the array into groups with 5 elements.
The pivot to use is a good enough pivot because it is obtained using the median of the median.

The size of the element to be searched is reduced by 95%.

there fore $O((19/20 * n) + n)$.

To ignore constant multiples

$O(n)$

## About Space complexity
- get_min_max(ints)
  - $O(n)$. because ints is array.
- kth_largest_arr(arr, k)
  - $O(n ^ 2)$. This is because each time it is executed recursively, it holds more arrays.
## About implementation

You can get the minimum and maximum values by specifying 1, and len (inputs).
