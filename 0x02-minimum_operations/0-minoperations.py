#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy
        paste
'''
def minOperations(n):
   if n < 2:
        return 0

    min_operations = float('inf')  # Initialize with infinity

    for i in range(2, n + 1):
        if n % i == 0:
            operations = minOperations(i) + (n // i)
            min_operations = min(min_operations, operations)

    return min_operations

if __name__ == '__main__':
    # Test the function with some sample values
    print(minOperations(3))  # Expected output: 3 (Copy All, Paste, Paste)
    print(minOperations(8))  # Expected output: 6 (Copy All, Paste, Paste, Paste, Paste, Paste)

