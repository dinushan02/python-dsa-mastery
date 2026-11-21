numbers = [2, 5, 2, 8, 2, 10, 5]

target = 2
count_target = 0

for num in numbers:
    if num == target:
        count_target += 1

print(f"Target Occurrences: {count_target}")