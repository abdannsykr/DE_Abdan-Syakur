def group_numbers(numbers, target):
    number = [[], []] 
    for num in numbers:
        number[num % target == 0].append(num)
    return number[::-1]

print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) # [[3, 6, 9], [1, 2, 4, 5, 7, 8]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5)) # [[15, 20, 75, 30, 45], [23, 19]]
