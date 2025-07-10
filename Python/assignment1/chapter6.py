# 1. Create a lambda to multiply two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
multiply = lambda a, b: a * b
print("Result:", multiply(a, b))


# 2. Use lambda to sort a list of tuples by second value
n = int(input("How many tuples? "))
data = []
for _ in range(n):
    t1 = int(input("  Enter first element of tuple: "))
    t2 = int(input("  Enter second element of tuple: "))
    data.append((t1, t2))
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted by second value:", sorted_data)


# 3. Use lambda with filter to get even numbers
nums = input("Enter numbers separated by space: ")
numbers = list(map(int, nums.split()))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)


# 4. Use lambda with map to square a list of numbers
nums = input("Enter numbers to square (space-separated): ")
nums_list = list(map(int, nums.split()))
squares = list(map(lambda x: x * x, nums_list))
print("Squares:", squares)


# 5. Use lambda with reduce to sum a list
from functools import reduce
nums = input("Enter numbers to sum (space-separated): ")
num_list = list(map(int, nums.split()))
total = reduce(lambda x, y: x + y, num_list,0)
print("Sum:", total)