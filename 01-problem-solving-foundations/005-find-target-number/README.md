# Problem 005: Find the Target Number in an Array

**Difficulty:** Easy

**Category:** Searching / Problem-Solving Foundations

**Algorithm:** Linear Search

**Language:** Python

## Problem Statement

Given a list of integers and a target number, determine whether the target exists in the list without using Python's built-in `in` operator, `index()`, or `find()` methods.

## Learning Objectives

- Understand the linear search algorithm.
- Practice iterating through a list.
- Use conditional statements for comparison.
- Understand Boolean variables and flags.
- Learn when and why to use the `break` statement.
- Analyze best-case, average-case, and worst-case time complexity.

## Example

**Input:**

```python
numbers = [10, 25, 30, 45, 50]
target = 30
```

**Output:**

```text
Target Found: True
```

## Approach

1. Initialize a Boolean variable `target_found` with `False`.
2. Iterate through the list using a `for` loop.
3. Compare each element with the target number.
4. If a match is found, update `target_found` to `True`.
5. Use `break` to stop searching because the target has already been found.
6. Print the final Boolean result.

## Solution

```python
numbers = [10, 25, 30, 45, 50]

target = 30
target_found = False

for num in numbers:
    if num == target:
        target_found = True
        break

print(f"Target Found: {target_found}")
```

## How It Works

The algorithm checks each element in the list sequentially.

- Compare `10` with `30`: No match.
- Compare `25` with `30`: No match.
- Compare `30` with `30`: Match found.
- Set `target_found` to `True`.
- Stop the loop using `break`.

The final result is `True`.

## Mistake Encountered and Correction

**Initial mistake:**

The original implementation used an `else` block to reset `target_found` to `False` whenever the current element did not match the target.

This caused a logical error because a previously discovered match could be overwritten by a later non-matching element.

**Correction:**

Remove the resetting `else` block and use `break` after finding the target.

This ensures that once a match is found, the result remains `True`.

## Complexity Analysis

**Best-case Time Complexity: O(1)**

The target is found in the first element.

**Average-case Time Complexity: O(n)**

The algorithm may need to examine several elements.

**Worst-case Time Complexity: O(n)**

The target is at the end of the list or does not exist.

**Auxiliary Space Complexity: O(1)**

The algorithm uses a constant amount of additional memory.

## Test Cases

| Input Target | Expected Result |
|---|---|
| `10` | `True` |
| `30` | `True` |
| `50` | `True` |
| `100` | `False` |
| `25` | `True` |

## Key Takeaway

Linear Search is a fundamental searching algorithm that checks elements one by one.

This problem introduced Boolean flags and the `break` statement, which are useful when controlling loops and searching for specific values.

An important lesson from this problem is that a discovered result should not be accidentally overwritten during later iterations.

---

**Status:** Completed after logical correction

**Concepts Practiced:** Lists, loops, conditional statements, Boolean flags, linear search, break statement, and complexity analysis.