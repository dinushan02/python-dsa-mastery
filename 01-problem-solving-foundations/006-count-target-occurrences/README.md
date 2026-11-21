# Problem 006: Count the Occurrences of a Target Number

**Difficulty:** Easy

**Category:** Problem-Solving Foundations

**Language:** Python

## Problem Statement

Given a list of integers and a target number, count how many times the target appears in the list without using Python's built-in `count()` method.

## Learning Objectives

- Understand Python lists and loops.
- Practice conditional comparisons.
- Apply the counter pattern.
- Understand the difference between searching and counting.
- Learn when to continue or stop a loop.
- Analyze time and auxiliary space complexity.

## Example

**Input:**

```python
numbers = [2, 5, 2, 8, 2, 10, 5]
target = 2
```

**Output:**

```text
Target Occurrences: 3
```

## Approach

1. Initialize a counter variable named `count_target` with `0`.
2. Iterate through every element in the list.
3. Compare each element with the target number.
4. If the current element matches the target, increment the counter.
5. Continue checking all remaining elements.
6. Print the final occurrence count.

## Solution

```python
numbers = [2, 5, 2, 8, 2, 10, 5]

target = 2
count_target = 0

for num in numbers:
    if num == target:
        count_target += 1

print(f"Target Occurrences: {count_target}")
```

## How It Works

The algorithm checks every element in the list and increments the counter whenever a match is found.

- First occurrence of `2`: Counter becomes `1`.
- Second occurrence of `2`: Counter becomes `2`.
- Third occurrence of `2`: Counter becomes `3`.

The final result is `3`.

## Complexity Analysis

**Time Complexity: O(n)**

The algorithm traverses every element in the list exactly once.

**Auxiliary Space Complexity: O(1)**

Only a constant amount of additional memory is required for the counter and loop variable.

## Test Cases

| Input | Target | Expected Result |
|---|---:|---:|
| `[2, 5, 2, 8, 2, 10, 5]` | 2 | 3 |
| `[1, 2, 3, 4]` | 5 | 0 |
| `[7, 7, 7, 7]` | 7 | 4 |
| `[5]` | 5 | 1 |
| `[]` | 2 | 0 |
| `[-2, 3, -2, 0]` | -2 | 2 |

## Key Takeaway

The counter pattern is useful for counting elements that satisfy a particular condition.

Unlike a simple search operation, counting occurrences requires checking every element in the collection.

This problem demonstrates how loops, conditional statements, and counter variables work together to solve practical programming problems.

---

**Status:** Completed

**Concepts Practiced:** Lists, loops, conditional statements, counter pattern, target comparison, and complexity analysis.