# Problem 003: Calculate the Sum of an Array

**Difficulty:** Easy

**Category:** Problem-Solving Foundations

**Language:** Python

## Problem Statement

Given a list of integers, calculate the sum of all elements without using Python's built-in `sum()` function.

## Learning Objectives

- Understand Python lists and loops.
- Learn the accumulator pattern.
- Practice arithmetic operations.
- Understand how to maintain a running total.
- Analyze time and auxiliary space complexity.

## Example

**Input:**

```python
numbers = [4, 7, 2, 9, 3]
```

**Output:**

```text
Total: 25
```

## Approach

1. Initialize a variable named `total` with `0`.
2. Iterate through each element in the list using a `for` loop.
3. Add the current element to the running total.
4. Continue until all elements have been processed.
5. Print the final total.

## Solution

```python
numbers = [4, 7, 2, 9, 3]

total = 0

for num in numbers:
    total += num

print(f"Total: {total}")
```

## How It Works

The algorithm uses an accumulator variable to maintain the running sum.

- Initially, `total` is `0`.
- Add `4`: total becomes `4`.
- Add `7`: total becomes `11`.
- Add `2`: total becomes `13`.
- Add `9`: total becomes `22`.
- Add `3`: total becomes `25`.

The final result is `25`.

## Complexity Analysis

**Time Complexity: O(n)**

The algorithm visits every element in the list exactly once.

**Auxiliary Space Complexity: O(1)**

Only one additional variable, `total`, is required regardless of the input size.

## Test Cases

| Input | Expected Result |
|---|---:|
| `[4, 7, 2, 9, 3]` | `25` |
| `[5]` | `5` |
| `[10, 20, 30]` | `60` |
| `[-2, 5, -3]` | `0` |
| `[]` | `0` |

## Key Takeaway

The accumulator pattern is useful when calculating totals or maintaining a running result while iterating through a collection.

Initializing the accumulator with zero allows the algorithm to handle an empty list correctly.

---

**Status:** Completed

**Concepts Practiced:** Lists, loops, arithmetic operations, accumulator pattern, and complexity analysis.