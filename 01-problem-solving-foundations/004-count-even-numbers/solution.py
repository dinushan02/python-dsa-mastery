numbers = [2, 5, 8, 11, 14, 7, 20]

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"Even Numbers Count: {even_count}")