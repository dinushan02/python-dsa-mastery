def find_target_index(numbers, target):

    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


numbers = [10, 25, 30, 45, 30, 50]
target = 30

result = find_target_index(numbers, target)

print(f"Target Index: {result}")