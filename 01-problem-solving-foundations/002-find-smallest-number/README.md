# Problem 002: Find the Smallest Number

**Difficulty:** Easy

**Category:** Problem-Solving Foundations

**Language:** Python

## Problem Statement

Given a non-empty list of integers, find the smallest number without using Python's built-in `min()` function or sorting the list.

## Learning Objectives

- Understand Python lists and loops.
- Apply comparison operators.
- Maintain a running minimum value.
- Reuse a known algorithmic pattern.
- Analyze time and auxiliary space complexity.

## Example

**Input:**

```python
numbers = [8, 3, 12, 1, 6]
```

**Output:**

```text
Smallest Number: 1
```

## Approach

1. Initialize `smallest_number` with the first element.
2. Iterate through each number in the list.
3. Compare the current number with `smallest_number`.
4. If the current number is smaller, update `smallest_number`.
5. Print the final smallest number.

## Solution

```python
numbers = [8, 3, 12, 1, 6]

smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

print(f"Smallest Number: {smallest_number}")
```

## Complexity Analysis

**Time Complexity: O(n)**

Each element is checked once.

**Auxiliary Space Complexity: O(1)**

The algorithm uses a constant amount of additional space.

## Test Cases

| Input | Expected Result |
|---|---|
| `[8, 3, 12, 1, 6]` | `1` |
| `[5]` | `5` |
| `[-8, -3, -12]` | `-12` |
| `[7, 7, 7]` | `7` |
| `[0, -2, 4]` | `-2` |

The solution assumes a non-empty list.

## Key Takeaway

A running minimum can be found by traversing a list once and updating the stored value whenever a smaller element appears.

This approach follows the same general pattern as finding the largest number, with the comparison reversed.

---

**Status:** Completed

**Concepts Practiced:** Lists, loops, conditional statements, comparisons, and complexity analysis.