# Program to create a list of 5 favorite movies

favorite_movies = ["one piece", "thor", "mass", "titanic", "fast and furious tokyo drift"]

print("My 5 favorite movies are:")
for movie in favorite_movies:
    print("-", movie)



# Program to create a dictionary with keys: name, age, course

student = {
    "name": "shreyas",
    "age": 18,
    "course": "Full stack Python"
}

print("Student Profile:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])



# Program to add and remove items from a set

skins = {"m416 glacier", "ump glacier", "akm glacier"}

skins.add("shinobi kami m416")
print("After adding 'shinobi kami m416':", skins)

skins.remove("m416 glacier")
print("After removing 'm416 glacier':", skins)

skins.discard("akm glacier")
print("After discarding 'akm glacier':", skins)



# Program to sort a list of numbers

numbers = [7,10,12,8,19]
numbers.sort()

print("Sorted list in ascending order:", numbers)

numbers.sort(reverse=True)
print("Sorted list in descending order:", numbers)



# Program to loop through a dictionary and print key-value pairs

student = {
    "name": "Shreyas",
    "age": 18,
    "course": "Computer Engineering"
}



print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")



