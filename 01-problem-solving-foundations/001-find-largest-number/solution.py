numbers = [12, 5, 27, 9, 18]

largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"Largest Number: {largest_number}")