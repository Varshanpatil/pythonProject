#Write a program to make a new string with all the consonants deleted from the string "Hello, have a good day".
# Original string
original_string = "Hello, have a good day"

# Define vowels for reference
vowels = "aeiouAEIOU"

# Initialize an empty string to store the result
new_string = ""

# Loop through each character in the original string
for char in original_string:
    if char in vowels or not char.isalpha():  # Keep vowels and non-alphabetic characters
        new_string += char

# Print the new string
print("String without consonants:", new_string)


#Explaination
#Step 1: Define the Original String->  original_string = "Hello, have a good day"
#The given string "Hello, have a good day" is assigned to the variable original_string.
#This will be the string we process.

#Step 2: Define Vowels

#Step 3: Initialize an Empty String ->new_string = ""
#An empty string new_string is initialized.
#This string will store the result after removing all consonants from the original string.

#Step 4: Loop Through Each Character ->for char in original_string:
#A for loop is used to iterate through each character in the original_string.

#Step 5: Check Each Character
#Condition Explanation:
#char in vowels: Checks if the current character is a vowel.
#not char.isalpha(): Checks if the character is not a letter (e.g., spaces, punctuation like ,).
#Action:If the character is a vowel or non-alphabetic, it is added to the new_string.
#Skip Consonants:If the character is a consonant, it is ignored, and nothing is added to new_string.

#Step 6: Add to the Result String
#The operation new_string += char appends the character to new_string if it meets the condition in Step 5.

#Step 7: Print the Result


