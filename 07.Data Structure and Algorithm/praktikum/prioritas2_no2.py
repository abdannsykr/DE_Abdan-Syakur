def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_rectangle(height, width, start):
    matrix = []
    prime_sum = 0
    current_number = start
    for i in range(height):
        row = []
        for j in range(width):
            while not prime(current_number):
                current_number += 1
            row.append(current_number)
            current_number += 1
        matrix.append(row)
    
    for row in matrix:
        prime_sum += sum(row)
        print(" ".join(map(str, row)))

    print(prime_sum)

# Test case
print("Test case 1:")
prime_rectangle(3, 2, 17)
print("\nTest cast 2:")
prime_rectangle(5, 2, 1)
