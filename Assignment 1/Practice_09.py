#Write a program to find the number of vowels, consonants, digits, and white space characters in a string

# Get input from the user
user_input = input("Enter a string: ")

#Intialize counters
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0

# Define vowels for reference
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in user_input:
    if char in vowels:   # Check if the character is a vowel
        vowel_count =+1
    elif char.isalpha():  # Check if the character is a consonant
        consonant_count=+1
    elif char.isdigit():   # Check if the character is a digit
        digit_count =+1
    elif char.isspace():   # Check if the character is a whitespace
        space_count =+1

# Print the results
print("Vowels : ", vowel_count)
print("Consonants : ", consonant_count)
print("Digit: ", digit_count)
print("Space: ", space_count)

#Explaination
#1.Check for Vowel:
#If char is in the vowels string, it is a vowel.Increment the vowel_count by 1.

#2.Check for Consonant:
#The isalpha() method checks if the character is an alphabetic letter (A-Z or a-z).
#If it’s not a vowel (as checked earlier) and is alphabetic, it must be a consonant.
#Increment the consonant_count by 1.

#3.Check for Digit:
#The isdigit() method checks if the character is a numeric digit (0-9).
#Increment the digit_count by 1.

#4.Check for Whitespace:
#The isspace() method checks if the character is a space, tab, or newline (whitespace).
#Increment the whitespace_count by 1.

