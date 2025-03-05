#WAP to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# Get input from the user
string = input("Enter a string: ")

# Count uppercase letters in the first 4 characters
count = 0
for char in string[:4]:
    if char.isupper():
        count += 1

# Convert to uppercase if at least 2 uppercase letters are found
if count >= 2:
    string = string.upper()

print("Result:", string)