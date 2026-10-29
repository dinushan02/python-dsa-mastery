numbers = [8, 3, 12, 1, 6]

smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

print(f"Smallest Number: {smallest_number}")