#Write a Python program to count Uppercase, Lowercase, special character,numeric values in a given string

# Get string input from the user
user_input = input("Enter a string: ")

# Initialize counters
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
special_count = 0

# Loop through each character in the string
for char in user_input:
    if char.isupper():  # Check if the character is uppercase
        uppercase_count += 1
    elif char.islower():  # Check if the character is lowercase
        lowercase_count += 1
    elif char.isdigit():  # Check if the character is a digit
        numeric_count += 1
    else:  # If not uppercase, lowercase, or digit, it is a special character
        special_count += 1

# Print the results
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Numeric values:", numeric_count)
print("Special characters:", special_count)


#Explaination
#1.Initialize Counters:uppercase_count = 0, lowercase_count = 0,numeric_count = 0 special_count = 0
# These variables keep track of counts for each type of character.

#2.Loop through the string:for char in user_input:
# A for loop iterates over each character in the input string.

#3.Character Checks:
#Uppercase - The isupper() method checks if the character is uppercase.
#Lowercase - The islower() method checks if the character is lowercase.
#Numeric - The isdigit() method checks if the character is numeric.
#Special Character - If the character is none of the above, it is considered a special character.

#What is special_count? special_count = 0
#special_count is a variable that acts as a counter.Its purpose is to keep track of the number of special characters in the string.
#It is initialized at the beginning of the program.At this point, it is set to 0 because no characters have been counted yet.

#What does += mean?
#The operator += is a shorthand for incrementing a variable.
#It takes the current value of special_count, adds 1 to it, and updates special_count with the new value.
#Each time the program encounters a special character (a character that is not uppercase, lowercase, or numeric), we need to increment the counter by 1.
#This ensures that the program keeps an accurate count of how many special characters are in the string.

