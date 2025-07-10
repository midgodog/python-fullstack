# Program to print numbers from 1 to 10, skipping 5

for num in range(1, 11):
    if num == 5:
        continue 
    print(num)
    
    # Using pass in an empty function

def my_function():
    pass  

my_function()


# Program to sum numbers until the total reaches or exceeds 100
total = 0
num = 1

while total < 100:
    total += num
    num += 1

print("The sum has reached or exceeded 100.")
print("Final sum:", total)
print("Last number added:", num - 1)


# Program to break the loop if a negative number is entered
while True:
    num = int(input("Enter a number (negative number to stop): "))
    if num < 0:
        print("Negative number entered. Exiting loop.")
        break
    print("You entered:", num)


# Program to print all vowels in a string

text = input("Enter a string: ")

vowels = "a e i o u"

print("Vowels in the string are:")
for char in text:
    if char in vowels:
        print(char)


