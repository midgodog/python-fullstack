# 1. Write a function to add two numbers
def add_numbers(a, b):
    return a + b

a = int(input("\nEnter first number to add: "))
b = int(input("Enter second number to add: "))
print("Sum:", add_numbers(a, b))


# 2. Create a function that checks if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("\nEnter a number to check for prime: "))
print("Is Prime?" , is_prime(num))


# 3. Write a function to reverse a string
def reverse_string(s):
    return s[::-1]

text = input("\nEnter a string to reverse: ")
print("Reversed string:", reverse_string(text))


# 4. Use *args and **kwargs in a function
def demo_args_kwargs(*args, **kwargs):
    print("\n*args values:", args)
    print("**kwargs values:", kwargs)

demo_args_kwargs(1, 2, 3, name="Shreyas", age=18)


# 5. Create a function to count vowels in a sentence
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

sentence = input("\nEnter a sentence to count vowels: ")
print("Number of vowels:", count_vowels(sentence))