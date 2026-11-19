numbers = [10, 25, 30, 45, 50]

target = 30
target_found = False

for num in numbers:
    if num == target:
        target_found = True
        break

print(f"Target Found: {target_found}")