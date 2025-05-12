import pdb

# Debugging Examples in Python

# Example 1: Fixing a Syntax Error
# Without debugging, you might miss a simple typo.
def add_numbers(a, b):
    return a + b

# Debugging helps you identify and fix issues like this:
# print(add_numbers(5, 3))  # Uncomment to test

# Example 2: Identifying Logical Errors
# A function to calculate the average of a list of numbers.
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    # Debugging helps you realize if there's a division by zero error.
    return total / count if count > 0 else 0

# Debugging can help you test edge cases:
# print(calculate_average([10, 20, 30]))  # Expected: 20
# print(calculate_average([]))  # Expected: 0

# Example 3: Understanding Unexpected Behavior
# A function to find the maximum number in a list.
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Debugging helps you catch errors in edge cases:
# print(find_maximum([3, 1, 4, 1, 5, 9]))  # Expected: 9
# print(find_maximum([-1, -5, -3]))  # Expected: -1

# Example 4: Using Debugging Tools
# Python's built-in debugger (pdb) can help step through code.

def buggy_function():
    x = 10
    y = 0
    pdb.set_trace()  # Start debugging here
    result = x / y  # This will raise a ZeroDivisionError
    return result

# Uncomment the line below to test debugging with pdb:
# buggy_function()

# Debugging is essential for identifying and fixing errors, improving code quality, and understanding program behavior.