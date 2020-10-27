# Finding the Square Root of an Integer

## About data structure and algorithm

It uses recursive processing to cut the target value in half.

## About Order complexity
$O(log n)$

The Order complexity is $O(log n)$
This is because the value is halved each time the process is executed.

## About Space complexity

- sqrt(number)
  - $O(1)$.
- recursive_sqrt(number, target_num)
  - $O(n)$. A value is assigned to the `number` variable each time it is called recursively.

## About implementation

Decrease the 'number' variable in half.
This function always halves the value and checks if the square of that value is equal to the desired value.
Since this function needs to return a value as an integer, we add to the base case whether the square of `number` and the square of `number + 1` are within the desired range.