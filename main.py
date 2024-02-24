# Problem Set 3
# Vowels and Consonants

'''
    Write a program that takes a string input and counts the number of vowels and consonants in it.
'''

vowels = 0
consonants = 0

usr_string = input("Enter your string: ")
for letter in usr_string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowels += 1
    else:
        consonants += 1

print(f"There were {vowels} vowels.")
print(f"There were {consonants} consonants.")
