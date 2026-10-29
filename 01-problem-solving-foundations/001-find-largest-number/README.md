# Problem 001: Find the Largest Number

**Difficulty:** Easy

**Category:** Problem-Solving Foundations

**Language:** Python

## Problem Statement

Given a non-empty list of integers, find the largest number without using Python's built-in `max()` function or sorting the list.

## Learning Objectives

- Understand Python lists and loops.
- Compare numbers using conditional statements.
- Maintain a running maximum value.
- Practice logical thinking and problem decomposition.
- Analyze time and auxiliary space complexity.

## Example

**Input:**

```python
numbers = [12, 5, 27, 9, 18]
```

**Output:**

```text
Largest Number: 27
```

## Approach

1. Initialize `largest_number` with the first element of the list.
2. Iterate through each number in the list.
3. Compare the current number with `largest_number`.
4. If the current number is larger, update `largest_number`.
5. Print the final largest number after the loop finishes.

## Solution

```python
numbers = [12, 5, 27, 9, 18]

largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"Largest Number: {largest_number}")
```

## How It Works

The algorithm starts with `12` as the largest number.

- `5` is smaller than `12`, so no update is needed.
- `27` is larger than `12`, so the largest value becomes `27`.
- `9` and `18` are both smaller than `27`, so the value remains unchanged.

The algorithm finishes with `27` as the largest number.

## Complexity Analysis

**Time Complexity: O(n)**

The algorithm iterates through all `n` elements once.

**Auxiliary Space Complexity: O(1)**

The algorithm uses a constant amount of additional space.

## Assumptions and Edge Cases

The solution assumes that the list contains at least one element.

| Test Case | Expected Result |
|---|---|
| `[12, 5, 27, 9, 18]` | `27` |
| `[5]` | `5` |
| `[-8, -3, -12]` | `-3` |
| `[7, 7, 7]` | `7` |
| `[0, -2, 4]` | `4` |

An empty list must be handled separately if it is allowed by the problem requirements.

## Key Takeaway

Maintaining a running maximum allows us to find the largest number in one traversal without sorting the list or using a built-in maximum function.

This pattern can also be adapted to find the smallest number and track the best value in other problems.

---

**Status:** Completed

**Concepts Practiced:** Lists, loops, conditional statements, comparisons, and complexity analysis.