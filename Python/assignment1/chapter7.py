#count vowels and consonents
text = input("Enter a string: ")
text = text.lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha(): 
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
#string palindrome

text = input("Enter a string: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#replace spaces with dashes

text = input("Enter a string: ")

modified_text = text.replace(" ", "-")

print("Modified string:", modified_text)


#split into 1st and last

full_name = input("Enter your full name: ")

name_parts = full_name.strip().split()

if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    print("First Name:", first_name)
    print("Last Name:", last_name)
else:
    print("Please enter both first and last name.")


#capitalize each word in sentance

sentence = input("Enter a sentence: ")

capitalized_sentence = sentence.title()

print("Capitalized sentence:", capitalized_sentence)

