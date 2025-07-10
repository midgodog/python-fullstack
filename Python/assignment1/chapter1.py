Name=input("Enter name")
Age=input("Enter Age")
Country=input("Enter Country")
print("Name",Name,"Age",Age,"Country",Country)



# Program to convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")


# Program to check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")



# Program to store a user profile and print it in a sentence

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profession = input("Enter your profession: ")

print(f"{name} is {age} years old, lives in {city}, and works as a {profession}.")


# Program to take user input for three numbers and find the average

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print(f"The average of the three numbers is: {average}")

