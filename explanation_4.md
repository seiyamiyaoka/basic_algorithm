# Dutch National Flag Problem

## About data structure and algorithm

I am using quicksort using the median of medians.

## About Order complexity
$O(n)$

Loop until front_index is at end_position.

Increase front_index or decrease end_position under any condition of the loop.

Therefore, two numbers approach each other by one for each loop.

## About Space complexity

- sort_012(input_list)
  - $O(n)$. This is because the contents of one array are replaced and used.

## About implementation

Place 1 to the right of 0, or to the left of 2, and 2 to the right, so that 0 is placed to the left.

This algorithm increases the sorted part each time it loops.

Sorting generally requires $O(n log n)$ time complexity.

If there are three types of numbers, this method is more effective because it requires less calculation.