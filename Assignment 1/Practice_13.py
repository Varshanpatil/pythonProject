#Write a program to find last 10 characters of a string?

# Get input from the user
string = input("Enter a string: ")

# Get the last 10 characters using slicing
last_10_chars = string[-10:]

print("Last 10 characters:", last_10_chars)