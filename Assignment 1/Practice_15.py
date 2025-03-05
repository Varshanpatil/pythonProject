#How do you count the occurrence of a given character in a string?


# Get input from the user
string = input("Enter a string: ")
char = input("Enter the character to count: ")

# Use count() method
count = string.count(char)

print(f"The character '{char}' appears {count} times.")