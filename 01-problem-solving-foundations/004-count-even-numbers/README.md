# Problem 004: Count Even Numbers in an Array

**Difficulty:** Easy

**Category:** Problem-Solving Foundations

**Language:** Python

## Problem Statement

Given a list of integers, count how many even numbers are present without using Python's built-in `count()` method.

## Learning Objectives

- Understand Python lists and loops.
- Identify even numbers using the modulo operator.
- Apply conditional statements.
- Understand the counter pattern.
- Analyze time and auxiliary space complexity.

## Example

**Input:**

```python
numbers = [2, 5, 8, 11, 14, 7, 20]
```

**Output:**

```text
Even Numbers Count: 4
```

## Approach

1. Initialize a counter variable named `even_count` with `0`.
2. Iterate through each element in the list.
3. Check whether the current number is divisible by `2` using the modulo operator (`%`).
4. If the remainder is `0`, increment the counter by `1`.
5. Print the final count after processing all elements.

## Solution

```python
numbers = [2, 5, 8, 11, 14, 7, 20]

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"Even Numbers Count: {even_count}")
```

## How It Works

The algorithm checks every number in the list.

- `2` is even: counter becomes `1`.
- `5` is odd: counter remains `1`.
- `8` is even: counter becomes `2`.
- `11` is odd: counter remains `2`.
- `14` is even: counter becomes `3`.
- `7` is odd: counter remains `3`.
- `20` is even: counter becomes `4`.

The final result is `4`.

## Complexity Analysis

**Time Complexity: O(n)**

The algorithm traverses the entire list once, where `n` represents the number of elements.

**Auxiliary Space Complexity: O(1)**

Only a constant amount of additional memory is required for the counter variable.

## Test Cases

| Input | Expected Result |
|---|---:|
| `[2, 5, 8, 11, 14, 7, 20]` | `4` |
| `[2, 4, 6, 8]` | `4` |
| `[1, 3, 5, 7]` | `0` |
| `[0, 2, 4]` | `3` |
| `[-2, -4, 3]` | `2` |
| `[5]` | `0` |
| `[]` | `0` |

## Key Takeaway

The counter pattern is useful when counting elements that satisfy a specific condition.

The modulo operator allows us to identify even numbers efficiently without using built-in counting methods.

---

**Status:** Completed

**Concepts Practiced:** Lists, loops, conditional statements, modulo operator, counter pattern, and complexity analysis.